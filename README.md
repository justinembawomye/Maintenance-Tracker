# Maintenance-Tracker 
---
[![Build Status](https://travis-ci.org/Besufekadsm/Maintenance-Tracker.svg?branch=master)](https://travis-ci.org/Besufekadsm/Maintenance-Tracker)
[![Coverage Status](https://coveralls.io/repos/github/Besufekadsm/Maintenance-Tracker/badge.svg?branch=master)](https://coveralls.io/github/Besufekadsm/Maintenance-Tracker?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Description
Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

## Project Features
* Users can create accounts and are able to login
* Users can request for a Repair/Maintenance 
* Users can manage their requests
* Admin can Approve/Disapporve a request
* Admin can view all requests made
* Admin can view the details of requests

## Project Structure
* **root:** The root folder contains all the html files of the project.
* **design:** The design folder contains all the design files that have been developed before starting the project.
* **static:** The static folder contains all the css,images and js for the project.   

### API End Points Version 1

Endpoint | Functionality| Access
------------ | ------------- | -------------
GET /api/v1/users/requests |Gets all requests of a specified user. | PUBLIC
GET /api/v1/users/requests/<requestId> | get a specific request of a user | PUBLIC
POST /api/v1/users/requests | Creates a new request| PRIVATE
PUT /api/v1/users/requests/<requestId> | Modify a user request | PRIVATE
POST /api/v1/login | Logs in a User | PUBLIC

## Tests
The Project has been tested on
* Google Chromium (Version 66.0.3359.181)
* Mozilla Firefox (Version 60.0.1 )

## Instalation

Clone the GitHub repo:
 
`$ git clone https://github.com/Besufekadsm/Maintenance-Tracker`

cd into the folder and install a Virtual Environment

`$ virtualenv --python=python3 mtracker`

Activate the virtual environment

`$ mtracker/bin/activate`

Install all application requirements from the requirements file found in the root folder

`$ pip install -r requirements.txt`

Start Server 

`python progect.py`.

## GitHub Pages
Go to [Maintenance-Tracker](https://besufekadsm.github.io/Maintenance-Tracker/)

## Contributors
* Besufekad Shifferaw

## How to Contribute
1. Download and install Git
2. Clone the repo `git clone https://github.com/Besufekadsm/Maintenance-Tracker.git`

## ScreenShots

![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_homepage.png)
![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_login.png)
![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_register.png)
![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_user_dashboard.png)
![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_admin_dashboard.png)
![alt text](https://besufekadsm.github.io/Maintenance-Tracker/design/UI/UI_manage_users.png)