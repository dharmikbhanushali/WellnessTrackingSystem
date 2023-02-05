.. Trouble shooting readme.

Troubleshooting
=====================================

This page contains some advice about errors and problems commonly encountered during the development.

Docker:
-------

To fix unknown docker related issues, you can either:

- Clear your project-related Docker cache with ``docker-compose -f local.yml down --volumes --rmi all``.
- Use the Docker volume sub-commands to find volumes (`ls`_) and remove them (`rm`_).
- Use the `prune`_ command to clear system-wide (use with care!).

.. _ls: https://docs.docker.com/engine/reference/commandline/volume_ls/
.. _rm: https://docs.docker.com/engine/reference/commandline/volume_rm/
.. _prune: https://docs.docker.com/v17.09/engine/reference/commandline/system_prune/

Others
------

- Unable to handle the callback step in oauth2 workflow when developing locally.

.. note::

    - The callback uri points to ``http://localhost``.
        - ``${application_host}`` in ``base\.envs\local\.wrike``

.. attention::

  While local development after step 1. ``Authorization``, change the localhost in browser window to ``<<host>>/<<endpoint>>/callback?code=`` and code obtained in step 1. This allows redirection to localhost on specific port and endpoint.

.. attention::

    The wrike api doesn't allow modifying the ``callback_url`` from ``http://localhost`` to something like

    - ``http://localhost:8000`` or ``http://127.0.0.1:8000``
