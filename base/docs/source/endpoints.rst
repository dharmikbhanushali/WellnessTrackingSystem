.. _endpoints:

.. index:: End points, api

=========
Endpoints
=========

.. note::

    On initial run the database get auto populated for:

    -  ``CustomFields`` database for default ``space_id`` :ref:`wrike_api_related`.
    -  ``Project`` database for default ``space_id`` :ref:`wrike_api_related`.
    -  ``Tasks`` database for default ``space_id``  :ref:`wrike_api_related`.

    .. todo::

        Use `Celery`_ to initialize the database asynchronously on startup.


============================= ================================== =======================================================
Endpoint                      Details                            Additional Details.
============================= ================================== =======================================================
``api/docs``                  Interactive Swagger Api            Alternatively ``api/rdocs``
``api/user/``                 User Management and Auth Tokens    N/A
``api/wrike/``                Wrike oauth2 workflow              Per user basis access to protected resource.
``api/pt``                    Audit and tasks details            Access the Wrike API using a permanent access token.
``http://localhost:9000/``    Sphinx Documentation server.       :ref:`documentation`
``http://localhost:8025/``    Mail-hog server                     :ref:`mailhog_details_docker`, :ref:`mailhog_details`
``api/sample``                Sample Endpoints                   Used for development and testing purpose.
============================= ================================== =======================================================


Workflow
========

1. ``User Registration and Authentication``
    - Create new user using ``api/usercreate``, fill out necessary details
    - Validate the details and obtain Auth token using ``api/usertoken``

        .. important::

            Make sure to include this token in all future requests, otherwise error:``Authentication details are not provided.``

    - Submit the request to admin user for elevated access using ``api/userupgrade``

        .. note::

            This will send request to ``admin`` user. Until the admin user's approval, the user will not have access to protected resources.


        .. important::

            After ``admin`` user's approval.
            The current user will be marked as ``staff`` user and will have permanent access to protected resources.

2. Access ``api/pt`` endpoints.

    .. important::

        This endpoint will be accessible to all ``staff and admin users``.


    .. note::

        Make sure to include the ``Auth token`` in request.

3. Optionally, access ``api/wrike``.
    - This endpoint is experimental, it's proxy for per user access to protected resources workflow.

.. _Celery: https://docs.celeryq.dev/en/stable/index.html
