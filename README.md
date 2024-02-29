## Create Python virtual environment and install `pytest-xdist` in it.

A dependency of `pytest-xdist` is `pytest`, so this also installs `pytest`.

```
pipenv --python=3.11.2 install pytest-xdist
```

## Run tests.

To run tests, execute the following command in the same directory as this
`README.md` file.
```
pipenv run pytest --color=yes -f .
```
