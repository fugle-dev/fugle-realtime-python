# fugle-realtime-py

## Contributing

Install [`poetry`](https://poetry.eustace.io/) if not yet installed:

```sh
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Then install dependencies and setup [`pre-commit`](https://pre-commit.com/):

```sh
poetry install

poetry run pre-commit install
```

Code formatting using [`black`](https://black.readthedocs.io/en/stable/):

```sh
poetry run black .
```

Testing using [`pytest`](https://pytest.org):

```sh
poetry run pytest
```
