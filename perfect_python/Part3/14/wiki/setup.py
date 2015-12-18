from setuptools import setup, find_packages

setup(
    name="py3wiki",
    install_requires=[
        'webob',
        'webdispatch',
        'jinja2',
        'sqlalchemy',
        'docutils>=0.10',
    ],
    packages=find_packages(),
    test_suite='py3wiki',
    )

