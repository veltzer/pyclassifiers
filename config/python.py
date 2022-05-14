import config.project

package_name = config.project.project_name

dev_requires = [
    "pypitools",
]
make_requires = [
    "pymakehelper",
]
config_requires = [
    "pyclassifiers",
]
install_requires = [
    "requests",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
