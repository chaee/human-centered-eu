import csv
import csv
import requests
from xml_to_txt import parse_xml
import subprocess
import os
import json
import requests

# read urls from the query result csv file
urls = []
json_path = 'queries/sparql_query_results/query_results_20240412-121407.json' # change file name to query keyword instead of dates
json_file_name = os.path.basename(json_path)

with open(json_path, 'r') as file:
    data = json.load(file)
    # Extract the URL
    for result in data['results']['bindings']:
        url = result['work']['value']
        print(url)
        urls.append(url)

# curl those urls and get xmls
xml_responses = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://publications.europa.eu/webapi/rdf/sparql?default-graph-uri=&query=prefix+cdm%3A+%3Chttp%3A%2F%2Fpublications.europa.eu%2Fontology%2Fcdm%23%3E%0D%0Aselect+distinct%3Fwork%0D%0Awhere%0D%0A%7B%0D%0A%3Fwork+cdm%3Aresource_legal_in-force+%22true%22%5E%5E%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23boolean%3E+%3B%0D%0Aa+cdm%3Alegislation_secondary%3B%0D%0Acdm%3Awork_is_about_concept_eurovoc+%3Chttp%3A%2F%2Feurovoc.europa.eu%2F3030%3E+.%0D%0A%7D&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


for url in urls:
    response = requests.get(url, headers=headers)

    doc_key = url.split('/')[-1]
    xml_file_path = os.path.join('xml_results', doc_key + '.xml')
    text_file_path = os.path.join('txt_results', doc_key + '.txt')

    # Create the 'xml_results' folder if it doesn't exist
    if not os.path.exists('xml_results'):
        os.makedirs('xml_results')
    if not os.path.exists('txt_results'):
        os.makedirs('txt_results')
    with open(xml_file_path, 'w') as file:
        file.write(response.text)

    parse_xml(xml_file_path, text_file_path)