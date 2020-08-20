"""
===================
zms-skins
===================
The Zope Product zms-skins acts as a helper to register filesystem pathes for
your Zope skins with CMFCore.registerDirectory. To make the product generally
working its configure.zcml contains only one recursive directory registration:
/skins
For using your skins with the Zope instances based on current virtual python
context, please add your projects skin-code folders as symlinks to this /skins
folder.
"""
from setuptools import setup, find_packages

setup(
    name='Products.zms-skins',
    version='0.0.1',
    url='https://github.com/zms-publishing/zms-skins',
    author='HOFFMANN+LIEBENBERG in association with SNTL Publishing, Berlin',
    author_email='zms@sntl-publishing.com',
    description='Registry for Filesystem based Zope Skins',
    packages=find_packages('src'),
    namespace_packages=['Products'],
    package_dir={'': 'src'},
    zip_safe=False,
)