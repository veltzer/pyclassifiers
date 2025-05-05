""" platform definition """

import pyclassifiers.values

python_requires = ">=3.12"

license_type = "MIT AND (Apache-2.0 OR BSD-2-Clause)"

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
    pyclassifiers.values.ProgrammingLanguage__Python__312,
    pyclassifiers.values.Topic__Utilities,
]
