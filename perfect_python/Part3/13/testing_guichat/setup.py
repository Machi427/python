from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.txt')) as f:
    readme = f.read()

setup(
    name="ppjp.chat",
    packages=['ppjp.chat'],
    version="0.1",
    author="Perfect Python",
    author_email="ppjp@perfoectpython.jp",
    description="a simple gui chat application",
    long_description=readme,
    url='http://pypi.python.org/ppjp.chat',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Communications :: Chat",
    ],
    test_suite="ppjp.chat",
)
