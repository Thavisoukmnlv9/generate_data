import json
import os
import requests

folder_name = "data/bill"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("data/bill/bill.json", "r", encoding="utf-8") as data_file:
    original_data = json.load(data_file)

formatted_data = []
machine_id_counter = {}

for row in original_data["rows"]:
    bil_seller = row["bil_seller"]
    if bil_seller in machine_id_counter:
        machine_id = machine_id_counter[bil_seller]
    else:
        machine_id_counter[bil_seller] = row["id"]
        machine_id = row["id"]

    formatted_item = {
        "id": row["id"],
        "billNumber": row["bil_number"],
        "totalCost": row["bil_price"],
        "entryRecord": {
            "type": "BILL",
            "id": row["id"],
            "participant": row["candidate"]["id"]
        },
        "machine": machine_id
    }
    formatted_data.append(formatted_item)

formatted_data_filename = os.path.join(folder_name, "formatted_bill_data.json")

with open(formatted_data_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)

print(f"Formatted data with machine_id has been written to {formatted_data_filename}.")