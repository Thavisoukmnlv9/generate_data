import json
import os

folder_name = "data/machine"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("data/machine/updated_data.json", "r", encoding="utf-8") as data_file:
    original_data = json.load(data_file)

formatted_data = []
machine_id_counter = set()

for row in original_data["rows"]:
    bil_seller = row["bil_seller"]
    if bil_seller not in machine_id_counter:
        machine_id_counter.add(bil_seller)
        formatted_item = {
            "id": row["id"],
            "number": bil_seller,
        }
        formatted_data.append(formatted_item)
formatted_data_filename = os.path.join(folder_name, f"{folder_name}.json")

formatted_data_json_filename = os.path.join(folder_name, "formatted_data.json")
with open(formatted_data_json_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)
    
print(f"Formatted data has been written to {formatted_data_json_filename}.")
