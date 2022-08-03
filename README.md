# SOAP-REST-DJANGO

Example of SOAP and REST app in django

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents

- [dev enviroments](#dev-env)
  - [virtualenv](#virtualenv)
    - [Install pre-installation dependencies](#install-pre-installation-dependencies)
    - [Setup postgreSQL (database)](#setup-postgresql-database)
      - [Create .env file](#create-env)
      - [Setup dev enviroment](#setup-dev-env)
      - [Setup de Database and start the project](#create-a-database-and-database-user-for-development)
      - [Create and activate virtual enviroment and install python dependencies](#create-a-virtual-enviroment)
    - [API documentation](#api-docs)
    - [Testing](#testing)
- [References](#references)

## Dev enviroments <a name="dev-env"></a>

### Virtual env <a name="virtualenv"></a>

This method is tested to work on linux, and is the most confortable for developing, because is faster in dev time, but need some pre working to start the enviroments

### Install pre-installation dependencies <a name="install-pre-installation-dependencies"></a>

- Python3
  Should come preinstalled with Ubuntu

- Pip3
  Installation on Ubuntu
  `sudo apt install python3-venv python3-pip`

### Setup postgreSQL (database) <a name="setup-postgresql-database"></a>

`sudo apt-get install libpq-dev postgresql-12`

### Create .env file <a name="create-env"></a>

Edit `.env.example` with your own settings and rename it `.env`

### Setup dev enviroment <a name="setup-dev-env"></a>

```bash
source ./scripts/start.sh
```

#### Create and activate virtual enviroment and install python dependencies <a name="create-a-virtual-enviroment"></a>

```bash
setup_venv
```

#### Setup de Database and start the project <a name="create-a-database-and-database-user-for-development"></a>

```bash
setup_db
```

#### Test the setup <a name="test-the-setup"></a>

Test the setup by running the development server

```bash
runserver
```

## References <a name="references"></a>

- [Steps followed to setup django with postgreSQL][postgres]
- [Directory structure explanation](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)

[postgres]: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
