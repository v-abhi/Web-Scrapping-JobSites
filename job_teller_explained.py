# importing time module
import time

start = time.time()     #countdown start









# request library is used for establishing and fetching data from internet
import requests
# bs4 library is used for parsing and extracting text data from webpage
import bs4 
# sys library is for system calls
import sys
# re library is used for task related to regualr expressions 
import re
# os library is used for file handling
import os









### function
## storing data in opened csv file
def in_csv_file(dictfile) :
    list1 = ["Url", "Name", "Location", "Position", "Salary", "Experience", "Eligibility", "Date"]
    #print (dictfile)
    for i in range (0,8) :
        if list1[i] in dictfile:    #checking wether value_having_specific_key is present or not
            temp1 = str(dictfile[list1[i]]).replace(",", " / ").replace("\n", " ").replace(":", "").replace(";", "/")    #replacing characters, "," in csv file leads to new column and so on.
            f.write(temp1 + ",")    #writting content to another file
        else :
            f.write("No Data" + ",")    #in case no value_having_specific_key is found 
    f.write("\n")    #new line in csv file
        
    







### function
## extracting info from each job_page
def company_scrapper(name,company_url,Date) :
    response = requests.get(company_url)    #fetching a webpage of particular webpage for job
    web_content = response.content    #extracting content
    soup = bs4.BeautifulSoup(web_content, 'html.parser')    #parsing that content and storing them
    job_details = {}    #creating a DICTIONARY_DATATYPE for storing informations
    job_details["Url"]= company_url    #storing value with specified key
    for job_description in soup.find_all("div", {"class" : "td-post-content"}) :    #extracting only specified part of web content
        for details in (list(job_description.find_all("strong")) + list(job_description.find_all("b"))) :   #again extracting only specified part of web content
            if (re.search("^[a-zA-Z].*ompa.*", details.text.replace(u'\xa0', u' '))) :     #searching presence of string given in specific pattern from text content of tag 
                Name = details.next_sibling    #searching and storing next sibling (next text content of its parent) <p> <1> ..text1.. </1> <2> ..next_sibling.. </2> </p> 
                Name = str(Name).replace(u'\xa0', u' ')    #replacing some specific texts
                job_details["Name"]= name   #storing value in "Name" key
            elif (re.search("^[a-zA-Z].*itio.*", details.text.replace(u'\xa0', u' '))) :
                Position = details.next_sibling
                Position = str(Position).replace(u'\xa0', u' ')
                job_details["Position"]= Position
            elif (re.search("^[a-zA-Z].*lar.*|ackag.*", details.text.replace(u'\xa0', u' '))) :
                Salary = details.next_sibling
                Salary = (str(Salary).replace(u'\xa0', u' '))
                job_details["Salary"]= Salary
            elif (re.search("^[a-zA-Z].*rienc.*", details.text.replace(u'\xa0', u' '))) :
                Experience = details.next_sibling
                Experience = str(Experience).replace(u'\xa0', u' ')
                job_details["Experience"]= Experience
            elif (re.search("Job Location", details.text.replace(u'\xa0', u' '))) :
                Location = details.next_sibling
                Location = str(Location).replace(u'\xa0', u' ')
                job_details["Location"]= Location
            elif (re.search("^[a-zA-Z].*gibil.*", details.text.replace(u'\xa0', u' '))) :
                Eligibility = details.find_next().li    #finding next tag named <li>..</li> from present tag    
                try :
                    Eligibility = Eligibility.text
                    Eligibility = str(Eligibility).replace(u'\xa0', u' ')
                    job_details["Eligibility"]= Eligibility
                    break
                except :
                    a =0
        break
    job_details["Date"]= Date
    in_csv_file(job_details)







### function
## extracting name, link, notification_date and extracting info from that link
def link_scrapper(soup) :
    for job_header in soup.findAll("h3", {"class" : "entry-title td-module-title"}) :    #extracting only specified part of web content (only 'h3' with specified attribute-value pair)
        for link in job_header.find_all('a') :    #again extracting specific part from extracted web content (only 'a')
            Name = link.get('title')    #extracting value of meta_data from extracted webcontent stored in         <a metadata1=value, --  >.....</a>
            Url = link.get('href')
            Date = link.find_next().time    #finding next tag named <time>..</time> from present tag named <a>..</a>
            Date = Date.text    #extracting text part of given tag        <time> ..text.. </time>
            company_scrapper(Name,Url,Date)    #calling next function
            #sys.exit("")   #to exit programe
    








 
### function  
## scarapping page page of sites  
def scrapping_start() :
    for page in range(1,3) :
        url = "https://apuzz.com/tag/2019-batch/page/"+str(page)+"/"
        response = requests.get(url)
        web_content = response.content  #extracting web_content
        soup = bs4.BeautifulSoup(web_content, 'html.parser')    #parsing of recieved web content
        link_scrapper(soup)    #calling next function
    
  
  
  
  
  
  

### gloabal variable
temp0 = 0 
### function 
## function to check internet connection availability 
def check() :
    global temp0    #because, global variable can not be initialized in function
    try :
        response = requests.get('https://apuzz.com/tag/2019-batch/', timeout=10)    #getting webpage all info in dictionary data type
    except :
        temp0 = 1
        print ("NO INTERNET or OTHER PROBLEM\n")

     








file_name = "job_file.csv"
file_path = os.getcwd()     #getting current working directory location
if os.path.exists(file_path+"/"+file_name) :     #checking wether csv_file exists or not
    os.remove(file_path+"/"+file_name)
f = open(file_name, "w", encoding='utf-8-sig')   #creating new file in csv format
headers = "Url, Name, Location, Position, Salary, Experience, Eligibility, Date\n"
f.write(headers)    #writting content in csv file








    





### calling functions
check()
if temp0 == 0 :
    scrapping_start()

  




end = time.time()
print ("Total Time Elasped" + "  " + str(end-start)) 
f.close()
            
            
            
            
            
            
            
            
            
