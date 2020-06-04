# InformationSecurityProject
Repo for the project of the Information Security course at UniBZ.

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

Create a WordPress page containing a quiz.

The underlying database should be mySQL.

Launch the exploit with the following URL:

*http://app-uri/quiz-page*

## Victor CMS
Unzip VictorCMS.zip into server folder
Change the code in the "includes/db.php" with your data

- - $DB_host = ""; 
  - $DB_user = ""; 
  - $DB_pass = ""; 
  - $DB_name = "";

- Import the database file named "php_cms.sql"
