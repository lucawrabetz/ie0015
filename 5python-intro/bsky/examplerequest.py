import requests

endpoint_url = "https://httpbin.org/ip"
response = requests.get(endpoint_url)

if response.status_code == 200:
    data = response.json()  # Requests automatically converts JSON to a dictionary
    print("Endpoint Response (Dictionary):")
    print(
        data
    )  # Print the dictionary directly (less pretty, but illustrates the data structure)
    print(
        "\nNotice how this is a dictionary, with keys like 'origin' and their values."
    )
else:
    print(f"Error fetching from endpoint: Status Code: {response.status_code}")

website_url = "https://example.com"
response = requests.get(website_url)

if response.status_code == 200:
    html_content = response.text
    print("\nWebsite Response (HTML):")
    print(html_content)
    print("\nNotice how this is HTML code intended for a web browser to render.")
else:
    print(f"Error fetching from website: Status Code: {response.status_code}")
