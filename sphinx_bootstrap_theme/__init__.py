"""Sphinx bootstrap theme."""
import os

VERSION = (0, 8, 0)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__

# NOTE: SPHINX_BOOTSTRAP_THEME_DEV_VERSION environment variable is for internal
# usage only.  It is used to create a dev release to deploy to TestPyPI, see
# .github/workflows/package.yaml for more information.
dev = os.getenv("SPHINX_BOOTSTRAP_THEME_DEV_VERSION", None)
if dev:
    __version__ += ".dev" + dev
    __version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]


def setup(app):
    """Setup."""
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = get_html_theme_path()[0]
        app.add_html_theme('bootstrap', os.path.join(theme_path, 'bootstrap'))
