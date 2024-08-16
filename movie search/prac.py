import requests

url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjMyY2QwMzAyYTA1MTEzYjg1OWI0ZDlmM2UzNzhlZCIsInN1YiI6IjY1YTBkOTQ3ZDIwN2YzMDEyZWU3NTVlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TX_GFUfpwZLnWdOM3xk1gj4N6AyQiRpyx9Hk8l_ZB8w"
}

response = requests.get(url, headers=headers)

data = response.json()
print(data)