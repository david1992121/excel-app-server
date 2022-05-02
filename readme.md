[![CI](https://github.com/david1992121/excel-app-server/actions/workflows/ci.yml/badge.svg)](https://github.com/david1992121/excel-app-server/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/david1992121/excel-app-server/branch/master/graph/badge.svg?token=OcBf2eNMb1)](https://codecov.io/gh/david1992121/excel-app-server)

# Excel App

Web service for managing statistic data of companies

## Overview

- Sheet CRUD
- Data Management (Profit, Growth, Variation, Validity and so on)
- Auto calculation of several measures ()

## Main Features

- DRF Restful API
- SimpleUI for django admin
- Swagger API Documentation
- AWS Deployment

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/david1992121/excel-app-server.git
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver