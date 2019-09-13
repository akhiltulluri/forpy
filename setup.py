from setuptools import setup, find_packages

setup(
    name='forpy',
    version='1.0.0',
    description='An async Python API wrapper for the Fortnite API',
    long_description='Powered by fortnitetracker.com. ',
    url='https://github.com/Akhil2149/fortpy',
    author='Akhil',
    author_email='akhilaug2003@gmail.com',
    license='MIT',
    keywords=['fortnite, forpy, api-wrapper, async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
)