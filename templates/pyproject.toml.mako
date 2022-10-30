<%!
    import pydmt.helpers.misc
    import pydmt.helpers.project
    import pydmt.helpers.python
    import pydmt.helpers.urls
    import config.python
    import user.personal
    import config.project
    import config.version
    import pydmt.helpers.python
%>[tool.poetry]

name = "${pydmt.helpers.project.get_name()}"
version = "${pydmt.helpers.misc.get_version_str()}"
description = "${config.project.description_short}"

packages = [{ include = "${pydmt.helpers.project.get_name()}" }]

license = "${pydmt.helpers.python.get_license_type()}"
authors = ["${user.personal.fullname}"]

readme = "README.rst"

homepage = "https://pypi.org/project/TemplateDemo"
documentation = "https://TemplateDemo.readthedocs.io"
repository = "https://github.com/jacebrowning/template-python-demo"

keywords = ${pydmt.helpers.python.array_indented(0, config.project.keywords)}

classifiers = ${pydmt.helpers.python.array_indented(0, pydmt.helpers.python.get_classifiers())}

[tool.poetry.dependencies]

python = "^3.9"

# TODO: Remove these and add your library's requirements
click = "*"
minilog = "*"

[tool.poetry.dev-dependencies]

# Formatters
black = "^22.1"
isort = "^5.10"

# Linters
mypy = "~0.931"
pydocstyle = "^6.1"
pylint = "~2.12.2"
types-setuptools = "*"

# Testing
pytest = "^7.1"
pytest-describe = "^2.0"
pytest-expecter = "^3.0"
pytest-random = "*"
pytest-cov = "^3.0"
freezegun = "*"

# Reports
coveragespace = "^6.0"

# Documentation
mkdocs = "~1.3"
pygments = "^2.11.1"

# Tooling
pyinstaller = "*"
sniffer = "*"
MacFSEvents = { version = "*", platform = "darwin" }
pync = { version = "*", platform = "darwin" }
ipython = "^7.12.0"

[tool.poetry.scripts]

TemplateDemo = "demo.cli:main"

[tool.black]

quiet = true

[tool.isort]

profile = "black"

[tool.mypy]

ignore_missing_imports = true
no_implicit_optional = true
check_untyped_defs = true

cache_dir = ".cache/mypy/"

[tool.pytest.ini_options]

addopts = """
--strict-markers

-r sxX
--show-capture=log

--cov-report=html
--cov-report=term-missing:skip-covered
--no-cov-on-fail
"""

cache_dir = ".cache/pytest/"

markers = []

[build-system]

requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
