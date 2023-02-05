.. _documentation:

Documentation
=============

This project uses Sphinx_ documentation generator.

.. seealso::

    - Getting started tutorial_ and `first steps`_
    - Various `Themes`_ and Current Theme customization_

After you have set up to `develop locally`_, run the following command from the project directory to build and serve HTML documentation.

- From ``docs`` directory. ::

    $ make livehtml
    $ # or
    $ sphinx-autobuild -b html --open-browser --port 9000 --watch ..\base -c .\source source build/html

- From root directory ``base``.

    - Static Build.: ::

        $ sphinx-build -b html docs/source/ docs/build/html


If you set up your project to `develop locally with docker`_, run the following command: ::

    $ docker-compose -f local.yml up docs

Navigate to port 9000 on your host to see the documentation. This will be opened automatically at `localhost`_ for local, non-docker development.

.. note::

    Make sure to change ``--open-browser`` to ``--host 0.0.0.0`` in ``base/docs/Makefile``


Note: using Docker for documentation sets up a temporary SQLite file by setting the environment variable ``DATABASE_URL=sqlite:///readthedocs.db`` in ``docs/conf.py`` to avoid a dependency on PostgreSQL.

Generate API documentation
----------------------------

Edit the ``docs`` files and project application docstrings to create your documentation.

The sphinx extension `apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html/>`_ is used to automatically document code using signatures and docstrings.

Numpy or Google style docstrings will be picked up from project files and available for documentation. See the `Napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_ extension for details.

To compile all docstrings automatically into documentation source files, use the command:  ::

    $ make apidocs

or  ::

    $ sphinx-apidoc --force --module-first -o base/docs/source/ base/<module_name>

.. note::

    Make sure the ``<module_name>`` is included in ``modules.rst`` and ``modules`` is listed in ``toctree`` of ``index.rst``

.. seealso::

    `Sphinx apidoc documentation`_ for more details and `Napoleon`_, `Example Google Style Python Docstrings`_ and `config`_.

Setting up ReadTheDocs
----------------------

To setup your documentation on `ReadTheDocs`_, you must

1. Go to `ReadTheDocs`_ and login/create an account
2. Add your GitHub repository
3. Trigger a build

Additionally, you can auto-build Pull Request previews, but `you must enable it`_.

.. _localhost: http://localhost:9000/
.. _Sphinx: https://www.sphinx-doc.org/en/master/index.html
.. _develop locally: ./developing-locally.html
.. _develop locally with docker: ./developing-locally-docker.html
.. _ReadTheDocs: https://readthedocs.org/
.. _you must enable it: https://docs.readthedocs.io/en/latest/guides/autobuild-docs-for-pull-requests.html#autobuild-documentation-for-pull-requests
.. _tutorial: https://www.sphinx-doc.org/en/master/tutorial/getting-started.html
.. _first steps: https://www.sphinx-doc.org/en/master/tutorial/first-steps.html
.. _customization: https://pradyunsg.me/furo/customisation
.. _Themes: https://sphinx-themes.org/
.. _Example Google Style Python Docstrings: https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/
.. _config: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config
.. _Sphinx apidoc documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
