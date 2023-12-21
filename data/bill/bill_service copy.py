import json
import os
import requests

def post_bill_data(api_url, bill_data):
    """
    Posts bill data to the specified API endpoint.

    Parameters:
        - api_url (str): The URL of the API endpoint.
        - bill_data (dict): The bill data to be posted.

    Returns:
        - dict: The response from the API.
    """
    response = requests.post(api_url, json=bill_data)
    return response.json()

def main():
    folder_name = "data/bill"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open("data/bill/bill.json", "r", encoding="utf-8") as data_file:
        original_data = json.load(data_file)

    api_url = "http://localhost:8000/api/v1/bill"

    for row in original_data["rows"]:
        bil_seller = row["bil_seller"]
        machine_id_counter = {}

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

        response = post_bill_data(api_url, formatted_item)

        if response.get("status") == "success":
            print(f"Record with id {row['id']} has been successfully sent to {api_url}.")
        else:
            print(f"Failed to send record with id {row['id']}. Response: {response}")

    print("Streaming data completed.")

if __name__ == "__main__":
    main()
