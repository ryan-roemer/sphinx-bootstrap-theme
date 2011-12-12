"""Fabric file."""

import os
import json
import urllib2

from fabric.api import local, lcd
from fabric.decorators import task

GH_USER = "ryan-roemer"
GH_REPO = "sphinx-bootstrap-theme"
GH_TOKEN = os.environ.get("GITHUB_TOKEN", None)
GH_BASE = "https://api.github.com"


@task
def clean():
    """Clean up build files."""
    local("rm -rf bootstrap-*.zip bootstrap.zip")


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


def gh_op(path):
    """Perform a GitHub API request and decode to JSON."""
    url_path = "/".join((GH_BASE, path.lstrip("/"))) if path else GH_BASE
    url_obj = urllib2.urlopen(url_path)
    return json.loads(url_obj.read())


@task
def downloads():
    """Verify GitHub downloads."""
    dl_list = gh_op("repos/%s/%s/downloads" % (GH_USER, GH_REPO))
    
    print("Downloads")
    for dl_dict in dl_list:
        print("%(created_at)s: %(name)s" % dl_dict)
