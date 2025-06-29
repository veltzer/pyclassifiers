""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
    # modules
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
