dev_requires = [
    "pypitools",
    "requests",
]
config_requires = [
    "pyclassifiers",
]
install_requires = []
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
    "mypy",
    "types-requests",
]
requires = config_requires + install_requires + make_requires + test_requires
