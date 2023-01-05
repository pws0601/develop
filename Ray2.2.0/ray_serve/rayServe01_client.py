import requests

english_text = "Hello world!"

response = requests.post("http://localhost:8000", json=english_text)
french_text = response.text

print(french_text)