"""Fabric file."""

import os
import json
import urllib2

from fabric.api import local, lcd, abort
from fabric.decorators import task


def gh_config(key):
    """Get a .gitconfig GH value."""
    val = local("git config github.%s" % key, capture=True).strip()
    return val if val else None


GH_USER = gh_config("user")
GH_TOKEN = gh_config("token")
GH_REPO = "sphinx-bootstrap-theme"
GH_BASE = "https://api.github.com"


class Request(urllib2.Request):
    """Requests with method support."""

    def __init__(self, *args, **kwargs):
        """Initializer."""
        self._method = kwargs.pop('method', "GET")
        urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        """Method."""
        return self._method


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


def gh_op(path, method="GET"):
    """Perform a GitHub API request and decode to JSON."""
    url_path = "/".join((GH_BASE, path.lstrip("/"))) if path else GH_BASE
    req = Request(url_path, method=method)
    url_obj = urllib2.urlopen(req)
    results = url_obj.read()
    return json.loads(results) if results else {}


def gh_downloads():
    """Retrieve current GitHub downloads."""
    return gh_op("repos/%s/%s/downloads" % (GH_USER, GH_REPO))


def gh_dl_delete(dl_obj):
    """Delete a download file."""
    return gh_op("repos/%s/%s/downloads/%s" % (GH_USER, GH_REPO, dl_obj['id']),
                 method="DELETE")


@task
def downloads():
    """Verify GitHub downloads."""
    print("Downloads:")
    for download in gh_downloads():
        print("%(created_at)s: %(name)s (%(id)s)" % download)


@task
def upload():
    """Upload new zip files."""
    git_hash = local("git rev-parse HEAD", capture=True).strip()
    base_zip = "bootstrap.zip"
    hash_zip = "bootstrap-%s.zip" % git_hash

    if not (os.path.exists(base_zip) and os.path.exists(hash_zip)):
        abort("Did not find current zip files. Please create.")

    # Check if existing downloads
    dl_dict = dict((x['name'], x) for x in gh_downloads())
    dl_hash = dl_dict.get(hash_zip)
    dl_base = dl_dict.get(base_zip)

    if dl_hash is not None:
        print("Found hashed zip file already. Skipping")
        return

    if dl_base is not None:
        print("Removing current base zip file.")
        result = gh_dl_delete(dl_base)
        print("Result: %s" % json.dumps(result, indent=2))




