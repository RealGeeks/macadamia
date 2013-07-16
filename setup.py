#!/usr/bin/env python

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='macademia',
      version='0.0.1',
      description="A parser for Google Analytics Cookies",
      author='Kevin McCarthy',
      author_email='me@kevinmccarthy.org',
      url='https://github.com/realgeeks/macademia',
      packages=['macademia'],
      install_requires=['PyYAML'],
      license='MIT',
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
          'Topic :: Internet :: WWW/HTTP',
          'License :: OSI Approved :: MIT License',
      ],
)
