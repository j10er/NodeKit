#!/usr/bin/env python
import argparse
import logging
import os
import shutil
import subprocess

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Should match the addon name in blender_manifest.toml
addon_name = "NodeKit"


def build():

    source_dir = f"./{addon_name}"
    filename = addon_name
    config_path = f"{source_dir}/config.py"
    debug_line = "DEBUG = False"
    with open(config_path, "a") as file:
        file.write(f"{debug_line}")
    build_version = "4.5.0"
    log.info(f"Building addon: Using blender version {build_version} to build")

    _setup_blender("./blender", build_version)
    subprocess.run(
        [
            f"./blender/blender-{build_version}/blender",
            "--command",
            "extension",
            "build",
            "--source-dir",
            source_dir,
            "--output-filepath",
            f"{filename}.zip",
        ]
    )

    with open(config_path, "r") as file:
        lines = file.readlines()
    with open(config_path, "w") as file:
        for line in lines:
            if line.strip() != debug_line.strip():
                file.write(line)


def _run_tests(blender_executable):
    # Install addon
    subprocess.run(
        [
            blender_executable,
            "--command",
            "extension",
            "install-file",
            "-r",
            "user_default",
            "-e",
            f"{addon_name}.zip",
        ]
    )
    # Run tests
    result = subprocess.run(
        [
            blender_executable,
            "--background",
            "--python-exit-code",
            "1",
            "--python",
            "run_tests.py",
        ]
    )
    if result.returncode != 0:
        raise Exception("Tests failed")
    log.info("Tests passed")


def _setup_blender(blender_path, version):
    major_version = version[:3]
    if not os.path.exists(blender_path):
        os.makedirs(blender_path)
    if not os.path.exists(f"{blender_path}/blender-{version}"):
        log.info(f"Downloading Blender {version}.")

        subprocess.run(
            [
                "wget",
                "-nv",
                f"https://download.blender.org/release/Blender{major_version}/blender-{version}-linux-x64.tar.xz",
            ]
        )

        shutil.unpack_archive(f"blender-{version}-linux-x64.tar.xz")
        shutil.move(f"blender-{version}-linux-x64", f"{blender_path}/blender-{version}")
        os.remove(f"blender-{version}-linux-x64.tar.xz")
        os.mkdir(f"{blender_path}/blender-{version}/portable")
    else:
        log.info(
            f"Blender {version} already downloaded. Resetting existing installation."
        )
        shutil.rmtree(f"{blender_path}/blender-{version}/portable")
        os.mkdir(f"{blender_path}/blender-{version}/portable")


def _install_test_deps(blender_path, version):
    major_version = version[:3]
    python_dir = f"{blender_path}/blender-{version}/{major_version}/python/bin/"
    python_executable = f"{python_dir}/{next(name for name in os.listdir(python_dir) if name.startswith('python3.'))}"
    subprocess.run([python_executable, "-m", "pip", "install", "pytest", "-q", "-q"])


def test():
    blender_versions = ["4.5.0"]
    blender_path = "./blender"
    for version in blender_versions:

        _setup_blender(blender_path, version)
        _install_test_deps(blender_path, version)
        log.info(f"Running tests for Blender version {version}")
        _run_tests(blender_executable=f"{blender_path}/blender-{version}/blender")


# COMMAND LINE INTERFACE

parser = argparse.ArgumentParser()
parser.add_argument(
    "command",
    choices=["build", "test", "release"],
    help="""
  TEST = build with test files and run tests
  BUILD = Create the zip
  """,
)
parser.add_argument(
    "--skip-rebuild",
    action=argparse.BooleanOptionalAction,
    help="Do not rebuild the addon when running the tests, only viable when there are no changes in the addon code",
)
args = parser.parse_args()

if args.command == "build":
    build()
elif args.command == "test":
    if not args.skip_rebuild:
        build()
    test()
else:
    parser.log.info_help()
