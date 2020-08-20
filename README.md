# Products.zms-skins
Registry for Filesystem based Zope Skins

The Zope Product zms-skins acts as a helper to register filesystem pathes for
your Zope skins with CMFCore.registerDirectory. To make the product generally
working its configure.zcml contains only one recursive directory registration:
./skins
For using your skins with the Zope instances based on the current virtual python
context, please add your projects skin-code folders as symlinks to the empty
./skins folder.
