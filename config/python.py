from typing import List


dev_requires: List[str] = [
    "pymultigit",
    "pypitools",
    "black",
    "requests",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = []
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
    "mypy",
    "types-requests",
]
requires = config_requires + install_requires + make_requires + test_requires
