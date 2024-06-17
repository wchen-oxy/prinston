import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    json_array = []
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
            json_row = {
                "NDC": row[0],
                "description": row[1],
                "quantity": row[2],
                "form": row[3],
                "url": row[4],
                "category": row[5],
                "brand": row[6]
            }
            json_array.append(json_row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)


# Example usage:
csv_file_path = 'list.csv'  # Replace with your CSV file path
json_file_path = 'data.json'  # Replace with your desired JSON file path
csv_to_json(csv_file_path, json_file_path)
print(
    f"Conversion completed successfully! JSON file saved at {json_file_path}")
