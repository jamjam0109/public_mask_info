import csv

def dict_to_csv(dict_file, save_path):

    keys = dict_file[0].keys()

    with open(f'{save_path}', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict_file)