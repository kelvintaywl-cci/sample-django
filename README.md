# Sample Django

The goal here is to setup a "usable" Django project to test features from CircleCI.
In particular, I am interested in testing [the Parallelism + Test Splitting feature](https://circleci.com/docs/2.0/parallelism-faster-jobs/).

This is a sample Django project that is essentially built following the official tutorial:
https://docs.djangoproject.com/en/4.0/intro/tutorial01/

In fact, this is arguably **an incomplete version**.
I have completed only up to [Part 2 of the tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial02/).

What this means is that:

1. There is a Postgres DB set up as a dependency
2. There are schema migrations to be run on setup
3. There are **some** models (and their relevant SQL tables).
4. There are tests BUT these tests are not testing anything around the models.

You can confirm that the tests are merely dummy tests.
See the files under the `polls/tests` folder.

```console
# list all tests files line by line
$ ls -1 */tests/*.py

polls/tests/__init__.py
polls/tests/test_bar.py
polls/tests/test_foo.py
```

## Tools used

- Pyenv: for configuring the Python runtime version (see `.python-version` file)
- Poetry: for managing project's Python dependencies
- Black: for linting Python files
- Docker Compose: _just_ for spinning up a Postgres DB locally
