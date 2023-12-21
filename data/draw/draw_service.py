import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

base_url = os.getenv("API_ENDPOINT")
token = os.getenv("TOKEN")

def post_draw_data(formatted_draw):
    api_url = f"{base_url}/draw"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.post(api_url, json=formatted_draw, headers=headers)
    print("Response Status Code:", response.status_code)

    if response.status_code == 201:
        print(
            f"Ticket with id {formatted_draw['id']} has been successfully sent to {api_url}."
        )
        return True
    else:
        print(
            f"Failed to send draw with id {formatted_draw['id']}. Response: {response.text}"
        )
        return False



def main():
    folder_name = "data/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(
        "data/draw/draw.json", "r", encoding="utf-8"
    ) as draw_file:
        draw_data = json.load(draw_file)

    for draw in draw_data:
        formatted_draw = {
            "id": draw["id"],
            "drawName": draw["drawName"],
            "startDate": draw["startDate"],
            "startDate": draw["startDate"],
            "randomTime": draw["randomTime"],
            "isActive": draw["isActive"],
            "prizeGroup": draw["prizeGroup"],
        }
        if not post_draw_data(formatted_draw):
            break
    print("Streaming draw data completed.")

if __name__ == "__main__":
    main()