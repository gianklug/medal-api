import os
from setuptools import setup, find_packages

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="medal-api",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="Gian Klug",
    author_email="gian.klug@ict-scouts.ch",
    packages=find_packages("medal_api"),
    package_dir={"": "medal_api"},
    setup_requires=["requests"]
)
