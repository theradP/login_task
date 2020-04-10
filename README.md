prerequisites 
- python 3.6 and above
-mongodb 3.4 and above 

Getting started 
- run a mongodb instance on your localhost 
- create a virtual env using virtualenc or conda
- traverse to the project directory on the terminal and execute following commands
    -pip install -r requirements.txt
    - python manage.py makemigrations 
    - python manage.py migrate 
    - python manage,py runserver

- then on your browser go to ip-address and port  on which the django server is deployed 
    '/accounts/'
    
    ex - 127.0.0.1:8000/accounts/
    to get started with the registration and login process