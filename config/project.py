import pyclassifiers.values

github_username = "veltzer"
name = "pyclassifiers"
github_repo_name = name
website = f"https://{github_username}.github.io/{name}"
website_source = f"https://github.com/{github_username}/{name}"
website_git = f"git://github.com/{github_username}/{name}.git"
website_download_ppa = "https://launchpanet/~mark-veltzer/+archive/ubuntu/ppa"
website_download_src = website_source
description_short = "classifiers from pypi"
keywords = [
    "classifiers",
    "python",
    "pypi",
    "setuptools",
    "distutils",
]
license_type = "MIT"
year_started = 2017
platforms = [
    "python3",
]
classifiers = [
    pyclassifiers.values.DevelopmentStatus__4_Beta,
    pyclassifiers.values.Environment__Console,
    pyclassifiers.values.OperatingSystem__OSIndependent,
    pyclassifiers.values.ProgrammingLanguage__Python,
    pyclassifiers.values.ProgrammingLanguage__Python__3,
    pyclassifiers.values.ProgrammingLanguage__Python__3__Only,
    pyclassifiers.values.ProgrammingLanguage__Python__310,
    pyclassifiers.values.Topic__Utilities,
    pyclassifiers.values.License__OSIApproved__MITLicense,
]
