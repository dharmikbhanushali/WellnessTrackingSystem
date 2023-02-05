.. _environ:

Environment
===========

.. index:: Environment

.. seealso::

    ``./base/envs-example/readme.md``: for guide to create environment files.


Github Actions
~~~~~~~~~~~~~~

.. note::

    Create necessary `GitHub secrets`_  and tokens_  as referenced in ``yml`` files.

- Update ``./github`` for various github actions.
    - ``/workflows/``:
        - ``checks.yml``:  to modify testing, linting as per need etc.
        - ``ci.yml`` for ci related tasks.
        - ``pre-commit-autoupdate.yml`` for auto updating pre-commit hooks with PR request support.
    - ``dependabot.yml`` for setting `GitHub dependabot`_.


Miscellaneous
-------------

- ``.editorconfig``:  helps to maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. `editorconfig`_
- ``.gitattributes``: See details here. `git-attributes`_
- ``.pre-commit-search-and-replace.yaml``: See details here. `search_and_replace`_
- ``.pre-commit-config.yaml``: Defines all hooks used as part of pre-commit. See details here. `pre-commit-hooks`_


.. _GitHub dependabot: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
.. _GitHub secrets: https://docs.github.com/en/actions/security-guides/encrypted-secrets
.. _tokens: https://docs.github.com/en/actions/security-guides/automatic-token-authentication
.. _editorconfig: http://editorconfig.org
.. _git-attributes: https://www.git-scm.com/docs/gitattributes
.. _search_and_replace: https://github.com/mattlqx/pre-commit-search-and-replace
.. _pre-commit-hooks: https://pre-commit.com/hooks.html
