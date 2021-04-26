import csv
import json
from time import time

start = time()


def make_json(csv_path):
    data = []

    counter = 0

    with open(csv_path, encoding='utf-8-sig') as csvp:
        csv_reader = csv.DictReader(csvp)

        for row in csv_reader:
            row_items = list(row.items())
            for k, v in row_items:
                if v == "":
                    del row[k]

            data.append(row)
            counter += 1

            if counter%10 == 0:
                print(f'{counter} is multiple of 10')

    print(len(data))

    output = {
        "test": data
    }

    with open(json_path, 'w', encoding='utf-8-sig') as jsonp:
        jsonp.write(json.dumps(data, indent=2))


csv_path = r'random.csv'
json_path = r'random_batch.json'

make_json(csv_path)

print(f'Time taken to run: {time() - start} seconds')