# -*- coding: utf-8 -*-

import re
import os
import csv
import time
import string
import urllib2
from bs4 import BeautifulSoup


# We are going to iterate through all leters (a - z).
letter_list = string.lowercase[:26]

# We check if the results directory exists
if not os.path.exists('results'):
    # If it's not there, we create it
    os.makedirs('results')

# Each letter has its own page with its drug list.
# We will be saving a CSV file for each starting letter.
for letter in letter_list:
    with open('results/vademecum-' + str(letter) + '.csv', 'wb') as csvfile:
        # We will be saving the drug code, name and URL.
        fieldnames = ['cod_nacion', 'nombre', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        print "Going for letter " + str(letter)
        vademecum = "http://vademecum.es/medicamentos-" + letter + "_1"

        # We are faking our user-agent to appear like a regular browser.
        # This prevents unwanted connection resets.
        headers = {'User-agent' : 'Mozilla/5.0'}
        req = urllib2.Request(vademecum, None, headers)
        page = urllib2.urlopen(req, timeout = 3).read()
        soup = BeautifulSoup(page, "html.parser")

        drug_list = soup.find('ul', class_='no-bullet')

        i = 0
        for row in drug_list.findAll("li"):
            i += 1
            link = row.find('a')
            drug_link = 'http://vademecum.es' + str(link['href']).strip().encode('utf8')
            drug_name = link.contents[0].strip().encode('utf8')
            time.sleep(0.11)

            req = urllib2.Request('http://vademecum.es' + str(link['href']), None, headers)
            page = None
            # This loop prevents the script from stopping in case of a connection error.
            while True:
                try:
                    page = urllib2.urlopen(req, timeout = 3).read()
                # If user is trying to stop the script, we will comply
                except (KeyboardInterrupt, SystemExit):
                    raise
                # If something else happens, we will just ignore it and move forward
                except:
                    print "\t\t[WARNING] Exception trying to open page!"
                    continue
                break

            drug_soup = BeautifulSoup(page, "html.parser")
            for elem in drug_soup.findAll("strong"):
                try:
                    if "digo Nacional:" in elem.contents[0]:
                        drug_code = elem.parent.find("span").contents[0].strip().encode('utf8')
                        print "\tGetting drug " + drug_code + " (" + letter + "-" + str(i) + ")"
                        writer.writerow({'cod_nacion': drug_code, 'nombre': drug_name, 'url': drug_link})
                except (KeyboardInterrupt, SystemExit):
                    raise
                    continue
                except:
                    print "\t\t[WARNING] Exception trying to get drug_code!"
                    continue
        print "\tDone!"
    time.sleep(1)
