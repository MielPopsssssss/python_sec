import requests

url = "https://example.com/page"

# Send a GET request to the URL
response = requests.get(url)

# Check for the presence of innocuous tags in the response
if "innocuous_tag1" in response.text and "innocuous_tag2" in response.text:
    # Prepare payload for POST request
    payload = {"param1": "value1", "param2": "value2"}

    # Send a POST request with the payload
    exploit_response = requests.post(url, data=payload)

    # Check if the payload is present in the exploit response
    if "payload" in exploit_response.text:
        print("Payload successfully returned on the page")
    else:
        print("Payload not found on the page")
else:
    print("Innocuous tags not found in the response")
