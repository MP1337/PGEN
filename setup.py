from setuptools import setup
from codecs import open
from os import path

setup(
    name='PGEN Simple Password Generator',
    version='1.0.0',
    description='Simple Strong Password Generator',
    author='Peter Mazela',
    author_email='info@elix-it.de',
    license='GPLv2',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    ],
    keywords='password generator',
    install_requires=['pyqt5'],
    packages = ["pgen_start"],
    scripts = ["pgen_start"]
)
