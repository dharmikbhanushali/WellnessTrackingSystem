.. _testing:

Testing
========

.. index:: test, pytest, django testing, test coverage


Type checks
-----------

Running type checks with mypy. ::

    $ mypy <module_name>
    $ mypy wrike,tasks,user

Pytest
------

This project uses the Pytest_, a framework for easily building simple and scalable tests.
After you have set up to `develop locally`_, run the following commands to make sure the testing environment is ready: ::

    $ pytest

You will get a readout of the ``users`` app that has already been set up with tests. If you do not want to run the ``pytest`` on the entire project, you can target a particular app by typing in its location: ::

   $ pytest <path-to-app-in-project/app>

If you set up your project to `develop locally with docker`_, run the following command: ::

   $ docker-compose -f local.yml run --rm app pytest

Targeting particular apps for testing in ``docker`` follows a similar pattern as previously shown above.

Coverage
--------

You can run the ``pytest`` with code ``coverage`` by typing in the following command: ::

   $ docker-compose -f local.yml run --rm app coverage run -m pytest

Once the tests are complete, in order to see the code coverage, run the following command: ::

   $ docker-compose -f local.yml run --rm app coverage report

.. note::

   At the root of the project folder, you will find the ``pytest.ini`` file. You can use this to customize_ the ``pytest`` to your liking.

   There is also the ``.coveragerc``. This is the configuration file for the ``coverage`` tool. You can find out more about `configuring`_ ``coverage``.

.. seealso::

   For unit tests, run: ::

      $ python manage.py test

   Since this is a fresh install, and there are no tests built using the Python `unittest`_ library yet, you should get feedback that says there were no tests carried out.

.. _Pytest: https://docs.pytest.org/en/latest/example/simple.html
.. _develop locally: ./developing-locally.html
.. _develop locally with docker: ./developing-locally-docker.html
.. _customize: https://docs.pytest.org/en/latest/customize.html
.. _unittest: https://docs.python.org/3/library/unittest.html#module-unittest
.. _configuring: https://coverage.readthedocs.io/en/v4.5.x/config.html
