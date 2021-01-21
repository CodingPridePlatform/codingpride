# Installation

## Requirements

- Python 3.8+
- Pipenv
- Postgres Database

Create virtual environment in the root of the project and name it `.venv` using

```
py -m venv .venv
```

> Root of the project refers to the folder containing `manage.py` file.

This project use Postgres Database, make sure it's installed. If not yet, [download it](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

Create `.env` file, copy contents in `.env_sample` and paste in your `.env` file and modify accordingly.

Once Postgres is installed, create a database and fill credentials in `.env` file.

Install packages using

```
pipenv install --dev
```

Apply migrations using

```
python manage.py migrate
```
