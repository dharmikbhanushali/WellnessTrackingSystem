<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">repo_name</h3>
  <p align="center">
    project_description
    <br />
    <a href="https://kiran-karandikar.github.io/repo_name"><strong>Preview</strong></a>
    <br />
    <a href="https://github.com/kiran-karandikar/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kiran-karandikar/repo_name">View Demo</a>
    ·
    <a href="https://github.com/kiran-karandikar/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/kiran-karandikar/repo_name/issues">Request Feature</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Here's a blank template to get started: To avoid retyping too much info. Do a
search and replace with your text editor for the following: `repo_name`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This app uses the following Python packages

- [python-dotenv](https://pypi.org/project/python-dotenv/), to store sensitive
  information
- [requests-oauthlib](https://github.com/requests/requests-oauthlib), to
  integrate with third-party OAuth2 providers, such as Wrike.
- [requests](https://github.com/psf/requests), to send HTTP GET and POST
  requests
- [django-environ](https://django-environ.readthedocs.io/en/latest/), to manage
  django settings flawlessly
- [djangorestframework](https://www.django-rest-framework.org/) for **web
  browsable api**.
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for _Sane
  and
  flexible OpenAPI 3 schema generation for Django REST framework._
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) a
  configurable set of panels that display various debug information about the
  current request/response and when clicked, display more details about the
  panel's content.


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Optional:
    - [Dokcer](https://www.docker.com/get-started/)
      and [Docker dependencies](https://docs.docker.com/desktop/install/windows-install/)
      installed if using dokcer based setup.
    - Use [ruby installer](https://rubyinstaller.org/) if
      using [pre-commit hook](https://pre-commit.com/) : [Search and Replace](https://github.com/mattlqx/pre-commit-search-and-replace)

### Installation

1. Clone the repository
   ```sh
    $ git clone https://github.iu.edu/kikarand/Team-26-Wellness-Tracking-System
   ```
2. For local development, see the following:

   - [Developing locally using docker](./base/docs/source/developing-locally-docker.rst)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->

## Usage

- Setup docker containers using:

  ```shell
  docker build .
  docker compose -f local.yml build
  docker compose -f local.yml up
  docker compose -f local.yml down
  ```

_For more examples, please refer to
the [Documentation](https://localhost:9000/)_ built using `Sphinx`

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.iu.edu/kikarand/Team-26-Wellness-Tracking-System) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the `MIT License`. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>
