Linting
=======

.. index:: lint

.. note::
    The config details for linting are included in ``setup.cfg.``

flake8
------

To run flake8: ::

    $ flake8


pylint
------

To run pylint: ::

    $ pylint <python files that you wish to lint>

The config for pylint is located in .pylintrc. It specifies:

* Use the pylint_django plugin. If using Celery, also use pylint_celery.
* Set max line length to 120 chars
* Disable linting messages for missing docstring and invalid name
* max-parents=13

pycodestyle
-----------

This is included in flake8's checks, but you can also run it separately to see a more detailed report: ::

    $ pycodestyle <python files that you wish to lint>

The config for pycodestyle is located in setup.cfg. It specifies:

* Exclude ``.tox,.git,*/migrations/*,*/static/CACHE/*,docs,node_modules``
