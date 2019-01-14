"""Sphinx bootstrap theme."""
import os

VERSION = (0, 6, 5)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]


def add_js(app):
    bootstrap_version = \
        app.builder.config.html_theme_options.get('bootstrap_version', '3')
    add_js_file = getattr(app, 'add_js_file', app.add_javascript)
    add_js_file('searchtools.js')
    add_js_file('js/jquery-1.11.0.min.js')
    add_js_file('js/jquery-fix.js')
    add_js_file('bootstrap-%s/js/bootstrap.min.js' % (bootstrap_version,))
    add_js_file('bootstrap-%s/js/bootstrap-sphinx.js' % (bootstrap_version,))


def setup(app):
    """Setup."""
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = get_html_theme_path()[0]
        app.add_html_theme('bootstrap', os.path.join(theme_path, 'bootstrap'))
    app.connect('builder-inited', add_js)
