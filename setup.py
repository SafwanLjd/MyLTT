from setuptools import setup

description = 'A Simple MyLTT API Helper'
__version__ = '0.1'

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
	url='https://github.com/SafwanLjd/MyLTT',
	download_url=f'https://github.com/SafwanLjd/MyLTT/archive/refs/tags/v{__version__}.tar.gz',
	install_requires=['requests'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
)
