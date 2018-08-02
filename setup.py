from setuptools import setup, find_packages
import src

setup(
    name='DungeonMasterBot',
    version=src.__version__,
    packages=find_packages(),
    author='Andrew Volski',
    author_email='andrew.volski@gmail.com',
    install_requires=['discord'],
    description='Simple Discord bot for help players'
)
