import csv
import json
from time import time

start = time()


def make_json(csv_path, json_path):
    data = []

    with open(csv_path, encoding='utf-8-sig') as csvp:
        csv_reader = csv.DictReader(csvp)

        for row in csv_reader:
            row_items = list(row.items())
            for k, v in row_items:
                if v == "":
                    del row[k]

            data.append(row)

    output = {
        "test": data
    }

    with open(json_path, 'w', encoding='utf-8-sig') as jsonp:
        jsonp.write(json.dumps(output, indent=2))


csv_path = r'random55.csv'
json_path = r'elearning Test Records_v2_indent_test_01.json'

make_json(csv_path, json_path)

print(f'Time taken to run: {time() - start} seconds')