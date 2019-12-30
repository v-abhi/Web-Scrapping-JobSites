JOB_SCRAPPER is basically a PYTHON programe/script.

It extract JOB_DETAILS like Job_Name, Url, Salary, Location, Eligibility, Experience, Position and Advertisement_Date of many Companies.

These extracted data are saved into a CSV_File for better Analysis.




OLD_METHODS
    For searching about job vacancies, we have to search on Google or other Websites. We are given links about many companies.
    We have to open all job_links and gather their job_details one by one. We have to remember previous job_details while shifting on
    other job_links and while comparing among them. Or we have to pen down their details.
    
    It CONSUME SO MUCH TIME in LOADING_WEBPAGES, PENNING_DOWN_INFOs and SO MANY CLICKS.
    It ALSO REQUIRE so much CPU_Time and RAM and STRONG NETWORK.
    IT TAKES approx 10-15 MINUTES for 40 COMPANIES ATLEAST AND 40 TABS TOO.
    After that, It's quite possible, we may FORGET some details.


NEW_METHODS
    Using this programe/script, we can gather ALL these job_details about different jobs in A SINGLE CSV_File.
    
    IT JUST TAKES 1-2 MINUTES in gathering Job_Details of approx 40 COMPANIES and STORING in CSV_File. 1-2 MINUTES VS 10-15 MINUTES.
    IT CONSUMES VERY LITTLE CPU_TIME as well as RAM and WORKS in LOW NETWORK too.
    NO NEED OF BROWSER. 
    It becomes much easier to analyse among them BCZ ALL DATAS ARE GIVEN IN SYSTEMATIC WAY i.e. ROWS and COLUMNS.
    
  
  
    
    
    
    
    LIBRARIES/TECHNOLOGIES/LANGUAGES USED :
        PYTHON3
        ANT TEXT EDITOR
        any EXCEL programe that can handle CSV file
    
    
        LIBRARIES : bs4 and requests
            if not installed 
            install them
            contact google
        
    
        
    HOW TO USE : 
        download a file named "job_scrapper.zip"
        unzip or extract files from this
        
        open "command prompt" or "terminal" in windows and ubuntu respectivellyg
        go to the folder in which files are located i.e. in folder named "job_scrapper"
        
        run the python programe named "job_details_scrapper.py"
            command :
                python3 job_details_scrapper.py
    
    
    
    
  
    RESULTS :
    
        after 1-2 minutes after completion of this programe
        
        A CSV FILE named "job_file.csv" will be created containing details
        
        
        
        
        
    REMARKS :
        ## working on Ubuntu
        ## Hope works on others too.
        
