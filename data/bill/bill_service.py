import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

base_url = os.getenv("API_ENDPOINT")
token = os.getenv("TOKEN")


def post_bill_data(formatted_bill):
    api_url = f"{base_url}/bill"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.post(api_url, json=formatted_bill, headers=headers)
    print("Response Status Code:", response.status_code)

    if response.status_code == 201:
        print(
            f"Bill with id {formatted_bill['id']} has been successfully sent to {api_url}."
        )
        return True  # Indicate success
    else:
        print(
            f"Failed to send bill with id {formatted_bill['id']}. Response: {response.text}"
        )
        return False



def main():
    folder_name = "bill/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open("data/bill/formatted_bill_data.json", "r", encoding="utf-8") as bill_file:
        bill_data = json.load(bill_file)

    for bill in bill_data:
        formatted_bill = {
            "id": bill.get("id", ""),
            "billNumber": bill.get("billNumber", ""),
            "totalCost": bill.get("totalCost", ""),
            "entryRecord": {
                "type": "BILL",
                "id": bill["entryRecord"].get("id", ""),
                "participant": bill["entryRecord"].get("participant", ""),
            },
            "machine": bill.get("machine", ""),
        }
        if not post_bill_data(formatted_bill):
            break
    print("Streaming bill data completed.")


if __name__ == "__main__":
    main()
