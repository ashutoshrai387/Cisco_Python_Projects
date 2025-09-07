"""
Question 4: Web Scraping Assignment
Read a list of URLs from urls.txt, verify each returns HTTP status 200, scrape all <a href="..."> links, normalize them to absolute URLs, and write results to separate output files:
•	googleurls.txt
•	ciscourls.txt
•	wikiurls.txt
Also produce a short summary report with counts and basic link analytics.
urls.txt
https://www.google.com
https://www.cisco.com
https://www.wikipedia.org

Functional Requirement:
•	Read urls.txt line-by-line; ignore blanks and comments (lines starting with #).          #
•	For each URL:                                                                            #               
o	Make an HTTP GET request with a custom User-Agent header and a timeout (e.g., 10s).      #
o	If status != 200 → record it in summary.csv with total_links=0 and skip scraping.        #
o	If status == 200:                                                                        #
	Parse HTML and extract all <a> tags that have href.                                      #
	Convert relative links to absolute URLs using the page’s base URL.                       #
	Keep only http/https links                                                               #
	Write one link per line to the site-specific file:                                       #
	googleurls.txt for www.google.com                                                        #
	ciscourls.txt for www.cisco.com                                                          #
	wikiurls.txt for www.wikipedia.org                                                       #
	Count unique domains from the collected links for the summary.                           #
•	Must handle any number of URLs (don’t hardcode to 3).                                    #
•	Handle errors gracefully (timeouts, invalid URLs) and still produce summary.csv          #
"""

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin,urlparse

# creating and initializing summary.csv with headers
with open("summary.csv","w",newline="") as sobj:
    writer=csv.writer(sobj)
    header = ["Host Name","Response Status Code","Total Links","Unique Domains"]
    writer.writerow(header)


# opening url and performing operations
with open("urls.txt","r") as fobj:
    for line in fobj:
        stripped_line=line.strip()
        if stripped_line.startswith("#"):
            continue
        else:
            try:
                hostname=stripped_line
                response=requests.get(hostname,timeout=15)
                if response.status_code != 200:
                    with open("summary.csv","a",newline="") as sobj:
                        writer=csv.writer(sobj)
                        data=[hostname,response.status_code,0,0]
                        writer.writerow(data)
                    print("Host - ",hostname,"Not Responding")
                        
                elif response.status_code == 200:
                    print("Host - ",hostname,"is responsive.")
                    soup=BeautifulSoup(response.text,'html.parser')
                    title=hostname.split('.')[1]+"urls.txt"
                    count = 0
                    unique_domains = set()
                    with open(title,"w") as urlobj:
                        for link in soup.find_all('a'):
                            url=link.get('href')
                            if url.startswith("http") or url.startswith("https"):
                                urlobj.writelines([url,"\n"])
                                count += 1
                                parsed_url=urlparse(url)
                                domain=parsed_url.netloc
                                unique_domains.add(domain)
                            else:
                                absolute_url= urljoin(hostname,url)
                                urlobj.writelines([absolute_url,"\n"])
                                count += 1
                                parsed_url=urlparse(absolute_url)
                                domain=parsed_url.netloc
                                unique_domains.add(domain)
                        with open("summary.csv","a",newline="") as sobj:
                            writer=csv.writer(sobj)
                            data=[hostname,response.status_code,count,len(unique_domains)]
                            writer.writerow(data)
            except Exception as err:
                print("Exception Occured : ",err)