print("\nImportação e uso de um moódulo externo")
import requests

url = "https://www.examle.com"
response = requests.get(url)
print(f"Status code: {response.status_code}")