import requests
from bs4 import BeautifulSoup as bs
import os,sys
import argparse
from tqdm import tqdm
import re

# ---------------------------------------------------------------------------

def rename(name):
    
    """
       Function to rename minutes with standardised format
       Contains a bunch of regex expressions to find the dates
    """
    
    basename="Formal-Minutes-"
    
    m=re.search( r"\d\d-\d\d\D", name)
    if m:
        dates=m.group()[0:2]+"-"+m.group()[3:5]
        nodate=False
    else:
        nodate=True
    
    if nodate:
        m=re.search( r"\d\d\d\d-\d\d\d\d", name)
        if m:
            if m.group()[0:2]=="20" and m.group()[5:7]=="20" and int(m.group()[7:9])>int(m.group()[2:4]):
                nodate=False
                dates=m.group()[2:4]+"-"+m.group()[7:9]
            else:
                nodate=True
        else:
            nodate=True

    if nodate:
        m=re.search( r"\D\d\d\d\d\D", name)
        if m:
            y1 = m.group()[1:3]
            y2 = m.group()[3:5]
            if int(y2)<int(y1):
                nodate=True
            else:
                dates=m.group()[1:3]+"-"+m.group()[3:5]
                nodate=False
        else:
            nodate=True

    if nodate:
        m=re.search( r"\D\d\d\d\d\d\d\D", name)
        if m:
            if m.group()[1:3]=="20" and int(m.group()[5:7])>int(m.group()[3:5]):
                nodate=False
                dates=m.group()[3:5]+"-"+m.group()[5:7]
            else:
                nodate=True
        else:
            nodate=True

    if nodate:
        outname=name
    else:
        outname = basename+dates+".pdf"

    return outname


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    
    # optional command line arguments:
    parser = argparse.ArgumentParser(description='Download PDF minutes of all commons select committees')
    parser.add_argument("-p", "--path", help="directory name to store minutes")
    args = parser.parse_args()
    
    # set the data directory:
    if args.path==None:
        filepath = "SELECT-COMMITTEES"
    else:
        filepath = args.path

    # set base url:
    baseurl = "https://www.parliament.uk"
    url = "/business/committees/committees-a-z/commons-select/"

    r = requests.get(baseurl+url)
    page = r.text
    soup=bs(page,'lxml')

    com_list = []; com_links=[]
    for ul in soup.find_all("ul", class_='square-bullets-a-to-z'):
        coms = ul.find_all("h3")
        for com in coms:
            com_list.append(com.text)
            com_link = com.find("a").get("href")
            if com_link is not None:
                com_links.append(baseurl+com_link)
            else:
                com_links.append("None")

    # if the directory already exists, delete it:
    os.system('rm -rf '+filepath+' \n')

    # create the data directory:
    os.system("mkdir "+filepath+" \n")

    # then create the subdirectories, one for each committee:
    for i in range(0,len(com_list)):
        
        dirname = com_list[i].replace(" ","-").replace("(","").replace(")","").replace(",","").replace("'","").upper()
        os.system("mkdir ./"+filepath+"/"+dirname+" \n")

    min_links=[]
    for i in range(0,len(com_list)):

        if com_links[i]=="None":
            break

        r = requests.get(com_links[i])
        page = r.text
        soup=bs(page,'lxml')

        m="None"
        aa = soup.findAll("a")
        for a in aa:
            if a.text.lower()=="formal minutes":
                m = baseurl+a.get("href")

        min_links.append(m)


    for i in tqdm(range(0,len(com_list))):

        link = min_links[i]

        if link!="None":

            r = requests.get(link)
            page = r.text
            soup=bs(page,'lxml')
            
            aa = soup.find_all("a")
            for a in aa:
                if a.get("href")!=None:

                    getpdf=False
                    href = a.get("href")

                    if href.find('.pdf')>-1:
                        getpdf=True

                    if href.split('/')[-1].lower().find('attendance')>-1 or href.split('/')[-1].lower().find('attendence')>-1:
                        getpdf=False
                    if href.split('/')[-1].lower().find('members-att')>-1:
                        getpdf=False

                if getpdf:
                    
                    # check because DCMS seems to put in the full url for some minutes:
                    if href.find(baseurl)>-1:
                        pdf = href
                    else:
                        pdf = baseurl+href

                    response = requests.get(pdf)
                        
                    # set the directory to save the PDF:
                    dirname = com_list[i].replace(" ","-").replace("(","").replace(")","").replace(",","").replace("'","").upper()
                    pdfdir = "./SELECT-COMMITTEES/"+dirname+"/"
                        
                    # set the name of the PDF:
                    name = href.split('/')[-1].replace('%20','-')
                    pdfname = rename(name)

                    with open(pdfdir+pdfname, 'wb') as f:
                        f.write(response.content)
