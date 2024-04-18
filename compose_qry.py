"""
This module modifies existing SPARQL queries 
- to retrieve relevant EUROVOC concepts in legal in-force documents
- to retrieve other relevant documents
"""
import os



def change_eurovoc(sql_path, code):
    '''
    replace eurovoc code within SPARQL query that varies based on the eurovoc code
    '''
    with open(sql_path, 'r') as file: 
        sparql_query = file.read()
        print('SPARQL_QUERY:', sparql_query)
        sparql_query = sparql_query.replace('EUROVOC_CODE', code)
        print('SPARQL_QUERY:', sparql_query)
    return sparql_query


def get_qry(query_name, code=None):
    '''
    Choose the type of query in sparql_queries folder
    - all-eurovoc-concepts: retrieve all EUROVOC concepts
    - all-eu-treaties: retrieve all EU treaties
    - legal-in-force-EUROVOC: retrieve all EU legislation in force using EUROVOC concepts
    '''

    sql_path = '/Users/yun/Dev/humanet3/human-centered-eu/queries/sparql_queries/' + query_name
    qry_name = os.path.basename(sql_path).replace('.rq', '-')

    if code:
        sparql_query = change_eurovoc(sql_path, code)
    else:
        with open(sql_path, 'r') as file: 
            sparql_query = file.read()
        
    return sparql_query, qry_name