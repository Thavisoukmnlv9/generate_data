import json
import os
import requests

def post_data_to_api(api_url, formatted_item, token):
    """
    Posts formatted data to the specified API endpoint with authentication.

    Parameters:
        - api_url (str): The URL of the API endpoint.
        - formatted_item (dict): The data to be posted.
        - token (str): The authentication token.

    Returns:
        - dict: The response from the API.
    """
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    response = requests.post(api_url, json=formatted_item, headers=headers)
    return response.json()

def main():
    folder_name = "machine/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open("data/machine/formatted_data.json", "r", encoding="utf-8") as data_file:
        original_data = json.load(data_file)

    api_url = "http://localhost:8000/api/v1/machine"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzMTUxMTY1LCJpYXQiOjE3MDMwNjQ3NjUsImp0aSI6IjNlOTA0YzcxNjA1NjQzZDBhYjRiYzAyYzkxZGZkZTEyIiwidXNlcl9pZCI6MX0.pLxYFv7QRGprY7vjv4kQuTjlU2OEKLfRKShacjFixdI"

    for row in original_data:
        formatted_item = {
            "id": row["id"],
            "number": row["number"],
        }

        response = post_data_to_api(api_url, formatted_item, token)

        if response.get("status") == "success":
            print(f"Record with id {row['id']} has been successfully sent to {api_url}.")
        else:
            print(f"Failed to send record with id {row['id']}. Response: {response}")

    print("Streaming data completed.")

if __name__ == "__main__":
    main()
