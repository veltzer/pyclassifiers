import config.project

package_name = config.project.project_name

console_scripts = [
]
setup_requires = [
]
install_requires = [
]
test_requires = [
    "pytest",
    "pytest-cov",
    "pymakehelper",
    "flake8",
    "pylint",
]
dev_requires = [
    'pydmt',
    'pypitools',
    'requests',
    'pyclassifiers',
]
requirements3 = install_requires

python_requires = ">=3.6"

extras_require = {
}
