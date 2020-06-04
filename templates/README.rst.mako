<%!
    import config.project
    import user.personal
    import config.version
    import os
    line = '=' * (len(config.project.project_name)+2)
%>${line}
*${config.project.project_name}*
${line}

author: ${user.personal.personal_fullname}

version: ${config.version.version_str}

% if os.path.isfile("snipplets/main.rst.mako"):
<%include file="../snipplets/main.rst.mako" />
% endif
