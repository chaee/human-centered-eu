from query_cellar import to_json_cellar_response
from curl_urls import extract_urls, request_urls

eurovoc_codes = ['3030', '3231', '3236', 'c_65b9cd79']
# reference: https://publications.europa.eu/webapi/rdf/sparql?default-graph-uri=&query=prefix+cdm%3A+%3Chttp%3A%2F%2Fpublications.europa.eu%2Fontology%2Fcdm%23%3E%0D%0Aprefix+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0Aprefix+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0Aselect+distinct+%3Fconcept+%3Fidentifier+%3Fpreflabel+%3Faltlabel%0D%0AGROUP_CONCAT%28DISTINCT+%3Fbroader%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Fbroaders%0D%0AGROUP_CONCAT%28DISTINCT+%3Fnarrower%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Fnarrowers%0D%0AGROUP_CONCAT%28DISTINCT+%3FisTopConceptOf%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3FisTopConceptOfs%0D%0AGROUP_CONCAT%28DISTINCT+%3Frelated%3B+separator%3D%22%3B%5Cr%5Cn%22%29+AS+%3Frelateds%0D%0Awhere+%7B+graph+%3Chttp%3A%2F%2Feurovoc.europa.eu%2F100141%3E+%7B%0D%0A%3Fconcept+skos%3AprefLabel+%3Fpreflabel.%0D%0AFILTER+%28lang%28%3Fpreflabel+%29+%3D+%27en%27%29%0D%0AOPTIONAL%7B%0D%0A%3Fconcept+skos%3AaltLabel+%3Faltlabel.%0D%0AFILTER+%28lang%28%3Faltlabel+%29+%3D+%27en%27%29.%0D%0A%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Abroader+%3Fbroader.%7D%0D%0AUNION+%7B%3Fbroader+skos%3Anarrower+%3Fconcept.%7D%0D%0A%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Anarrower+%3Fnarrower.%7D%0D%0AUNION+%7B%3Fnarrower+skos%3Abroader+%3Fconcept.%7D%0D%0A%7D%0D%0AOPTIONAL%7B%3Fconcept+skos%3AtopConceptOf+%3FisTopConceptOf.%7D%0D%0AOPTIONAL%7B%0D%0A%7B%3Fconcept+skos%3Arelated+%3Frelated.%7D%0D%0AUNION%7B%3Frelated+skos%3Arelated+%3Fconcept.%7D%0D%0A%7D%0D%0A%3Fconcept+dc%3Aidentifier+%3Fidentifier.%0D%0A%7D%0D%0A%7D%0D%0A&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+
'''
 Artificial intelligence, 
 "c_65b9cd79" "artificial neural network"@en

How to collect relevant EUROVOC concepts?
- 3030: Artificial intelligence
- 3231 information and information processing
- 3236 information technology and data processing
- c_65b9cd79 artificial neural network
- 5188 information technology
- "5333" "impact of information technology"@en
- technology
- internet
- human
...
'''

query_types = ['all-eurovoc-concepts.rq', 'all-eu-treaties.rq', ('legal-in-force-EUROVOC.rq', '5333'), 'all-eu-leg-in-force.rq', 'intl-agreements.rq']

query_type = query_types[4]

if isinstance(query_type, tuple):
    query_type, eurovoc_code = query_type[0], query_type[1]
else:
    eurovoc_code = None

json_path, doctype = to_json_cellar_response(query_type, eurovoc_code)
#json_path = 'queries/sparql_query_results/legal-in-force-EUROVOC-3030_20240418-155200.json'

urls = extract_urls(json_path)#, doctype)
request_urls(urls, doctype)  