# api-calculator

Quickstart
----------

### Then bootstrap environment with ``poetry``:

    poetry install
    poetry shell

### Install dev-dependencies:
    poetry install --with dev

### Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application:

    touch .env
    echo DEBUG=True >> .env

### To run tests:

    source scripts/test.sh

### To run the web application in debug use:

    uvicorn app.main:app --reload
    --- or ---
    poetry run ./run.sh

