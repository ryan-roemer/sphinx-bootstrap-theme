"""Fabric file."""

import base64
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
        self.password = self.config("password")
        self.token = self.config("token")
        self.repo = "sphinx-bootstrap-theme"
        self.api_base = "https://api.github.com"

    @classmethod
    def _add_headers(cls, req, headers=None):
        """Format headers."""
        if headers:
            if isinstance(headers, dict):
                headers = headers.iteritems()

            for key, val in headers:
                req.add_header(key, val)

    @classmethod
    def config(cls, key):
        """Get a .gitconfig GH value."""
        val = local("git config github.%s" % key, capture=True).strip()
        return val if val else None

    def api_op(self, path, method="GET", headers=None, data=None):
        """Perform a GitHub API request and decode to JSON."""
        # Params: URL, data, auth string.
        url_path = self.api_base
        if path:
            url_path = "/".join((self.api_base, path.lstrip("/")))
        auth_str = base64.encodestring(
            "%s:%s" % (self.user, self.password))[:-1]

        req = Request(url_path, method=method, data=data)
        self._add_headers(req, headers)
        req.add_header("Authorization", "Basic %s" % auth_str)

        results = urllib2.urlopen(req).read()
        return json.loads(results) if results else {}

    def s3_op(self, path, file_name, method="POST", headers=None, data=None):
        """Perform S3 upload operation."""
        req = Request(path, method=method, data=data)
        self._add_headers(req, headers)

        return urllib2.urlopen(req)

    def downloads(self):
        """Retrieve current GitHub downloads."""
        return self.api_op("repos/%s/%s/downloads" % (self.user, self.repo))

    def downloads_del(self, dl_obj):
        """Delete a download file."""
        return self.api_op(
            "repos/%s/%s/downloads/%s" % (self.user, self.repo, dl_obj['id']),
            method="DELETE",
        )

    def downloads_put(self, file_name, git_hash, desc=None):
        """Upload a download file."""

        if not desc:
            desc = "Pre-packaged sphinx theme for %s." % git_hash

        # Part 1: Create the resource)
        put_dict = self.api_op(
            "repos/%s/%s/downloads" % (self.user, self.repo),
            method="POST",
            headers={
                'Content-Type': "application/json",
            },
            data=json.dumps({
                "name": file_name,
                "size": os.path.getsize(file_name),
                "description": "Latest release",
                #"content_type": "text/plain" (Optional)
            }),
        )

        # Part 2: Upload file to s3
        results = self.s3_op(
            "https://github.s3.amazonaws.com/",
            file_name,
            method="POST",
            headers=[
                ('key', put_dict['path']),
                ('acl', put_dict['acl']),
                ('success_action_status', 201),
                ('Filename', put_dict['name']),
                ('AWSAccessKeyId', put_dict['accesskeyid']),
                ('Policy', put_dict['policy']),
                ('Signature', put_dict['signature']),
                ('Content-Type', put_dict['mime_type']),
            ],
        )

        print(dir(results))
        print(results)
        return {"TODO": "TODO"}


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


@task
def upload():
    """Upload new zip files."""
    git_hash = local("git rev-parse HEAD", capture=True).strip()
    base_zip = "bootstrap.zip"
    hash_zip = "bootstrap-%s.zip" % git_hash

    if not (os.path.exists(base_zip) and os.path.exists(hash_zip)):
        abort("Did not find current zip files. Please create.")

    # Check if existing downloads
    github = GitHub()
    dl_dict = dict((x['name'], x) for x in github.downloads())
    dl_hash = dl_dict.get(hash_zip)
    dl_base = dl_dict.get(base_zip)

    if dl_hash is not None:
        print("Found hashed zip file already. Skipping")
        return

    # if dl_base is not None:
    #     print("Removing current base zip file.")
    #     result = github.downloads_del(dl_base)
    #     print("Result: %s" % json.dumps(result, indent=2))
    #
    # print("Upload new base zip file.")
    # result = github.downloads_put(dl_base)
    # print("Result: %s" % json.dumps(result, indent=2))

    print("Upload new hashed zip file.")
    result = github.downloads_put(hash_zip, git_hash)
    print("Result: %s" % json.dumps(result, indent=2))
