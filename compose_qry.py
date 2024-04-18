"""
This module modifies existing SPARQL queries 
- to retrieve relevant EUROVOC concepts in legal in-force documents
- to retrieve other relevant documents
"""
import os

eurovoc_codes = ['3030', '3231', '3236', 'c_65b9cd79']
# reference: https://publications.europa.eu/webapi/rdf/sparql?default-graph-uri=&query=prefix+cdm%3A+%3Chttp%3A%2F%2Fpublications.europa.eu%2Fontology%2Fcdm%23%3E%0D%0Aprefix+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0Aprefix+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0Aselect+distinct+%3Fconcept+%3Fidentifier+%3Fpreflabel+%3Faltlabel%0D%0AGROUP_CONCAT%28DISTINCT+%3Fbroader%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Fbroaders%0D%0AGROUP_CONCAT%28DISTINCT+%3Fnarrower%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Fnarrowers%0D%0AGROUP_CONCAT%28DISTINCT+%3FisTopConceptOf%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3FisTopConceptOfs%0D%0AGROUP_CONCAT%28DISTINCT+%3Frelated%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Frelateds%0D%0Awhere+%7B+graph+%3Chttp%3A%2F%2Feurovoc.europa.eu%2F100141%3E+%7B%0D%0A%3Fconcept+skos%3AprefLabel+%3Fpreflabel.%0D%0AFILTER+%28lang%28%3Fpreflabel+%29+%3D+%27en%27%29%0D%0AOPTIONAL%7B%0D%0A%3Fconcept+skos%3AaltLabel+%3Faltlabel.%0D%0AFILTER+%28lang%28%3Faltlabel+%29+%3D+%27en%27%29.%0D%0A%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Abroader+%3Fbroader.%7D%0D%0AUNION+%7B%3Fbroader+skos%3Anarrower+%3Fconcept.%7D%0D%0A%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Anarrower+%3Fnarrower.%7D%0D%0AUNION+%7B%3Fnarrower+skos%3Abroader+%3Fconcept.%7D%0D%0A%7D%0D%0AOPTIONAL%7B%3Fconcept+skos%3AtopConceptOf+%3FisTopConceptOf.%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Arelated+%3Frelated.%7D%0D%0AUNION%7B%3Frelated+skos%3Arelated+%3Fconcept.%7D%0D%0A%7D%0D%0A%3Fconcept+dc%3Aidentifier+%3Fidentifier.%0D%0A%7D%0D%0A%7D%0D%0A&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+
'''
 Artificial intelligence, 
 "c_65b9cd79" "artificial neural network"@en

How to collect relevant EUROVOC concepts?
- Artificial intelligence
- technology
- internet
- human
...

'''


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
    qry_name = os.path.basename(sql_path).replace('.rq', '_')

    if code:
        sparql_query = change_eurovoc(sql_path, code)
    else:
        with open(sql_path, 'r') as file: 
            sparql_query = file.read()
        
    return sparql_query, qry_name