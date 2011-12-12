"""Fabric file."""

import os
import json
import urllib
import urllib2

from fabric.api import local, lcd, abort
from fabric.decorators import task


class Request(urllib2.Request):
    """Request with method support."""

    def __init__(self, *args, **kwargs):
        """Initializer."""
        self._method = kwargs.pop('method', "GET")
        urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        """Method."""
        return self._method


class GitHub(object):
    """GitHub API wrapper."""

    def __init__(self):
        """Initializer."""
        self.user = self.config("user")
        self.token = self.config("token")
        self.repo = "sphinx-bootstrap-theme"
        self.api_base = "https://api.github.com"

    @classmethod
    def config(cls, key):
        """Get a .gitconfig GH value."""
        val = local("git config github.%s" % key, capture=True).strip()
        return val if val else None

    def api_op(self, path, method="GET"):
        """Perform a GitHub API request and decode to JSON."""
        url_path = "/".join((self.api_base, path.lstrip("/"))) \
            if path else self.api_base
        data = urllib.urlencode({
            'login': self.user,
            'token': self.token,
        })

        req = Request(url_path, method=method, data=data)
        print(req.get_full_url())
        print(req.get_data())

        results = urllib2.urlopen(req).read()
        return json.loads(results) if results else {}

    def downloads(self):
        """Retrieve current GitHub downloads."""
        return self.api_op("repos/%s/%s/downloads" % (self.user, self.repo))

    def dl_delete(self, dl_obj):
        """Delete a download file."""
        return self.api_op(
            "repos/%s/%s/downloads/%s" % (self.user, self.repo, dl_obj['id']),
            method="DELETE",
        )


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


@task
def downloads():
    """Verify GitHub downloads."""
    print("Downloads:")
    for download in GitHub().downloads():
        print("%(created_at)s: %(name)s (%(id)s)" % download)


# @task
# def upload():
#     """Upload new zip files."""
#     git_hash = local("git rev-parse HEAD", capture=True).strip()
#     base_zip = "bootstrap.zip"
#     hash_zip = "bootstrap-%s.zip" % git_hash
# 
#     if not (os.path.exists(base_zip) and os.path.exists(hash_zip)):
#         abort("Did not find current zip files. Please create.")
# 
#     # Check if existing downloads
#     github = GitHub()
#     dl_dict = dict((x['name'], x) for x in github.downloads())
#     dl_hash = dl_dict.get(hash_zip)
#     dl_base = dl_dict.get(base_zip)
# 
#     if dl_hash is not None:
#         print("Found hashed zip file already. Skipping")
#         return
# 
#     if dl_base is not None:
#         print("Removing current base zip file.")
#         result = github.dl_delete(dl_base)
#         print("Result: %s" % json.dumps(result, indent=2))
