.. _settings:

=============
DJANGO Config
=============

.. index:: settings

.. seealso::

    Check out the :ref:`environ` page for a miscellaneous environments details.

This project relies extensively on environment settings which **will not work with Apache/mod_wsgi setups**.

.. note::

    - Common django related environment variables in: ``settings.base``
    - Development related environment variables in: ``settings.local``
    - Production related environment variables in: ``settings.production``

For configuration purposes, the following table maps Django setting to development  and production settings:

=========================== ============================================== ======================================================================
Django Setting              Development Default                            Production Default
=========================== ============================================== ======================================================================
DATABASES                   auto w/ Docker; postgres://base w/o            raises error
ADMIN_URL                   'admin/'                                       raises error
DEBUG                       True                                           False
SECRET_KEY                  auto-generated                                 raises error
SECURE_BROWSER_XSS_FILTER   n/a                                            True
SECURE_SSL_REDIRECT         False                                          True
SECURE_CONTENT_TYPE_NOSNIFF n/a                                            True
SECURE_FRAME_DENY           n/a                                            True
HSTS_INCLUDE_SUBDOMAINS     n/a                                            True
SESSION_COOKIE_HTTPONLY     n/a                                            True
SESSION_COOKIE_SECURE       False                                          False
DEFAULT_FROM_EMAIL          n/a                                            "your_project_name <noreply@your_domain_name>"
SERVER_EMAIL                n/a                                            "your_project_name <noreply@your_domain_name>"
EMAIL_SUBJECT_PREFIX        n/a                                            "[your_project_name] "
ALLOWED_HOSTS               ["localhost", "0.0.0.0", "127.0.0.1"]          ['your_domain_name']
=========================== ============================================== ======================================================================

The following table lists settings and their defaults for third-party applications, which may or may not be part of your project:

======================================= =========================== ============================================== ======================================================================
Environment Variable                    Django Setting              Development Default                            Production Default
======================================= =========================== ============================================== ======================================================================
SENDGRID_API_KEY                        SENDGRID_API_KEY            n/a                                            raises error
SENDGRID_GENERATE_MESSAGE_ID            True                        n/a                                            raises error
SENDGRID_MERGE_FIELD_FORMAT             None                        n/a                                            raises error
SENDGRID_API_URL                        n/a                         n/a                                            "https://api.sendgrid.com/v3/"
======================================= =========================== ============================================== ======================================================================

.. seealso::

    `Django settings page`_

.. _wrike_api_related:

-----------------
WRIKE_API Related
-----------------

+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment Variable             | Default Value                                                                                                              | Description                                                                                                                                               |
+==================================+============================================================================================================================+===========================================================================================================================================================+
| ``client_id``                    | N/A                                                                                                                        | Client ID: `App Console`_                                                                                                                                 |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``client_secret``                | N/A                                                                                                                        | Client Secret: `App Console`_                                                                                                                             |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``host``                         | ``https://www.wrike.com``                                                                                                  | Wrike Api Host                                                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``authorization_base_url``       | ``https://login.wrike.com/oauth2/authorize/v4``                                                                            | API Access url                                                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``token_url``                    | ``https://login.wrike.com/oauth2/token``                                                                                   | Exchanging authorization code for access token                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``refresh_url``                  | ``https://login.wrike.com/oauth2/token``                                                                                   | Refreshing access token                                                                                                                                   |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``redirect_uri``                 | ``http://localhost``                                                                                                       | URI where the response will be redirected. We assume that you have a working web server with a public address that can correctly handle Wrike requests.   |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``profile_url``                  | ``https://www.wrike.com/api/v4/contacts?me=true``                                                                          | `Wrike Contacts`_                                                                                                                                         |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``all_tasks``                    | ``https://www.wrike.com/api/v4/tasks``                                                                                     | `Wrike Tasks`_                                                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``projects_url``                 | ``https://www.wrike.com/api/v4/spaces/{spaceId}/folders?project=True&fields=["customFields"]``                             | `Project Folder Tree`_                                                                                                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``task_url``                     | ``https://www.wrike.com/api/v4/folders/{folderId}/tasks?sortField=UpdatedDate&sortOrder=Desc``                             | `Query Tasks`_                                                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``permanent_token``              | N/A                                                                                                                        | `Obtaining a permanent token`_                                                                                                                            |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``space_id``                     | N/A                                                                                                                        | Space ID                                                                                                                                                  |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``workflow_url``                 | ``https://www.wrike.com/api/v4/workflows``                                                                                 | `Query Workflows`_                                                                                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``custom_field_url``             | ``https://www.wrike.com/api/v4/customfields``                                                                              | `Query Custom Fields`_                                                                                                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso::

    - `Wrike api documentation`_, `Overview`_, `Oauth2 Workflow`_ and `Get Tasks Details`_

--------------------------
Other Environment Settings
--------------------------

+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| Environment Variable                     | Default Value                     | Description                                                                                |
+==========================================+===================================+============================================================================================+
| ``PROJECT_EXPIRES_IN``                   | 1440                              | Time in minutes when application should refresh the ``Project`` data from the wrike api.   |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``TASKS_EXPIRES_IN``                     | 1440                              | Time in minutes when application should refresh the ``Tasks`` data from the wrike api.     |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``APPS_TO_EXCLUDE_FROM_MIDDLEWARE``      | ``wrike``                         | Short circuiting middleware for handling exceptions                                        |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``OAUTHLIB_INSECURE_TRANSPORT``          | ``1``                             | Bypass ``Oauthlib``'s ``InsecureTransportError``, when accessing over http                 |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``DJANGO_SUPERUSER_EMAIL``               | ``kkarandikar@bmiaudit.com``      | Default Django admin  super user email.                                                    |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``DJANGO_SUPERUSER_USERNAME``            | ``Kiran Karandikar``              | Default Django admin super user name.                                                      |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+
| ``DJANGO_SUPERUSER_PASSWORD``            | ``admin-user``                    | Default Django admin super user password.                                                  |
+------------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------+

.. note::

    The system will auto create django admin super user with details ``DJANGO_SUPERUSER_*`` on first load. For additional details please `login to admin`_ portal.

.. warning::

    When writing middleware to handle exceptions, django follows specific flow. Thus required configuration for ``APPS_TO_EXCLUDE_FROM_MIDDLEWARE``
    see also: `Django Middleware`_ and `process exception`_


.. _Django Middleware: https://docs.djangoproject.com/en/4.0/topics/http/middleware
.. _process exception: https://docs.djangoproject.com/en/4.0/topics/http/middleware/#process-exception
.. _Wrike api documentation: https://developers.wrike.com/
.. _Overview: https://developers.wrike.com/overview/
.. _Oauth2 Workflow: https://developers.wrike.com/oauth-20-authorization/
.. _Get Tasks Details: https://developers.wrike.com/api/v4/tasks/
.. _App Console: https://www.wrike.com/frontend/apps/index.html#/api
.. _Wrike Contacts: https://developers.wrike.com/api/v4/contacts/
.. _Wrike Tasks: https://developers.wrike.com/api/v4/tasks/
.. _Query Tasks: https://developers.wrike.com/api/v4/tasks/
.. _Query Workflows: https://developers.wrike.com/api/v4/workflows/
.. _Query Custom Fields: https://developers.wrike.com/api/v4/custom-fields/#query-custom-fields
.. _Project Folder Tree: https://developers.wrike.com/api/v4/folders-projects/
.. _Obtaining a permanent token: https://developers.wrike.com/oauth-20-authorization/
.. _login to admin: http://localhost:8000/admin
.. _Django settings page: https://docs.djangoproject.com/en/3.2/ref/settings
