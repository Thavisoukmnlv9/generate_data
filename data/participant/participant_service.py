import json
import os
import requests
from dotenv import load_dotenv


load_dotenv()

base_url = os.getenv("API_ENDPOINT")
token = os.getenv("TOKEN")

def post_participant_data(formatted_bill):
    api_url = f"{base_url}/participant"
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
    folder_name = "participant/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(
        "data/participant/formatted_participant_data.json", "r", encoding="utf-8"
    ) as participant_file:
        participant_data = json.load(participant_file)


    for participant in participant_data:
        formatted_participant = {
            "id": participant["id"],
            "fullName": participant["fullName"],
            "village": participant["village"],
            "phoneNumber": participant["phoneNumber"],
            "district": participant["district"],
            "updated_on": participant["updated_on"],
            "created_on": participant["created_on"],
        }
        # print(formatted_participant)
        if not post_participant_data(formatted_participant):
            break
    print("Streaming participant data completed.")


if __name__ == "__main__":
    main()