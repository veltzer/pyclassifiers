""" python depedencies for this project """
from typing import List


dev_requires: List[str] = [
    "pypitools",
    "black",
    "requests",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = []
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
    "mypy",
    "types-requests",
]
requires = config_requires + install_requires + build_requires + test_requires
