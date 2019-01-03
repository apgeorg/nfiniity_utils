import setuptools
import nfiniity_utils


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nfiniity_utils",
    version=nfiniity_utils.__version__,
    author="Apostolos Georgiadis",
    author_email="apostolos.georgiadis@nfiniity.com",
    description=" Diverse python utilities by nfiniity GmbH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apgeorg/nfiniity_utils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
