from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='cantailme-client',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='http://cantail.me/',
      license='GPLм2+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'tailme=cantailmeclient.client:main',
          ]
      },
      )
