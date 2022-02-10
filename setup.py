import os
from setuptools import setup

setup(name='python-fritzbox',
  version='0.3',
  description='Automate the Fritz!Box with python',
  url='https://github.com/PhilippLange/python-fritzbox',
  author='Philipp Lange',
  author_email='philipp.i.b.lange@gmail.com',
  license='GNU',
  packages=['fritzbox', 'tools'],
  zip_safe=False,
  install_requires=[
      'Pillow',
      'ldif3',
      'requests',
      'vobject'
  ],
  scripts=[
    os.path.join('tools', 'fritzboxphonebook.py'),
    os.path.join('tools', 'fritzboxktipp.py'),
  ]
)

