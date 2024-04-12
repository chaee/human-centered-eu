import os

def compose_qry():
      

      return


def get_qry():
    sql_path = 'queries/sparql_queries/legal_in-force_EUROVOC.rq'
    qry_name = os.path.basename(sql_path)

    with open(sql_path, 'r') as file: 
        sparql_query = file.read()
        print('SPARQL_QUERY:', sparql_query)
        sparql_query = sparql_query.replace('EUROVOC_CODE', '3231')
        print('SPARQL_QUERY:', sparql_query)
    return sparql_query, qry_name

get_qry()