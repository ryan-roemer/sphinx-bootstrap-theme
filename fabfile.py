"""Fabric file."""

import os

from fabric.api import local, lcd
from fabric.decorators import task

@task
def bundle():
    """Create zip file upload bundles."""
    git_hash = local("git rev-parse HEAD", capture=True).strip()
    
    print("Cleaning old build files.")
    clean()
    
    print("Bundling new files.")
    with lcd("bootstrap"):
        local("zip -r ../bootstrap.zip .")
    local("cp bootstrap.zip bootstrap-%s.zip" % git_hash)

    print("Verifying contents.")
    local("unzip -l bootstrap.zip")

@task
def clean():
    """Clean up build files."""
    local("rm -rf bootstrap-*.zip bootstrap.zip")
