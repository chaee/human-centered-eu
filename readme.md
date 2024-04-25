# Human-centrism in EU legal documents 

## Project
For the human-centrism project by [Humanet3](https://humanet3.mpg.de) group, we aim to investigate how the concept of human-centrism is reflected and used in public domain in EU. For this purpose, we are collecting relevant documents from [EU Cellar](https://op.europa.eu/en/publication-detail/-/publication/658088eb-c071-11e8-9893-01aa75ed71a1/language-en/format-PDF/source-76875949) (The semantic repository of the Publications Office). Our keywords of interest include human-centered AI, internet, and digital transformation. 
   
For further project description and the concept of Humanet3, please refer to our [webpage](https://humanet3.mpg.de/concept/).

## Scripts
The project is work in progress. The repository consists of scripts  
- collecting documents from EU Cellar and process into human-readable text 
- saving retrieved files in a structured way based on the type of query and EUROVOC keyword for further use   
- conducting text analysis on the collected documents  

So far, all EU treaties and EU legislations in force about several EUROVOC concepts including AI have been collected.

## File structure
📦human-centered-eu   
 ┣ 📂analyses  
 ┃ ┗ 📜human_concordance.txt   
 ┣:**✨📂concat_results**✨   
 ┃ ┣ 📜all-eu-treaties-20240418-162444.txt   
 ┃ ┣ 📜legal-in-force-EUROVOC-3030.txt  
 ┃ ┣ 📜legal-in-force-EUROVOC-3231.txt  
 ┃ ┣ 📜legal-in-force-EUROVOC-5188.txt  
 ┃ ┗ 📜legal-in-force-EUROVOC-5333.txt  
 ┣ 📂queries  
 ┃ ┣ 📂sparql_queries :sparkles:*SPARQL queries for certain task*  
 ┃ ┃ ┣ 📜all-eu-leg-in-force.rq :sparkles:*all EU legislations in force (WIP)*  
 ┃ ┃ ┣ 📜all-eu-treaties.rq :sparkles:*all EU treaties*  
 ┃ ┃ ┣ 📜all-eurovoc-concepts.rq :sparkles:*EU legislations in force about certain EUROVOC concept*  
 ┃ ┃ ┗ 📜legal-in-force-EUROVOC.rq  
 ┃ ┗ 📂sparql_query_results :sparkles:*saves the query result in .json*
 ┃ ┃ ┣ 📜all-eu-treaties-20240418-162253.json  
 ┃ ┃ ┣ 📜all-eu-treaties-20240418-162444.json  
 ┃ ┃ ┣ 📜all-eu-treaties_20240412-145449.json  
 ┃ ┃ ┣ 📜all-eurovoc-concepts_20240412-144328.json  
 ┃ ┃ ┣ 📜curl_command.txt  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-3030_20240418-155200.json :sparkles:*naming convention: type of query - EUROVOC identifier - querying date and time*  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-3030_20240418-160328.json  
 ...  
 ┃ ┃ ┣ 📜legal-in-force-EUROVOC-c_65b9cd79_20240418-160709.json  
 ┃ ┃ ┗ 📜query_results_20240412-121407.json  
 ┣ 📂txt_results :sparkles:*transforms xml file into readble text for each document*  
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
 ┣ 📜analyze.py :sparkles:*run text analysis on text files*  
 ┣ 📜compose_qry.py :sparkles:*modify SPARQL query*  
 ┣ 📜concatenate.py :sparkles:*concatenate files into one document based on the folder*  
 ┣ 📜curl_urls.py :sparkles:*send request urls (achieved by querying cellar) to the endpoint*  
 ┣ 📜eurovoc_concepts.csv :sparkles:*readible list of relevant EUROVOC conepts (WIP)*  
 ┣ 📜query_cellar.py :sparkles:*send SPARQL query to the Celar*  
 ┣ 📜run_together.py :sparkles:*query cellar - curl urls - format in one script*  
 ┗ 📜xml_to_txt.py :sparkles:*modify xml to txt*  
