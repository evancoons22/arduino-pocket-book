import requests

def delete_messages():
    # Replace with the IP and port of your ESP8266 server
    url = "http://192.168.4.1/delete-messages"

    password = input("Enter the password to delete messages: ")

    # Sending the POST request
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data={'password': password}, headers = headers)
        if response.status_code == 200:
            print("Success: ", response.text)
        else:
            print("Error: ", response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)

if __name__ == "__main__":
    delete_messages()

