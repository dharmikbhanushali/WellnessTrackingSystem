# Example for `.envs`

---

> Steps to recreate the environment files.

- create `.env` under root directory.
  - Under `.env` create directories `.local` and `.production` for local and
    production environment respectively.
- Copy `.django`, `.postgres` and `.wrike` files to respective environment.
- Make necessary changes in the environment files.

> `Environment files are passed as configuration in docker-compose file.`
