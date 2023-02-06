import os
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

BUILD_ID = os.environ.get("BUILD_BUILDID", "3")

setup(
    name="medal-api",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="Gian Klug",
    author_email="gian.klug@ict-scouts.ch",
    url="https://github.com/gianklug/medal-api",
    packages=find_packages("medal_api"),
    package_dir={"": "medal_api"},
    setup_requires=["requests"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
