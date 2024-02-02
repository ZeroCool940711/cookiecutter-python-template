import os
from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
#__version__ = run_path('src/{{ cookiecutter.module_name }}/version.py')['__version__']
import versioneer


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="{{ cookiecutter.project_slug }}",
    version=versioneer.get_version(),
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    license="proprietary",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'{{ cookiecutter.module_name }}': ['res/*']},
    long_description=read('README.md'),
    install_requires=[],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pre-commit',
    ],
    platforms='any',
    python_requires='>=3.8',
    cmdclass=versioneer.get_cmdclass(),
)
