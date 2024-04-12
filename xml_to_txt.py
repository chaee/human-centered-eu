from lxml import etree

def extract_text(node):
        if node is None:
            return ""

        text = node.text if node.text else ""
        if node.tail:
            text += node.tail
        for child in node:
            text += extract_text(child)

        return text
    

def write_text_to_file(text, text_file_path):
    with open(text_file_path, 'w') as file:
        texts = text.split("\n")
        text = '\n'.join([text for text in texts if text.strip() != ""])
        file.write(text) 


def parse_xml(xml_file_path, text_file_path):
    with open(xml_file_path, 'rb') as file:
        data = file.read()
        
    tree = etree.fromstring(data)
    text = extract_text(tree)
    return write_text_to_file(text, text_file_path)