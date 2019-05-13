# Gallery

#### A photo gallery application

## Author 

[Jason Muchiri](https://github.com/jasonmuchiri)

## Description

A simple application that displays a variety of photos and their details once clicked.One can also search for photos in terms of categories and copy their link for sharing.

## Set up instuctions and installations

### Prerequisites

- python3.6 

- python virtual environment ~ to create one run the following command `python3.6 -m venv --without-pip virtual`

- python pip ~ to install pip activate virtual environment `source virtual/bin/activate` then run `curl https://bootstrap.pypa.io/get-pip.py | python`

- Postgres ~ to install follow the following commands in your home directory:
    `sudo apt-get update`
    `sudo apt-get install postgresql postgresql-contrib libpq-dev`
    `sudo service postgresql start`
    `sudo -u postgres createuser --superuser $USER`
    `sudo -u postgres createdb $USER`
    `touch .psql_history`

### Installation instructions

- Clone the repo ~ `git clone`

- Activate virtual environment: 
   `python3.6 -m venv --without-pip virtual` then `source virtual/bin/activate`

- Install all the dependancies in the requirements.txt file to get a development env running
   `pip3 install -r requirements.txt`

- Create a database 
   `psql`
   `CREATE DATABASE gallery;`

- Run initial migration

   `python3.6 manage.py makemigrations gallery`
   `python3.6 manage.py migrate`

- Run the app

   `python3.6 manage.py runserver`

- Open the `localhost:8000` to check if the app is running successfully.

### Dependancies 

All the project's dependancies are found in the requirements.txt file.Open it for reference.

## Technologies used 

  - HTML
  - CSS
  - Python3.6
  - Javascript
  - Postgresql
  - Bootstrap4

## Live link in heroku



## License

MIT License

Copyright (c) 2019 cooldragon
