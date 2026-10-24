# Unitwise — Unit Converter

A responsive browser converter and Python conversion library for length, temperature, and weight. The web app runs locally in the browser and does not send entered values to a server.

## Features

- Length: meters, kilometers, miles, and feet.
- Temperature: Celsius, Fahrenheit, and Kelvin, with below-absolute-zero validation.
- Weight: kilograms, grams, and pounds.
- Browser app with category tabs, unit selectors, swap action, live results, responsive layout, and input errors.
- Python functions with validation for unsupported units, non-numeric/non-finite values, and non-finite results.
- pytest suite and GitHub Actions workflow.

## Run the web app

Open `index.html` in a browser. The app is a static page with no build step or JavaScript dependencies.

## Run Python tests

Python 3.12 or later is used by CI. Install the sole test dependency and run:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Project layout

```text
converter.py                 Python conversion functions
tests/                       pytest test suite
index.html                   Static web app and GitHub Pages entry point
.github/workflows/tests.yml  CI test workflow
docs/                        Legacy empty Pages files (not the configured entry point)
```

## Deployment

GitHub Pages is deployed from the repository root on `main`:
https://youssef-dev-lab.github.io/UnitConverter-Team-G/

The assignment brief was not present in this checkout. See [`docs/SUBMISSION_REPORT.md`](docs/SUBMISSION_REPORT.md) for the audit checklist, evidence, and outstanding submission items.
