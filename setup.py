import os
import sys
import poll_directory

from setuptools import setup

#if sys.argv[-1] == 'test':
#    os.system('nosetests tests/tests.py')
#    sys.exit()

setup(
    name='poll_directory',
    version=poll_directory.__version__,
    description='Convert XML documents into Python objects',
    long_description=__doc__,
    author='Norman Moeschter',
    author_email='normo@posteo.de',
    url='http://',
    #py_modules=['poll_directory'],
    #packages=['packages/files', 'packages/hasher', 'packages/logger'],
    # Include additional files into the package
    include_package_data=True,
    license='MIT', 
    # long_description=open("README.txt").read(),  
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        #'License :: OSI Approved :: MIT License',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        #'Programming Language :: Python :: 3.0',
    )
    
    #,
    ## Dependent packages (distributions)
    #install_requires=[
    #    "flask",
    #]
    #test_suite = 'nose.collector'    
)
