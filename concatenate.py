import os

def concatenate_text_files(folder_path, output_file):
    concatenated_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                concatenated_text += file.read() + "\n"
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the concatenated text to the output file
    with open(output_file, 'w') as output:
        output.write(concatenated_text)

for folders in os.listdir('txt_results'):
    folder_path = os.path.join('txt_results', folders)  # Replace with the path to input folder
    output_file = os.path.join('concat_results', os.path.basename(folder_path) + '.txt')
    concatenate_text_files(folder_path, output_file)