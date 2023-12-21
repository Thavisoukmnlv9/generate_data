import json
import os


folder_name = "data/ticket"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("data/ticket/formatted_bill_data.json", "r", encoding="utf-8") as data_file:
    original_data = json.load(data_file)

formatted_data = []


for row in original_data:
    formatted_item = {
    "id": row["id"],
    "ticketType": "SLOT",
      "entry_record_id": row["id"],
    "ticketStatus": "NOT_USED",
    }
    formatted_data.append(formatted_item)

formatted_data_filename = os.path.join(folder_name, "formatted_ticket_data.json")

with open(formatted_data_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)

print(f"Formatted data with updated phone numbers has been written to {formatted_data_filename}.")