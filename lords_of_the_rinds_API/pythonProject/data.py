import requests

lord_of_the_rings_endpoint = "https://the-one-api.dev/v2/quote"

headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer HeS5WfmIw5k7UOfqAM9R'
    }


response = requests.get(url=lord_of_the_rings_endpoint, headers=headers)
print(response.status_code)
data = response.json()
quote_in_dict = data["docs"]