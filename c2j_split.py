import csv
import json
from time import time

start = time()


def make_json(csv_path):
    data = []

    with open(csv_path, encoding='utf-8-sig') as csvp:

        csv_reader = csv.DictReader(csvp)

        for row in csv_reader:
            row_items = list(row.items())
            for k, v in row_items:
                if v == "":
                    del row[k]

            data.append(row)

    data_extra = len(data) - len(data) // 10 * 10
    remaining = data[-data_extra:]

    loop = 0

    for i in range(len(data) // 10):

        output = {"items": data[10 * i:10 * (i + 1)]}

        json_path = rf"--{csv_path} - {i}0's.json"

        with open(json_path, 'w', encoding='utf-8-sig') as jsonp:
            jsonp.write(json.dumps(output, indent=2))

    if data_extra != 0:

        for i in range(len(remaining)):

            output = {"items": remaining[10 * i:10 * (i + 1)]}

            json_path = rf"--{csv_path} - remaining {len(remaining)}.json"

            with open(json_path, 'w', encoding='utf-8-sig') as jsonp:
                jsonp.write(json.dumps(output, indent=2))

            if loop == 0:
                break


csv_path = r'random114.csv'
make_json(csv_path)

print(f'Time taken to run: {time() - start} seconds')