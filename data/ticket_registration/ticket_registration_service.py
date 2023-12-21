import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

base_url = os.getenv("API_ENDPOINT")
token = os.getenv("TOKEN")


def post_ticket_registration_data(formatted_ticket_registration):
    api_url = f"{base_url}/ticket_registration"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.post(api_url, json=formatted_ticket_registration, headers=headers)
    print("Response Status Code:", response.status_code)

    try:
        response_data = response.json()
        print("Response Content:", response_data)
    except json.JSONDecodeError:
        print("Invalid JSON response")

    if response.status_code == 201:
        print(
            f"Ticket Registration has been successfully sent to {api_url}."
        )
        return True 
    else:
        print(
            f"Failed to send ticket_registration. Response: {response.text}"
        )
        return False




def main():
    folder_name = "ticket_registration/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open("data/ticket_registration/formatted_ticket_registration_data.json", "r", encoding="utf-8") as ticket_registration_file:
        ticket_registration_data = json.load(ticket_registration_file)

    for ticket_registration in ticket_registration_data:
        formatted_ticket_registration = {
            "ticket": ticket_registration["ticket"],
            "isDrawn": ticket_registration["isDrawn"],
            "draw": ticket_registration["draw"],
        }
        if not post_ticket_registration_data(formatted_ticket_registration):
            break
    print("Streaming ticket_registration data completed.")


if __name__ == "__main__":
    main()
