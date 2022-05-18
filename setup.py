import setuptools


def get_readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pyclassifiers",
    version="0.0.7",
    packages=[
        'pyclassifiers',
    ],
    # from here all is optional
    description="classifiers from pypi",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        'classifiers',
        'python',
        'pypi',
        'setuptools',
        'distutils',
    ],
    url="https://veltzer.github.io/pyclassifiers",
    download_url="https://github.com/veltzer/pyclassifiers",
    license="MIT",
    platforms=[
        'python3',
    ],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=">=3.10",
)
