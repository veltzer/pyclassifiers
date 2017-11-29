<%!
    import config.project
    import config.personal
    import config.version
%>${'=' * (len(config.project.project_name)+2)}
*${config.project.project_name}*
${'=' * (len(config.project.project_name)+2)}

author: ${config.personal.personal_fullname}

version: ${config.version.version_str}
