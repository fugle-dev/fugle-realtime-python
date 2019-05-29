# Contributing & Publishing

## Contributing

Git clone the repository:

```sh
git clone https://github.com/fortuna-intelligence/fugle-realtime-py.git
cd fugle-realtime-py
```

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

## Publishing

### [PyPI](https://pypi.org/): [`fugle-realtime`](https://pypi.org/project/fugle-realtime/)

Set credentials of [PyPI](https://pypi.org/) with [`poetry`](https://poetry.eustace.io/) if not yet been set:

```sh
poetry config http-basic.pypi username password
```

Then bump the version in `pyproject.toml` with valid [semver](https://semver.org/) bump rule:

```sh
poetry version [patch|minor|major|prepatch|preminor|premajor|prerelease]
```

Finally build and publish the package to [PyPI](https://pypi.org/):

```sh
poetry build
poetry publish
```
