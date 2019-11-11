import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alpha-orm",
    version="0.0.1",
    author="Claret Nnamocha",
    author_email="devclareo@gmail.com",
    description="A nice database orm written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alpha-orm/python-alpha-orm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)