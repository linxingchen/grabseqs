import setuptools
from distutils.core import setup

setup(name='grabseqs',
	version='0.3.3',
	description='Easily download reads from next-gen sequencing repositories like NCBI SRA',
	author='Louis J Taylor',
	author_email='l'+'ouis'+'@'+'u'+'penn.edu',
	url='https://github.com/louiejtaylor/grabseqs',
	packages=['grabseqslib'],
	license='MIT License',
	entry_points={'console_scripts': [
	'grabseqs = grabseqslib:main'
	]},
	classifiers = ['Intended Audience :: Science/Research',
				'Environment :: Console',
				'Environment :: Web Environment',
				'License :: OSI Approved :: MIT License',
				'Programming Language :: Python :: 3',
				'Topic :: Scientific/Engineering :: Bio-Informatics',],
	py_modules = ['sra','mgrast']
)