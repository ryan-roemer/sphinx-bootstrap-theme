Maintenance
===========

Testing Suite
-------------

The ``sphinx-bootstrap-theme`` is developed using tox_.  When contributing
changes, you can run the checks locally:

.. _tox: https://tox.readthedocs.io/en/latest/

.. code-block:: bash

    # Install `tox` if you do not have it already, replace
    # `pip` with your python package manager of choice.
    $ pip install tox

    # Go to this repository's directory
    $ cd /path/to/sphinx-bootstrap-theme

    # Run the default tests (py and lint).
    $ tox

A given check can be run explicitly provided that you supply the "environment
list" to ``tox``.  For example, ``tox -e py`` runs the ``py`` environment.  You
can run multiple using a comma separated list, e.g., ``tox -e py,lint``.  The
available environments are as follows:

.. cssclass:: table-striped table-bordered

+---------------+--------------------------------------------------------------+
| Test Name     | Behavior                                                     |
+===============+==============================================================+
| ``py``        | Run the python tests.  This is the ``[testenv]`` section of  |
|               | ``tox.ini``.                                                 |
|               |                                                              |
|               | .. note:: No python tests are currently implemented!         |
+---------------+--------------------------------------------------------------+
| ``docs``      | Build the ``demo`` site documentation.  The resultant        |
|               | documentation will be placed in                              |
|               | ``{tox_workdir}/docs/tmp/html/``.  Unless explicitly changed |
|               | with ``--workdir`` argument to ``tox``, this will be the     |
|               | ``.tox`` directory created next to ``tox.ini``.              |
+---------------+--------------------------------------------------------------+
| ``linkcheck`` | Builds the ``demo`` site documentation and validates         |
|               | internal and external links all point to somewhere.          |
+---------------+--------------------------------------------------------------+
| ``server``    | Builds the ``demo`` site documentation using a local server. |
|               | The server re-generates whenever changes are made, which can |
|               | be convenient for iterative development.  By default the     |
|               | port is ``8000``, if that port is in use supply the desired  |
|               | port to use.  Example: ``tox -e server -- -p 8080``.  Notice |
|               | the ``--`` before ``-p 8080``.  That is required, ``--``     |
|               | tells ``tox`` that everything after the dashes should be     |
|               | ignored.  In this case, the arguments after ``--`` are       |
|               | forwarded to sphinx-autobuild_.                              |
+---------------+--------------------------------------------------------------+
| ``lint``      | Run any linting checks associated with the project.          |
+---------------+--------------------------------------------------------------+
| ``dist``      | Build the python source and wheel distributions in           |
|               | preparation for upload.  Produces a top-level ``build/`` and |
|               | ``dist/`` directory as a result.                             |
|               |                                                              |
|               | Manual uploads can be done using ``twine upload dist/*``.    |
+---------------+--------------------------------------------------------------+
| ``clean``     | Helper target to delete miscellaneous files that may be      |
|               | created as a result of development.  For example, removes    |
|               | the ``build/`` and ``dist/`` directories that would be       |
|               | created by ``tox -e dist``.                                  |
+---------------+--------------------------------------------------------------+

.. _sphinx-autobuild: https://github.com/GaretJax/sphinx-autobuild

Versioning and Packaging
------------------------

The Sphinx Bootstrap Theme uses semantic versioning.  The ``__version__``
attribute defined in ``__init__.py`` is the current version of the theme.  We
use the versioning tactics `described here`__, example scenario:

1. Current version on ``master`` is ``0.8.0.dev``, it is time to release.
2. A commit sets the version to be ``0.8.0``, a pull request is opened to run
   the test suite one last time.  The PR is (rebase-)merged.
3. The merged commit is tagged as ``v0.8.0`` and the tag is pushed.  This will
   trigger the CI to deploy to PyPI.
4. After deployment, a new commit sets the version to be ``0.8.1.dev``.

__ https://snarky.ca/how-i-manage-package-version-numbers/
