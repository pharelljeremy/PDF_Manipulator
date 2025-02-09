def get_file_list(prompt):
    files = input(prompt).split(',')
    return [file.strip() for file in files]

def get_output_file(prompt):
    return input(prompt).strip()

def get_output_file(prompt):
    output = input(prompt).strip()
    if not output.endswith('.pdf'):
        output += '.pdf'
    return output