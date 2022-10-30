<%!
    import pydmt.helpers.misc
    import pydmt.helpers.project
    import pydmt.helpers.python
    import pydmt.helpers.urls
    import config.python
    import default.python
    import user.personal
    import config.project
    import config.version
    import pydmt.helpers.python
    import os.path
%>[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "${pydmt.helpers.project.get_name()}"
description = "${config.project.description_short}"
version = "${pydmt.helpers.misc.get_version_str()}"

packages = [{ include = "${pydmt.helpers.project.get_name()}" }]

license = "${pydmt.helpers.python.get_license_type()}"
authors = [
	{ name = "${user.personal.fullname}", email = "${user.personal.email}", }
]

% if os.path.isfile("README.rst"):
readme = "README.rst"
% endif

keywords = ${pydmt.helpers.python.array_indented(0, config.project.keywords)}

classifiers = ${pydmt.helpers.python.array_indented(0, pydmt.helpers.python.get_classifiers())}

requires-python = "${default.python.python_requires}"

dependencies = [
% if hasattr(config.python, "install_requires"):
${config.python.install_requires}
% endif
% if hasattr(config.python, "extras_requires"):
${config.python.extras_requires}
% endif
]

[project.optional-dependencies]
% if hasattr(config.python, "dev_requires"):
dev = ${config.python.dev_requires}
% endif

% if hasattr(config.python, "console_scripts"):
[tool.poetry.scripts]
script = "{config.python.console_scripts}"
% endif
