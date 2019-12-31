import requests
import bs4 
import sys
import re
import os





def in_csv_file(dictfile) :
    list1 = ["Url", "Name", "Location", "Position", "Salary", "Experience", "Eligibility", "Date"]
    #print (dictfile)
    for i in range (0,8) :
        if list1[i] in dictfile:    
            temp1 = str(dictfile[list1[i]]).replace(",", " / ").replace("\n", " ").replace(":", "").replace(";", "/")    
            f.write(temp1 + ",")    
        else :
            f.write("No Data" + ",")    
    f.write("\n")    
        
    






def company_scrapper(name,company_url,Date) :
    response = requests.get(company_url)    
    web_content = response.content    
    soup = bs4.BeautifulSoup(web_content, 'html.parser')    
    job_details = {}   
    job_details["Url"]= company_url    
    for job_description in soup.find_all("div", {"class" : "td-post-content"}) :    
        for details in (list(job_description.find_all("strong")) + list(job_description.find_all("b"))) :   
            if (re.search("^[a-zA-Z].*ompa.*", details.text.replace(u'\xa0', u' '))) :     
                Name = details.next_sibling    
                Name = str(Name).replace(u'\xa0', u' ')   
                job_details["Name"]= name   
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
                Eligibility = details.find_next().li      
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






def link_scrapper(soup) :
    for job_header in soup.findAll("h3", {"class" : "entry-title td-module-title"}) :    
        for link in job_header.find_all('a') :    
            Name = link.get('title')    
            Url = link.get('href')
            Date = link.find_next().time    
            Date = Date.text   
            company_scrapper(Name,Url,Date)   
           
    



 

def scrapping_start() :
    for page in range(1,2) :
        url = "https://apuzz.com/tag/2019-batch/page/"+str(page)+"/"
        response = requests.get(url)
        web_content = response.content  
        soup = bs4.BeautifulSoup(web_content, 'html.parser')    
        link_scrapper(soup)   
    
  
  
  
  


temp0 = 0 
def check() :
    global temp0   
    try :
        response = requests.get('https://apuzz.com/tag/2019-batch/', timeout=10)    
    except :
        temp0 = 1
        print ("NO INTERNET or OTHER PROBLEM\n")

     





file_name = "job_file.csv"
file_path = os.getcwd()     
if os.path.exists(file_path+"/"+file_name) :     
    os.remove(file_path+"/"+file_name)
f = open(file_name, "w", encoding='utf-8-sig')   
headers = "Url, Name, Location, Position, Salary, Experience, Eligibility, Date\n"
f.write(headers)    







check()
if temp0 == 0 :
    scrapping_start()

  
f.close()
            
            

            
            
            
            
            
            
