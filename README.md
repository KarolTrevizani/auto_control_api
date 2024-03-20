# Auto Control API

## Overview

The Auto Control API is the backend part of a project aimed at providing comprehensive control over automotive-related expenses, user management, and vehicle tracking. 
<br>
This project is developed collaboratively by a team of four: on the backend, [Karoline Trevizani](https://github.com/KarolTrevizani) and [Rolf Matela](https://github.com/roollf), and on the frontend, [Emanuel Vidal](https://github.com/emanuelvidall) and [Fernando Custódio](https://github.com/Fcsla). The frontend can be found at [Frontend Repository URL](https://github.com/emanuelvidall/auto-control).

## Technical Stack
- **Framework**: Django
- **API**: Django Rest Framework (DRF)
- **Database**: Configurable

## Environment Setup

### Prerequisites
- Python 3.8 or newer
- pip (Python package installer)

Before starting, it is recommended to use a virtual environment to isolate project dependencies. This can be done using:

```bash
# Create the venv enviroment
python3 -m venv venv

# Activate the venv enviroment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

After activating the virtual environment, install the project dependencies.

### Requirements File

The `requirements.txt` file contains all the necessary packages to run this project. Ensure you have this file in your project root and have run the command above to install these dependencies.

```bash
# Go to the dir where the requirements.txt are
pip install -r requirements.txt
```

## Configuration

### Environment Variables

_Go to the dir where the file .env.dist are (It stays on the project dir)_

To configure your project environment, copy the `.env.dist` file to `.env` in the same directory. Update this `.env` file with your specific configurations. The `.env.dist` file serves as a template outlining all necessary environment variables.

```bash
cp .env.dist .env
# Edit .env to fill in your specific settings
```

### Django Settings

This project uses two settings files for different environments:

- `development.py` for development settings
- `production.py` for production settings

To run the project using the correct settings, specify the settings module when executing Django commands. For example:

```bash
python manage.py runserver --settings=auto_control.settings.development
```

## Running the Application

Ensure you have correctly set up your `.env` file and activated your virtual environment. To start the server with development settings, use:

```bash
python manage.py runserver --settings=auto_control.settings.development
```

## Project Structure

The Auto Control API is built using Django Rest Framework (DRF) and contains three main apps:

- `expenses`: Handles all operations related to managing expenses.
- `users`: Manages user authentication, registration, and profiles.
- `vehicles`: Manages vehicle-related information and operations.

## Contributing

This project is currently being developed by Karoline Trevizani, Rolf Matela, Emanuel Vidal, and Fernando Custódio. Contributions, bug reports, and feature requests are welcome.