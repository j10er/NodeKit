#!/usr/bin/env python
import argparse
import os
import shutil
import subprocess

addon_name = "GeoNodeDevelopment"
addon_id = "geo_node_development"


def build(fast=False):
    source_dir = f"./{addon_name}"
    filename = addon_name
    if fast:
        print(f"Building addon: Zipping folder {source_dir} to {filename}.zip")
        shutil.make_archive(addon_name, "zip", addon_name)
    else:
        version = "4.4.3"
        print(f"Building addon: Using blender version {version} to build")
        setup_blender("./blender", version)
        subprocess.run(
            [
                f"./blender/blender-{version}/blender",
                "--command",
                "extension",
                "build",
                "--source-dir",
                source_dir,
                "--output-filepath",
                f"{filename}.zip",
            ]
        )


def run_tests(blender_executable):
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
    print("Tests passed")


def setup_blender(blender_path, version):
    major_version = version[:3]
    if not os.path.exists(blender_path):
        os.makedirs(blender_path)
    if not os.path.exists(f"{blender_path}/blender-{version}"):
        print(f"Downloading Blender {version}.")

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
        print(f"Blender {version} already downloaded. Resetting existing installation.")
        shutil.rmtree(f"{blender_path}/blender-{version}/portable")
        os.mkdir(f"{blender_path}/blender-{version}/portable")


def install_test_deps(blender_path, version):
    major_version = version[:3]
    python_dir = f"{blender_path}/blender-{version}/{major_version}/python/bin/"
    python_executable = f"{python_dir}/{next(name for name in os.listdir(python_dir) if name.startswith('python3.'))}"
    subprocess.run([python_executable, "-m", "pip", "install", "pytest", "-q", "-q"])


def test():
    blender_versions = ["4.4.3"]
    blender_path = "./blender"
    for version in blender_versions:

        setup_blender(blender_path, version)
        install_test_deps(blender_path, version)
        print(f"Running tests for Blender version {version}")
        run_tests(blender_executable=f"{blender_path}/blender-{version}/blender")


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
    "--fast",
    action=argparse.BooleanOptionalAction,
    help="Do not use the blender addon builder and instead just zip the folder",
)
parser.add_argument(
    "--skip-rebuild",
    action=argparse.BooleanOptionalAction,
    help="Do not rebuild the addon when running the tests, only viable when there are no changes in the addon code",
)
args = parser.parse_args()

if args.command == "build":
    build(args.fast)
elif args.command == "test":
    if not args.skip_rebuild:
        build(args.fast)
    test()
else:
    parser.print_help()
