""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    "requests",
]
test_requires: list[str] = [
    "pytest",
    "pylint",
    "mypy",
    "ruff",
    # types
    "types-requests",
]
requires = config_requires + build_requires + test_requires
