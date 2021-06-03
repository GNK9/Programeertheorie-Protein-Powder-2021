import csv

def output(configuration):
    """
    Output protein configuration to csv
    input: [{Amino-acid: position}...]
    output: CSV
    """
    with open('C:/Users/Ali/Desktop/Programeertheorie-Protein-Powder-2021/code/output/output.csv', newline="", mode='w') as output_file:
        headers = ['amino','fold']
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow(headers)
        [writer.writerow(row) for row in configuration]

# TEST CODE
output([('H', '0'), ('P', '-1'), ('P', '-1'), ('score', '-2')])