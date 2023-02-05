.. _deployment:

Deployment with Docker
======================

.. index:: deployment, docker, docker-compose, compose


Prerequisites
-------------

* Docker 17.05+.
* Docker Compose 1.17+


Understanding the Docker Compose Setup
--------------------------------------

Before you begin, check out the ``production.yml`` file in the root of this project. Keep note of how it provides configuration for the following services:

* ``django``: your application running behind ``Gunicorn``;
* ``postgres``: PostgreSQL database with the application's relational data;
* ``traefik``: Traefik reverse proxy with HTTPS on by default.
* ``celeryworker`` running a Celery worker process;
* ``celerybeat`` running a Celery beat process;
* ``flower`` running Flower_.

The ``flower`` service is served by Traefik over HTTPS, through the port ``5555``.

.. _`Flower`: https://github.com/mher/flower


Configuring the Stack
---------------------

The majority of services above are configured through the use of environment variables. Just check out :ref:`settings` and you will know the drill.

To obtain logs and information about crashes in a production setup, make sure that you have access to an external Sentry instance (e.g. by creating an account with `sentry.io`_), and set the ``SENTRY_DSN`` variable. Logs of level ``logging.ERROR`` are sent as Sentry events. Therefore, in order to send a Sentry event use:

.. code-block:: python

    import logging
    logging.error("This event is sent to Sentry", extra={"<example_key>": "<example_value>"})

The ``extra`` parameter allows you to send additional information about the context of this error.


You will probably also need to setup the Mail backend, for example by adding a `Sendgrid api keys`_ and a `Sendgrid`_ sender domain, otherwise, the account creation view will crash and result in a 500 error when the backend attempts to send an email to the account owner.

.. seealso::

    SendGrid-python_ to quickly and easily use the SendGrid Web API v3 via Python.

.. _sentry.io: https://sentry.io/welcome
.. _Sendgrid: https://sendgrid.com/
.. _Sendgrid api keys: https://app.sendgrid.com/settings/api_keys
.. _SendGrid-python: https://github.com/sendgrid/sendgrid-python/


HTTPS is On by Default
----------------------

SSL (Secure Sockets Layer) is a standard security technology for establishing an encrypted link between a server and a client, typically in this case, a web server (website) and a browser. Not having HTTPS means that malicious network users can sniff authentication credentials between your website and end users' browser.

* If you are not using a subdomain of the domain name set in the project, then remember to put your staging/production IP address in the ``ALLOWED_HOSTS`` environment variable (see :ref:`settings`) before you deploy your website. Failure to do this will mean you will not have access to your website through the HTTP protocol.

* Access to the Django admin is set up by default to require HTTPS in production or once *live*.

The Traefik reverse proxy used in the default configuration will get you a valid certificate from Lets Encrypt and update it automatically. All you need to do to enable this is to make sure that your DNS records are pointing to the server Traefik runs on.

You can read more about this feature and how to configure it, at `Automatic HTTPS`_ in the Traefik docs.

.. _Automatic HTTPS: https://docs.traefik.io/https/acme/


(Optional) Postgres Data Volume Modifications
---------------------------------------------

Postgres is saving its database files to the ``production_postgres_data`` volume by default. Change that if you want something else and make sure to make backups since this is not done automatically.


Building & Running Production Stack
-----------------------------------

You will need to build the stack first. To do that, run::

    docker-compose -f production.yml build

Once this is ready, you can run it with::

    docker-compose -f production.yml up

To run the stack and detach the containers, run::

    docker-compose -f production.yml up -d

To run a migration, open up a second terminal and run::

   docker-compose -f production.yml run --rm app python manage.py migrate

To create a superuser, run::

   docker-compose -f production.yml run --rm app python manage.py createsuperuser

If you need a shell, run::

   docker-compose -f production.yml run --rm app python manage.py shell

To check the logs out, run::

   docker-compose -f production.yml logs

If you want to scale your application, run::

   docker-compose -f production.yml up --scale app=4
   docker-compose -f production.yml up --scale celeryworker=2

.. warning:: don't try to scale ``postgres``, ``celerybeat``, or ``traefik``.

To see how your containers are doing run::

    docker-compose -f production.yml ps
