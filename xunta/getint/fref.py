import pandas as pd
import numpy as np
import smtplib
import config
import webbrowser
import requests
import bs4
import rocketreach
import json

SenderAddress = 'xs286@cornell.edu'
password = config.password

def find_recruiter_referral(c, loc):
    loc = '"' + loc + '"'
    newc = '"' + c + '"'
    recruiterquery = '"recruiter" "data science" site:linkedin.com'
    recruiterquery = newc + " " + recruiterquery + " " + loc
    for page in range(1,4):
        recruiterurl = "https://www.google.com/search?q={}".format(recruiterquery) + "&start=" + str((page - 1) * 10)
        webbrowser.open_new_tab(recruiterurl)
        res = requests.get(recruiterurl)
        if res.status_code == 200:
            print(res.status_code)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            linklist = [link for link in soup.find_all('a')]
            openlist = []
            for link in linklist:
                if "q=https://www.linkedin.com/in" in link.get('href'):
                    hyperlink = link.get('href').partition('=')[2]
                    hyperlink = hyperlink.partition('&')[0]
                    openlist.append(hyperlink)
    for i in openlist:
        webbrowser.open_new_tab(i)

    return openlist


def find_peer_referral(c, loc):
    loc = '"' + loc + '"'
    newc = '"' + c + '"'
    peerquery = '("tsinghua" OR "cornell" OR "peking university" OR "fudan" OR "University of Science and Technology of China" OR "jiaotong" OR "Nanjing")\
    "data scientist" site:linkedin.com'
    peerquery = newc + " " + peerquery
    
    for page in range(1,4):
        peerurl = "https://www.google.com/search?q={}".format(peerquery) + "&start=" + str((page - 1) * 10)
        res = requests.get(peerurl)
        if res.status_code == 200:
            print(res.status_code)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            linklist = [link for link in soup.find_all('a')]
            openlist = []
            for link in linklist:
                if "q=https://www.linkedin.com/in" in link.get('href'):
                    hyperlink = link.get('href').partition('=')[2]
                    hyperlink = hyperlink.partition('&')[0]
                    openlist.append(hyperlink)

    for i in openlist:
        webbrowser.open_new_tab(i)

    return openlist


def find_email(address):
    rr = rocketreach.Gateway(api_key=config.rocket_api_key)
    result = rr.account.get()
    if result.is_success:
        lookupresult = rr.person.lookup(linkedin_url=address)
    if lookupresult.is_success:
        print('email success')
    else:
        print('lookupfailed')

    return lookupresult.person
    
    #webbrowser.open_new_tab(url2)


def send_email(filename, position):
    e = pd.read_csv("C:/JospehShen/XunTa/data/contact/{}.csv".format(filename),encoding='utf8')
    personalemails = list(e['personalemail'])
    workemails = list(e['workmail'])
    emails = list(zip(personalemails,workemails))
    emails = [i[1] if pd.isnull(i[0]) else i[0] for i in emails]
    names = e['name'].values
    companies = e['company'].values
    titles = e['title'].values

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderAddress, password)
    
    for name, company, email, title in list(zip(names,companies,emails,titles)):
        name = name.split(" ")[0]
        if any(x in title for x in ['Recruiter','Talent','Sourcer']):
            msg = """
            Hello {},

            I am Xu(Joseph) Shen, a {} now working in a cybersecurity 
            company with a master's degree in statistics from Cornell. I got your 
            contact method from your LinkedIn and I am now actively seeking career 
            opportunities in the area of applied machine learning and data science. 
            
            I accumulated my working experience in end-to-end applied machine learning 
            model building, dashboard data visualization, simulation, and AB testing 
            in the industry for almost three years. I am proficient in SQL, python and R.
            Also, I hvae experience with modeling on large scale data set using cloud computing,
            driving business strategy through data-centric visualizations and working cross 
            functionally to commuicate complex ideas to different audience.

            Do you think I could pick your brain on the process of applying to a {} 
            position and what exciting problems can we solve at {}?
            
            Are you available for a quick phone call next week or so? Thank you so much!
            
            Best Regards,

            Xu Shen
            
            """.format(name, position, position, company)

            
            subject = "Xu Shen-Potential Senior Data Scientist Candidate-Aspiring {}".format(company)
            body = "Subject: {}\n\n{}".format(subject,msg)
            server.sendmail(SenderAddress, email, body)
        else:
            msg = """
            Hello {},

            I am Xu(Joseph) Shen, a data scientist now working in a cybersecurity 
            company with a master's degree in statistics from Cornell. I got your 
            contact method from your LinkedIn and I am now actively seeking career 
            opportunities in the area of applied machine learning and data science. 

            I am really fascinated with what you're doing at {}. I would love to get
            your career advice for 15-20 minutes.

            Most of my mentors told me if I want to grow further, I have to talk to 
            a senior data scientist solving real complex real-world problems. 
            Do you think I could pick your brain on your job and what motivated you to choose {}? 
            
            I would appreciate the opportunity to learn from you such as 
            (1)How you get started in this field?
            (2)What's the most exciting problem your team is facing right now? 
            (3)What is really required for advancing in this field?

            The conversation will help me gain insights into this field and career development.
            Are you available for a quick phone call next week or so? Thank you so much!
            
            Best Regards,
            Xu Shen
            
            """.format(name, company, company)

            #subject = "Xu Shen-Aspiring {}-Beijing Connection".format(company)
            #subject = "Xu Shen-Aspiring {}-Cornell Connection".format(company)
            subject = "Xu Shen-Aspiring {}-Looking for Advice From the Best".format(company)
            body = "Subject: {}\n\n{}".format(subject,msg)
            server.sendmail(SenderAddress, email, body)
    
    server.quit()


def get_recruiter_email_list(company, loc):
    recruiterlists = find_recruiter_referral(company, loc)
  
    df = []
    for i in recruiterlists:
        try:
            record = find_email(i)
            finalrec = {
                'company':record.current_employer,
                'name':record.name,
                'workmail':record.current_work_email,
                'personalemail':record.current_personal_email,
                'title':record.current_title
            }
            df.append(finalrec)
        except Exception as e:
            print(e)

    df = pd.DataFrame(df)
    df.to_csv('data/contact/contact_{}_recruiter.csv'.format(company))

    return df


def get_peer_email_list(company, loc):
    peerlists = find_peer_referral(company, loc)
    df = []
    for i in peerlists:
        try:
            record = find_email(i)
            finalrec = {
                'company':record.current_employer,
                'name':record.name,
                'workmail':record.current_work_email,
                'personalemail':record.current_personal_email,
                'title':record.current_title
            }
            df.append(finalrec)
        except Exception as e:
            print(e)

    df = pd.DataFrame(df)
    df.to_csv('data/contact/contact_{}_peers.csv'.format(company))

    return df

#TODO find_email_address()
#TODO add class config password in local env computer

if __name__ == "__main__":
    #contact_cvs_recruiter = get_recruiter_email_list('grubhub','boston')
    contact_spotify_peers = get_peer_email_list('grubhub','boston')
    #send_email('contact_twitter_peers','Data Scientist')


