from bs4 import BeautifulSoup
import requests
import sys

def safestr(data):
    if sys.version_info.major == 3:
        return str(data)
    if sys.version_info.major == 2:
        return unicode(data)

def scrap_description(page_data):
    datadiv = page_data.find('div',attrs={"class":"view-app__description"})
    data_p = datadiv.p
    datastring = ""
    for child in data_p.children:
        if safestr(child) == "<br/>":
            datastring += '\n'
        else:
            datastring += safestr(child)
    return datastring

def scrap_data(page_data,search_string):
    datadiv = page_data.find('div',attrs={"class":"popup__content popup__content--app-info"})
    datatable = datadiv.table
    v = None

    for row in datatable.findAll("tr"):
        cells = row.findAll("td")
        if cells[0].string == search_string:
            v = safestr(cells[1].string)
            break
    return v

def scrap_app_version(page_content):
    return scrap_data(page_content,"Version: ")

def scrap_app_name(page_content):
    return scrap_data(page_content,"App Name: ")

def scrap_app_releasedate(page_content):
    return scrap_data(page_content,"Release date: ")

def scrap_app_nbdownloads(page_content):
    return scrap_data(page_content,"Number of downloads: ")

def scrap_app(page):
    page_content = BeautifulSoup(page.content, "html.parser")

    version = scrap_app_version(page_content)
    name = scrap_app_name(page_content)
    rdate = scrap_app_releasedate(page_content)
    nbdownloads = scrap_app_nbdownloads(page_content)
    description = scrap_description(page_content)
    return name,version,nbdownloads,rdate,description

