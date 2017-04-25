# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
import string
import csv
import time

letter_list = string.lowercase[:26]


for letter in letter_list:
    with open('vademecum-' + str(letter) + '.csv', 'wb') as csvfile:
        fieldnames = ['cod_nacion', 'nombre', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        print "Going for letter " + str(letter)
        vademecum = "http://vademecum.es/medicamentos-" + letter + "_1"

        headers = {'User-agent' : 'Mozilla/5.0'}
        req = urllib2.Request(vademecum, None, headers)
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page, "html.parser")

        drug_list = soup.find('ul', class_='no-bullet')

        for row in drug_list.findAll("li"):
            link = row.find('a')
            drug_link = 'http://vademecum.es' + str(link['href']).strip().encode('utf8')
            drug_name = link.contents[0].strip().encode('utf8')
            time.sleep(0.11)

            req = urllib2.Request('http://vademecum.es' + str(link['href']), None, headers)
            page = None
            while True:
                try:
                    page = urllib2.urlopen(req).read()
                except:
                    print "\t\t[WARNING] Exception trying to open page!"
                    continue
                break
            #page = urllib2.urlopen('http://vademecum.es' + str(link['href']))
            drug_soup = BeautifulSoup(page, "html.parser")
            for elem in drug_soup.findAll("strong"):
                if "digo Nacional:" in elem.contents[0]:
                    drug_code = elem.parent.find("span").contents[0].strip().encode('utf8')
                    print "\tGetting drug " + drug_code
                    writer.writerow({'cod_nacion': drug_code, 'nombre': drug_name, 'url': drug_link})

        print "\tDone!"
    time.sleep(1)
