#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import urllib.request
from xml.dom.minidom import *
zaehler = 1
text = ""
form = cgi.FieldStorage()
response = urllib.request.urlopen("https://www.siebenpfeiffer-gymnasium.de/YmvWhf83s3/webplan1.xml")
xmlquellcode = response.read().decode("utf-8")
xmldoc = parseString(xmlquellcode)
print("Content-Type: text/html")
print()

def Stufen(klasse, k):
    alles = []
    liste = []
    kKlasse = k.getElementsByTagName("Stufe")
    for var in kKlasse:
        if var.firstChild.nodeValue == klasse:
            liste = [var.firstChild.nodeValue] + [var.nextSibling.nextSibling.firstChild.nodeValue] + [var.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.nodeValue] + [var.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.nodeValue] + [var.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.nodeValue]
            alles = alles + liste

    return(alles)

def Datum(doc):
    k = doc
    kDatum = k.getElementsByTagName("Datum")
    b = kDatum[0].firstChild.nodeValue
    return b

def Nummer(doc):
    k = doc
    kNummer = k.getElementsByTagName("Nummer")
    for element in kNummer:
        aktuellerKnoten = element.firstchild
        b = aktuellerKnotenfirstChild.nodeValue
        return b
text = """<?xml version="1.0" encoding="utf-8" ?> """
text = text + "\n"
text = text + "<!DOCTYPE html>"
text = text + "\n"
text = text + "<html>\n"
text = text + "<head>\n"
text = text + """<meta charset="UTF-8">\n"""
text = text + "<title>Persönlicher Vertretungsplan SGK</title>\n"
text = text + "</head>\n"
text = text + "<body>\n"
text = text + Datum(xmldoc) + "\n"
text = text + """<table border="1">\n<thead>\n<tr>\n<th>Stufe</th>\n<th>Fach</th>\n<th>Kurs</th>\n<th>Lehrer</th>\n<th>Anmerkung</th>\n</tr>\n</thead>\n""""
text = text + "<tbody>\n"
inhalt = Stufen(form.getvalue("kurs"),xmldoc)
for i in inhalt:
    if zaehler == 6:
        text = text + "</tr>\n"
        zaehler = 1
    if zaehler == 1:
        text = text + "<tr>\n"
    if zaehler <= 6:
        text = text + "<th>" + i + "</th>\n"
    zaehler += 1
text = text + "</tr>\n</tbody>\n</table>\n"
text = text + "</body>\n"
text = text + "</html>"
print(text)


            
