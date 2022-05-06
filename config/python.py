import config.project

package_name = config.project.project_name

test_requires = [
    "pytest",
    "pytest-cov",
    "pymakehelper",
    "flake8",
    "pylint",
]
dev_requires = [
    "pydmt",
    "pypitools",
    "requests",
    "pyclassifiers",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
