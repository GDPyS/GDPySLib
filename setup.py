from pathlib import Path

import setuptools

from gdpyslib import __author__ as LIB_AUTHORS
from gdpyslib import __version__ as LIB_VERSION

README = Path.cwd() / "README.md"

setuptools.setup(
    name="GDPySLib",
    version=LIB_VERSION,
    author=LIB_AUTHORS,
    description="Python library for GDPyS",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/GDPyS/GDPySLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
