import config.project

package_name = config.project.project_name

console_scripts = [
]
setup_requires = [
]
install_requires = [
]
test_requires = [
]
dev_requires = [
    'pydmt',  # for building
    'pypitools',  # for uploading
    'requests',  # for requesting
    'pyclassifiers',  # for classifying the software
]
requirements3 = install_requires 

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
