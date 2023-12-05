from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    
VERSION = '0.0.1'
DESCRIPTION = 'NeuraNET Python API library'
LONG_DESCRIPTION = 'NeuraNET Python API library'


setup(
    name='neuranet',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author='Dark25 (Ruben Roy)',
    author_email='me@ruben-roy.com',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['ai', 'machine learning', 'neuranet']
)
