import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nfiniity_utils",
    version="0.0.4",
    author="Apostolos Georgiadis",
    author_email="apostolos.georgiadis@nfiniity.com",
    description=" Diverse python utils by nfiniity GmbH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apgeorg/nfiniity_utils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
