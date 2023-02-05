Getting Up and Running Locally
==============================

.. index:: pip, virtualenv, PostgreSQL


Setting Up Development Environment
----------------------------------

Make sure to have the following on your host:

* Python 3.9
* PostgreSQL_.

.. note::

    All the environment variables used in DJANGO environment configuration are documented in :ref:`settings`

.. seealso::

   Check out the :ref:`environ` page for a miscellaneous environments details.


First things first.

#. Create a virtualenv: ::

    $ python3.9 -m venv <virtual env path>

#. Activate the virtualenv you have just created: ::

    $ source <virtual env path>/bin/activate

#. Install development requirements: ::

    $ pip install -r requirements/local.txt
    $ git init # A git repo is required for pre-commit to install
    $ pre-commit install

   .. note::

       the `pre-commit` hook exists in the generated project as default.
       For the details of `pre-commit`, follow the `pre-commit`_ site.

#. Create a new PostgreSQL database using createdb_: ::

    $ createdb --username=postgres <db_name>

   .. note::

       if this is the first time a database is created on your machine you might need an
       `initial PostgreSQL set up`_ to allow local connections & set a password for
       the ``postgres`` user. The `postgres documentation`_ explains the syntax of the config file
       that you need to change.


#. Set the environment variables for your database(s): ::

    $ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>

   .. note::

       Check out the :ref:`environ` page for a comprehensive list of the environments variables.

   .. seealso::

       To help setting up your environment variables, you have a few options:

       * create an ``.env`` file in the root of your project and define all the variables you need in it.
       * Use a local environment manager like `direnv`_

#. Apply migrations: ::

    $ python manage.py migrate

#. If you're running synchronously, see the application being served through Django development server: ::

    $ python manage.py runserver 0.0.0.0:8000

or if you're running asynchronously: ::

    $ uvicorn config.asgi:application --host 0.0.0.0 --reload

.. _PostgreSQL: https://www.postgresql.org/download/
.. _createdb: https://www.postgresql.org/docs/current/static/app-createdb.html
.. _initial PostgreSQL set up: https://web.archive.org/web/20190303010033/http://suite.opengeo.org/docs/latest/dataadmin/pgGettingStarted/firstconnect.html
.. _postgres documentation: https://www.postgresql.org/docs/current/static/auth-pg-hba-conf.html
.. _pre-commit: https://pre-commit.com/
.. _direnv: https://direnv.net/


Setup Email Backend
-------------------

.. _mailhog_details:

MailHog
~~~~~~~


MailHog is used to receive emails during development, it is written in Go and has no external dependencies.

#. `Download the latest MailHog release`_ for your OS.

#. Rename the build to ``MailHog``.

#. Copy the file to the project root.

#. Make it executable: ::

    $ chmod +x MailHog

#. Spin up another terminal window and start it there: ::

    ./MailHog

#. Check out `<http://127.0.0.1:8025/>`_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

.. _`Download the latest MailHog release`: https://github.com/mailhog/MailHog
