## Student Details
Admission Number : 167753
Group: BBIT 2.2C 



## Django E_Commerce Project customer and Order 
This project demonstrates how to set up Django application with the E_Commerce System.Ecommerce syestem has the customer and order models.The customer model represents the customer entity and stores details regarding the customer while the order model represents order placed by the customer.The relationship between customer and order is that one customer can have many orders (One-Many relationship)


## Requirements

- Project folder
- Github repository
- Python 3.16.2 
- Virtual environment
- migrations


## SetUp Instructions

### 1. Clone the repository

clone the repository from Github:
```bash
git clone https://github.com/yourusername/django-E-Commerce.git
cd django-E-Commerce
```
### 2.Set up the environment
- Create a folder
- Open the folder in VS Code
- Create virtual environment (`py -m venv .venv`)
- Activate it (`.\.venv\Scripts\Activate.ps1`) -Powershell
              (`.\.venv\Scripts\activate.bat`)- CMD

- install Django using pip (`pip install django`)
- Create a project (`django-admin startproject E_Commerce`)
- Navigate Navigate to the project folder(`cd myproject`)
- Run development Server (`python manage.py runserver`)
 


### 3.Create the models
- models.py
- customer model
- order model

### 4.Create necessary migrations to set up the database

`python manage.py makemigrations`
`python manage.py migrate`

### Run the development server
`python manage.py runserver`


### Push to git hub
`git add .`
`git commit -m " "`
`git push`




