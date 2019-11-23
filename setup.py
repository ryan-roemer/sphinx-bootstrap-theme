"""Sphinx Bootstrap Theme package."""
import os
import setuptools

# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# Setup the package.
setuptools.setup()
