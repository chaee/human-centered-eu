"""
This module contains functions for sending SPARQL queries to the EU Sparql endpoint
and retrieving the results in JSON format.
"""

import os
import json
import pandas as pd
from datetime import datetime
from SPARQLWrapper import SPARQLWrapper, JSON, POST
from compose_qry import get_qry


def send_request(sparql_query):
    """
    Send the given sparql_query to the EU Sparql endpoint
    and retrieve and return the results in JSON format.

    :param sparql_query: str
    :return: json dict
    """
    # sparql_query = "r'" + sparql_query + "'"
    # print('QUERY:', sparql_query)

    endpoint = "http://publications.europa.eu/webapi/rdf/sparql" # 2024-04-12 valid

    ## USING SPARQLWrapper
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(sparql_query)
    sparql.setMethod(POST)
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    # print('RESULTS:', results)

    return results


# print('SPARQL_QUERY:', sparql_query)

# sql_path = 'queries/sparql_queries/all_eu_treaties.rq'

#sql_path = '/Users/yun/Dev/humanet3/human-centered-eu/queries/sparql_queries/legal-in-force-EUROVOC.rq'
#sql_path = get_qry(sql_path)



def to_json_cellar_response(query_type, eurovoc_code):
    sparql_query, qry_name = get_qry(query_type, eurovoc_code)

    if eurovoc_code:
        qry_name = qry_name + eurovoc_code + '_'

    print('SPARQL_QUERY:', sparql_query)

    # Output SPARQL results to file
    sparql_query_results_dir = "queries/sparql_query_results/"
    os.makedirs(os.path.dirname(sparql_query_results_dir), exist_ok=True)
    timestamp = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
   
    sparql_query_results_file = sparql_query_results_dir + qry_name + timestamp + ".json"
    doctype = sparql_query_results_file.split('/')[-1].split('_')[0]

    sparql_query_results = send_request(sparql_query)

    #to_json_output_file(sparql_query_results_file, sparql_query_results)
    with open(sparql_query_results_file, 'w') as outfile:
        # print('JSON_DUMPS:', json.dumps(data))
        json.dump(sparql_query_results, outfile, indent=4)
    

    return sparql_query_results_file, doctype