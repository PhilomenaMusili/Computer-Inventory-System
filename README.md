# Computer Inventory System

A comprehensive system for managing and tracking computers within an organization.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Static Files](#static-files)
- [Templates](#templates)
- [Customization](#customization)
- [Documentation](#documentation)
- [License](#license)

## Installation

1. Clone the repository:

    git clone https://github.com/your-username/computer-inventory.git
    

2. Navigate to the project directory:

    cd computer-inventory
  
3. Install dependencies:

    pip install -r requirements.txt

4. Apply migrations:

    python manage.py migrate
    
5. Run the development server:

    python manage.py runserver
  
6. Open your browser and visit [http://localhost:8000/](http://localhost:8000/) to access the computer inventory system.

## Usage

The Computer Inventory System helps you manage and track computers within your organization. Follow these steps to get started:

1. Add new computers to the system.
2. Update information such as computer specifications, ownership, and location.
3. View and search for computers based on various criteria.
4. Generate reports for inventory analysis.


## Configuration

Configure the system settings in `settings.py` if needed. Common configurations include database settings and authentication.

## Static Files

Before running the project, collect static files:

python manage.py collectstatic

