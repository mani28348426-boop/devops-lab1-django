# DevOps Lab Portfolio – Django Project

## Project overview

This repository contains a simple Django web application built as part of a DevOps lab assignment. The project demonstrates a basic Django site with multiple pages, a minimal template structure, and URL routing. It also includes a GitHub Actions CI workflow for linting and testing the application.

The app consists of two Django apps:

- `main`: Handles the core views and templates for the site, such as the homepage and a shopping page.
- `uos_portfolio`: The main project configuration, including settings, WSGI/ASGI, and project-level URLs.

## Features

- Home page and shopping page rendered with Django templates
- URL routing configured across apps
- SQLite database (default Django setup)
- GitHub Actions CI workflow to run linting and testing the application


## Getting Started

### Prerequisites

- Python 3.10 or later
- [pip](https://pip.pypa.io/en/stable/) for package management

### Installation

```bash
# clone the repository
git clone https://github.com/mani28348426-boop/devops-lab1-django.git
cd devops-lab1-django

# create a virtual environment
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

### Running the Development Server

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to view the site.

## Testing and CI

Tests are defined under each app (if any) and can be run with:

```bash
python manage.py test
```

The `.github/workflows/ci.yml` file configures a GitHub Actions workflow that:

1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs linting with `flake8`
5. Runs Django tests

## Project Structure

```
/db.sqlite3
/manage.py
/requirements.txt
/main/
    urls.py
    views.py
    templates/main/index.html
    templates/main/shopping.html
/uos_portfolio/
    settings.py
    urls.py
    wsgi.py
    asgi.py
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance functionality, add tests, or improve documentation.

## License

This project is provided for educational purposes and does not have a specific license.

