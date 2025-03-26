import sys
import pytest


if __name__ == "__main__":
    result = pytest.main(["./tests/", "-v"])
    if result != 0:
        sys.exit(1)
