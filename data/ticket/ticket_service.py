import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

base_url = os.getenv("API_ENDPOINT")
token = os.getenv("TOKEN")

def post_ticket_data(formatted_ticket):
    api_url = f"{base_url}/ticket"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.post(api_url, json=formatted_ticket, headers=headers)
    print("Response Status Code:", response.status_code)

    if response.status_code == 201:
        print(
            f"Ticket with id {formatted_ticket['id']} has been successfully sent to {api_url}."
        )
        return True
    else:
        print(
            f"Failed to send ticket with id {formatted_ticket['id']}. Response: {response.text}"
        )
        return False




def main():
    folder_name = "ticket/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open("data/ticket/formatted_ticket_data.json", "r", encoding="utf-8") as ticket_file:
        ticket_data = json.load(ticket_file)

    for ticket in ticket_data:
        formatted_ticket = {
            "id": ticket.get("id", ""),
            "ticketType": ticket.get("ticketType", ""),
            "entry_record_id": ticket.get("entry_record_id", ""),
            "ticketStatus": ticket.get("ticketStatus", ""),
        }
        if not post_ticket_data(formatted_ticket):
            break
    print("Streaming ticket data completed.")


if __name__ == "__main__":
    main()
