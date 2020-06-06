# InformationSecurityProject
Repo for the project of the Information Security course at UniBZ. This repo contains the final report, all the plugins and CMS we exploited (apart from Wordpress) and the main.py which contains all the exploits we implemented. 

# Group Project
- Giacomo Melacini	15724
- Matteo Messmer      15725

# Objective
Implement exploits for existing vulnerabilities.
We will use exploitDB and CVEdetails databases to find vulnerabilities.

# Configurations

## CodeIgniter XSS

Install CodeIgniter (*v2.1.0*) from the given zip file. In the zip file there are already the demo files for the exploit. 

They can be found in:

- \codeigniter\application\controllers\xssdemo.php
- \codeigniter\application\views\xssdemo.php

In order to launch the exploit, type in the program the following URL:

*http://app-uri/index.php/xssdemo*

## Chained-Quiz SQL Injection

Install the provided version of the plugin in WordPress.

Create a quiz with a question.

Create a WordPress page containing a quiz.

The underlying database should be mySQL.

Launch the exploit with the following URL:

*http://app-uri/quiz-page*

## Victor CMS
Unzip VictorCMS.zip into server folder

Change the code in the "includes/db.php" with your data

- $DB_host = ""; 
- $DB_user = ""; 
- $DB_pass = ""; 
- $DB_name = "";

Import the database file named "php_cms.sql"

Launch the exploit with the URL of the main page

## Simple Membership
For this exploit we used Wordpress 4.9

Install and activate the plugin in wordpress

Go into the Simple Membership Dashboard

Create at least one role and one member with that role (the role id should be 2, because the exploit makes an example using that id)

Launch the exploit with the URL of the main page
