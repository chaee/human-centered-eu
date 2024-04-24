# Collecting legal documents from EU by quering EU Cellar (The semantic repository of the Publications Office)  
## File structure
📦human-centered-eu   
 ┣ 📂analyses  
 ┃ ┗ 📜human_concordance.txt   
 ┣:**📂concat_results**:sparkles:  
 ┃ ┣ 📜all-eu-treaties-20240418-162444.txt   
 ┃ ┣ 📜legal-in-force-EUROVOC-3030.txt  
 ┃ ┣ 📜legal-in-force-EUROVOC-3231.txt  
 ┃ ┣ 📜legal-in-force-EUROVOC-5188.txt  
 ┃ ┗ 📜legal-in-force-EUROVOC-5333.txt  
 ┣ 📂queries  
 ┃ ┣ 📂sparql_queries :sparkle:*SPARQL queries for certain task*  
 ┃ ┃ ┣ 📜all-eu-leg-in-force.rq :sparkle:*all EU legislations in force (WIP)*  
 ┃ ┃ ┣ 📜all-eu-treaties.rq :sparkle:*all EU treaties*  
 ┃ ┃ ┣ 📜all-eurovoc-concepts.rq :sparkle:*EU legislations in force about certain EUROVOC concept*  
 ┃ ┃ ┗ 📜legal-in-force-EUROVOC.rq  
 ┃ ┗ 📂sparql_query_results :sparkle:*saves the query result in .json :sparkle:*  
 ┃ ┃ ┣ 📜all-eu-treaties-20240418-162253.json  
 ┃ ┃ ┣ 📜all-eu-treaties-20240418-162444.json  
 ┃ ┃ ┣ 📜all-eu-treaties_20240412-145449.json  
 ┃ ┃ ┣ 📜all-eurovoc-concepts_20240412-144328.json  
 ┃ ┃ ┣ 📜curl_command.txt  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-3030_20240418-155200.json :sparkle:*naming convention: type of query - EUROVOC identifier - querying date and time*  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-3030_20240418-160328.json  
 ...  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-c_65b9cd79_20240418-160709.json  
 ┃ ┃ ┗ 📜query_results_20240412-121407.json  
 ┣ 📂txt_results :sparkle:*transforms xml file into readble text for each document*  
 ┃ ┣ 📂all-eu-treaties-20240418-162444  
 ┃ ┃ ┣ 📜00348c0c-c2c0-413b-b0d9-ca6519907f9d.txt  
...  
 ┃ ┣ 📂legal-in-force-EUROVOC-3030  
 ┃ ┃ ┣ 📜06d23b63-cae0-11ee-95d9-01aa75ed71a1.txt  
 ...  
 ┃ ┣ 📂legal-in-force-EUROVOC-3231  
 ┃ ┃ ┣ 📜008a44b9-990f-11e7-b92d-01aa75ed71a1.txt  
...  
 ┃ ┣ 📂legal-in-force-EUROVOC-5188  
 ┃ ┃ ┣ 📜00e7ffec-49e3-492b-8e8e-8839cae806bc.txt  
...  
 ┃ ┗ 📂legal-in-force-EUROVOC-5333  
 ┃ ┃ ┗ 📜28907e25-7c65-11e9-9f05-01aa75ed71a1.txt  
 ┣ 📜analyze.py :sparkle:*run text analysis on text files*  
 ┣ 📜compose_qry.py :sparkle:*modify SPARQL query*  
 ┣ 📜concatenate.py :sparkle:*concatenate files into one document based on the folder*  
 ┣ 📜curl_urls.py :sparkle:*send request urls (achieved by querying cellar) to the endpoint*  
 ┣ 📜eurovoc_concepts.csv :sparkle:*readible list of relevant EUROVOC conepts (WIP)*  
 ┣ 📜query_cellar.py :sparkle:*send SPARQL query to the Celar*  
 ┣ 📜run_together.py :sparkle:*query cellar - curl urls - format in one script*  
 ┗ 📜xml_to_txt.py :sparkle:*modify xml to txt*  
