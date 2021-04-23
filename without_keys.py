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

        # for row in csv_reader:
        #     row = {key: (None if value == "" else value) for key, value in
        #            row.items()}
        #
        #     data.append(row)

    with open(json_path, 'w', encoding='utf-8-sig') as jsonp:
        jsonp.write(json.dumps(data, indent=4))


csv_path = r'elearning Test Records_v2.csv'
json_path = r'elearning Test Records_v2.json'

make_json(csv_path, json_path)

print(f'Time taken to run: {time() - start} seconds')