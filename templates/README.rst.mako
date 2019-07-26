<%!
    import config.project
    import user.personal
    import config.version
    line = '=' * (len(config.project.project_name)+2)
%>${line}
*${config.project.project_name}*
${line}

author: ${user.personal.personal_fullname}

version: ${config.version.version_str}

The idea of this module is turn the classifiers list of pypi to a list of
variables in a namespace so that people will never be wrong in specifying
the classifiers themselves.

The classifiers are at: https://pypi.python.org/pypi?%3Aaction=list_classifiers
