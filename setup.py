#!/usr/env/bin python3

from setuptools import setup

description = 'A Simple MyLTT API Helper'
__version__ = '1.0'

try:
	long_description = open('README.md', 'r').read()
except IOError:
	long_description = description

setup(
	name='myltt',
	version=__version__,
	packages=['myltt'],
	author='Safwan Ljd',
	license_files=('LICENSE',),
	description=description,
	long_description=long_description,
	long_description_content_type='text/markdown',
	python_requires='>=3.6',
	url='https://gitlab.com/SafwanLjd/MyLTT',
	download_url=f'https://gitlab.com/SafwanLjd/MyLTT/-/archive/v{__version__}/MyLTT-v{__version__}.tar.gz',
	install_requires=['requests'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: OS Independent'
	]
)
