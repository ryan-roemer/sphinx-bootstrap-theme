"""Sphinx bootstrap theme."""
import os

__version__ = "0.8.0"


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
