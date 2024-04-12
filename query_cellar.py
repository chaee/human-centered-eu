import os
import json
import pandas as pd
from datetime import datetime
from SPARQLWrapper import SPARQLWrapper, JSON, POST

from compose_qry import get_qry

def request_query(sparql_query):
    """
    Send the given sparql_query to the EU Sparql endpoint
    and retrieve and return the results in JSON format.

    :param sparql_query: str
    :return: json dict
    """
    # sparql_query = "r'" + sparql_query + "'"
    # print('QUERY:', sparql_query)

    endpoint = "http://publications.europa.eu/webapi/rdf/sparql" # 2020-06-12 THIS

    ## USING SPARQLWrapper
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(sparql_query)
    sparql.setMethod(POST)
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    # print('RESULTS:', results)

    return results


# sparql_query, qry_name = get_qry()
# print('SPARQL_QUERY:', sparql_query)
sql_path = 'queries/sparql_queries/all_eurovoc_concepts.rq'
qry_name = os.path.basename(sql_path)

with open(sql_path, 'r') as file: 
    sparql_query = file.read()
    print('SPARQL_QUERY:', sparql_query)

sparql_query_results = request_query(sparql_query)

# Output SPARQL results to file
sparql_query_results_dir = "queries/sparql_query_results/"
os.makedirs(os.path.dirname(sparql_query_results_dir), exist_ok=True)

timestamp = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
sparql_query_results_file = sparql_query_results_dir + qry_name + timestamp + ".json"
#to_json_output_file(sparql_query_results_file, sparql_query_results)
with open(sparql_query_results_file, 'w') as outfile:
        # print('JSON_DUMPS:', json.dumps(data))
        json.dump(sparql_query_results, outfile, indent=4)
