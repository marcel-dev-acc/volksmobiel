from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess


class Autopep8Command(install):
    """Custom command to run autopep8."""
    description = 'run autopep8'

    def run(self):
        print("Running autopep8...")
        command = ['autopep8', '--in-place', '--recursive', '.']
        subprocess.call(command)

class TypeHintsCommand(install):
    """Custom command to add type hints to docstrings"""
    description = 'add type hints to docstrings'

    def run(self):
        print("Running sphinx-autodoc-typehints...")
        command = ['sphinx-autodoc-typehints', '--in-place', '--recursive', '.']
        subprocess.call(command)


setup(
    name='volksmobiel',
    version='1.0',
    packages=find_packages(),
    cmdclass={
        'autopep8': Autopep8Command,
        'typehints': TypeHintsCommand,
    },
)
