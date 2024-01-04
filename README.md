# Django Authentication Project

This Django project provides a simple authentication system.

## Getting Started

These instructions will help you set up and run the project locally.

### Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (>=3.6)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Virtualenv](https://pypi.org/project/virtualenv/)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/sibashis9692/Assignment.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Assignment
    ```

3. Create a virtual environment:

    ```bash
    virtualenv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Apply migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

### Running the Project

```bash
python manage.py runserver
