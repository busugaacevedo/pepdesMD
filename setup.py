from setuptools import setup


INSTALL_REQUIRES = ["Biopython"]

TEST_REQUIRES = [
    # testing and coverage
    "pytest",
    "coverage",
    "pytest-cov",
    # to be able to run `python setup.py checkdocs`
    "collective.checkdocs",
    "pygments",
]


with open("README.md", "r") as f:
    long_description = f.read()

with open("pepdesMD/__init__.py", "r") as f:
    init = f.readlines()

for line in init:
    if "__version__" in line:
        __version__ = line.split('"')[-2]

setup(
    name="pepdesMD",
    version=__version__,
    author="Usuga Brandon",
    author_email="brandon.usuga@gmail.com",
    description="Build peptide PDB files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    download_url="https://github.com/busugaacevedo/peptideDesign_MD",
    platforms="Tested on Linux, Ubuntu",
    packages=["pepdesMD"],
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES + INSTALL_REQUIRES,},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",
    ],
)
