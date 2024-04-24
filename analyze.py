from io import StringIO
import os
import sys
from contextlib import redirect_stdout
import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt')

def search_word_with_context(file_path, target_word, context_size, output_file):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Create an NLTK Text object for efficient search and concordance
    text_object = nltk.Text(words)
    con_list = text_object.concordance_list(target_word, width=context_size*2)
    text_object.concordance(target_word, width=context_size*2)
        # Write the output to the specified file or print to console
    if output_file:
        with open(output_file, 'w') as f:
            for con_item in con_list:
                f.write(f'{con_item.line}\n')
                # f.write(f'{" ".join(con_item.left)} {con_item.query} {" ".join(con_item.right)}\n') 
            # f.write('\n'.join(con_list))
    else:
        print(con_list)


# Example usage
#file_path = 'txt_results/all-eu-treaties-20240418-162444/2bf140bf-a3f8-4ab2-b506-fd71826e6da6.txt'  # Replace with the path to your text file
file_path = 'concat_results/all-eu-treaties.txt'
output_file = 'analyses/human_concordance.txt'  # Specify the output file name
target_word = 'human'  # Replace with the word you want to search for
context_size = 50
search_word_with_context(file_path, target_word, context_size, output_file)
