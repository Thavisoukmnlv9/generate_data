import json
import os

folder_name = "data/machine"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("data/machine/updated_data.json", "r", encoding="utf-8") as updated_data_file:
    updated_data = json.load(updated_data_file)

with open("data/machine/machine_data_new_value.json", "r", encoding="utf-8") as machine_data_file:
    machine_data = json.load(machine_data_file)

id_mapping = {item["number"]: item["id"] for item in machine_data["results"]}

formatted_data = []

for row in updated_data["rows"]:
    bil_seller = row["bil_seller"]
    id_from_machine_data = id_mapping.get(bil_seller, None)

    existing_item = next((item for item in formatted_data if item["number"] == bil_seller), None)

    if existing_item:
        existing_item["id"] = id_from_machine_data if id_from_machine_data is not None else row["id"]
    else:
        formatted_item = {
            "id": id_from_machine_data if id_from_machine_data is not None else row["id"],
            "number": bil_seller,
        }
        formatted_data.append(formatted_item)

formatted_data_filename = os.path.join(folder_name, "machine_number.json")

with open(formatted_data_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)

print(f"Formatted data has been written to {formatted_data_filename}.")
