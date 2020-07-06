#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:31:54 2020

@author: skand
"""
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from user_agents import getRandomUserAgent

user_agent = getRandomUserAgent()
def getDetails(cin):
    session = requests.session()
    variable2 = session.get(url="http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do",
                       headers={"Host": "www.mca.gov.in",
                                "User-Agent": user_agent ,
                                "Referer": "http://www.mca.gov.in/"})
    #print(variable2)
    #print(session.cookies)
    if variable2.status_code!=200:
        return 'connection error'
    url = "http://www.mca.gov.in/mcafoportal/companyLLPMasterData.do"
    myobj = {'companyName': '','companyID': cin,
             'displayCaptcha': 'false',
             'userEnteredCaptch': ''}

    header={'Host': 'www.mca.gov.in',
            'Connection': 'keep-alive',
            'Content-Length': '91',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.mca.gov.in',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            }

    final_request = session.post(url=url,headers=header,data=myobj)

    if final_request.status_code!=200:
        return 'connection error'
    #print(final_request.text)
    #f = open("myfile.txt", "w")
    #f.write(final_request.text)
    return(final_request.text)
    #print(session.cookies)





def getCompanyDetails():
    companyDetail=soup.find("div", {"id": "companyMasterData"}).find('table',{'id':'resultTab1'}).findAll("tr")
    companydetail = []
    for trow in companyDetail:
        tem=trow.findAll('td')[1].text.strip()
        if tem.strip()=='-':
            companydetail.append(None)
        else:
            companydetail.append(tem.strip() or None)
    if companydetail[7]:
        companydetail[7]=float(companydetail[7])
    if companydetail[8]:
        companydetail[8]=float(companydetail[8])
    if companydetail[9]:
        companydetail[9]=int(companydetail[9])
    if companydetail[10]:
        companydetail[10] = datetime.strptime(companydetail[10], "%d/%m/%Y")
    if companydetail[17]:
        companydetail[17] = datetime.strptime(companydetail[17], "%d/%m/%Y")
    if companydetail[18]:
        companydetail[18] = datetime.strptime(companydetail[18], "%d/%m/%Y")

    return(companydetail)

def getLlpDetails():
    companyDetail=soup.find("div", {"id": "llpMasterData"}).find('table',{'id':'resultTab3'}).findAll("tr")
    companydetail = []
    for trow in companyDetail:
        tem=trow.findAll('td')[1].text.strip()
        if tem.strip()=='-':
            companydetail.append(None)
        else:
            companydetail.append(tem.strip() or None)
    if companydetail[2]:
        companydetail[2]=int(companydetail[2])
    if companydetail[3]:
        companydetail[3]=int(companydetail[3])
    if companydetail[9]:
        companydetail[9]=float(companydetail[9])
    #if companydetail[10]:
        #companydetail[10]=int(companydetail[10])
    if companydetail[5]:
        companydetail[5] = datetime.strptime(companydetail[5], "%d/%m/%Y")
    if companydetail[12]:
        companydetail[12] = datetime.strptime(companydetail[12], "%d/%m/%Y")
    if companydetail[13]:
        companydetail[13] = datetime.strptime(companydetail[13], "%d/%m/%Y")

    return(companydetail)


def getForeignCompanyDetails():
    companyDetail=soup.find("div", {"id": "foreignCompanyMasterData"}).find('table',{'id':'resultTab2'}).findAll("tr")
    companydetail = []
    for trow in companyDetail:
        tem=trow.findAll('td')[1].text.strip()
        if tem.strip()=='-':
            companydetail.append(None)
        else:
            companydetail.append(tem.strip() or None)

    #if companydetail[10]:
        #companydetail[10]=float(companydetail[10])

    if companydetail[2]:
        companydetail[2] = datetime.strptime(companydetail[2], "%d/%m/%Y")


    return(companydetail)



def getCharges():
    companyCharges=soup.find("div", {"id": "chargesRegistered"}).find('table',{'id':'resultTab5'}).findAll("tr")
    companycharges = []
    prevname =  ' '
    for trow in companyCharges[1:]:
        chargeslist = []
        for i in trow.findAll("td"):
            if i.text.strip()=='No Charges Exists for Company/LLP':
                return chargeslist
            if i.text.strip()=='-':
                chargeslist.append(None)
            else:
                chargeslist.append(i.text or None)
        if chargeslist[0] !=None:
            prevname = chargeslist[0]
        else:
            chargeslist[0]=prevname
        if chargeslist[1]:
            chargeslist[1]=float(chargeslist[1])
        if chargeslist[2]:
            chargeslist[2] = datetime.strptime(chargeslist[2], "%d/%m/%Y")
        if chargeslist[3]:
            chargeslist[3] = datetime.strptime(chargeslist[3], "%d/%m/%Y")
        #print(chargeslist)
        companycharges.append(chargeslist)
    return(companycharges)


def getDirectors():
    companyDirectors=soup.find("div", {"id": "signatories"}).find('table',{'id':'resultTab6'}).findAll("tr")
    companydirectors = []
    for trow in companyDirectors[1:]:
        directordetail = []
        for i in trow.findAll("td"):
            if i.text.strip()=='-':
                directordetail.append(None)
            else:
                directordetail.append(i.text.strip() or None)
        if directordetail[2]:
            directordetail[2] = datetime.strptime(directordetail[2], "%d/%m/%Y")
        if directordetail[3]:
            directordetail[3] = datetime.strptime(directordetail[3], "%d/%m/%Y")
        companydirectors.append(directordetail)
    return(companydirectors)

def getType():
    if soup.find("div", {"id": "companyMasterData"}).find('table'):
        return 'company'
    elif soup.find("div", {"id": "llpMasterData"}).find('table'):
        return 'llp'
    elif soup.find("div", {"id": "foreignCompanyMasterData"}).find('table'):
        return 'foreigncompany'


def getalldata(cin):
    response = getDetails(cin)
    if response == 'connection error':
        return 'connection error'
    global soup
    soup=BeautifulSoup(response,'html.parser')
    CinNotFoundError = soup.find("div", {"id": "msg_overlay"})
    if CinNotFoundError:
        return(CinNotFoundError.text)
    else:
        return ('success')
    #getCompanyDetails()
    #getCharges()
    #getDirectors()


#getalldata('U01132WB1996PTC168244')
#print(*getCharges(),sep='\n')

#print(CinNotFoundError['style'])
#invalidCinError = soup.find("div", {"id": "alertmsg_overlay"})
#print(invalidCinError)
#print(invalidCinError['style'])
