import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['api']

requires = [
    "Flask==2.3.2"
]
test_requirements = [
    "pytest==5.4.2"
]

with open('README.md') as f:
    readme = f.read()

setup(
    name="Flask test API",
    version="0.0.1",
    description="Small test API",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Lucas Diniz",
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    tests_require=test_requirements,
)
