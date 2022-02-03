from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Strength_predict"
AUTHOR_USER_NAME = "Sarad_Mishra"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="AI in civil engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python = 3.7,
    packages=[SRC_REPO],
    license="MIT",
    install_requires=LIST_OF_REQUIREMENTS
)