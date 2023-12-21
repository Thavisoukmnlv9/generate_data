import json
import os

folder_name = "data/participant"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("data/participant/formatted_participant_data.json", "r", encoding="utf-8") as participant_file:
        participant_data = json.load(participant_file)


formatted_data = []

for entry in participant_data:
    original_phone_number = entry["phoneNumber"]
    formatted_phone_number = f"20{original_phone_number[-8:]}"
    entry["phoneNumber"] = formatted_phone_number
    formatted_data.append(entry)

formatted_data_filename = os.path.join(folder_name, "formatted_participant_data.json")

with open(formatted_data_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)

print(f"Formatted data with updated phone numbers has been written to {formatted_data_filename}.")