import json
import os

folder_name = "data/machine"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

original_data_filename = os.path.join(folder_name, "bill.json")

with open(original_data_filename, "r", encoding="utf-8") as data_file:
    original_data = json.load(data_file)

formatted_data = original_data.copy()

new_id = 900
for row in formatted_data["rows"]:
    row["id"] = new_id
    new_id += 1
    row["candidate"]["id"] = int(str(900) + str(row["candidate"]["id"]))

formatted_data_json_filename = os.path.join(folder_name, "updated_data.json")
with open(formatted_data_json_filename, "w", encoding="utf-8") as formatted_data_file:
    json.dump(formatted_data, formatted_data_file, ensure_ascii=False, indent=4)

print(f"Formatted data has been written to {formatted_data_json_filename}.")


{
    "user": {
        "name": "admin",
        "email": "",
        "image": null,
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzMjQwODY3LCJpYXQiOjE3MDMxNTQ0NjcsImp0aSI6ImVjZDU0YTA1ODRjZDQyNDk4YzgzY2JmOTE2OGRmMDE5IiwidXNlcl9pZCI6MX0.wATxKXNvOtHGImKA3I5WPPK22RGPJ9D-0C-XCGwAjOc",
    },
    "expires": "2024-01-20T10:27:51.063Z",
}
