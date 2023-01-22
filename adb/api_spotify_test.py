import requests

access_token = 'dd7fe34060af45b7a94dd4b10ba95dab'
headers = {'Authorization': 'Bearer ' + access_token}

response = requests.get('https://api.spotify.com/v1/me/tracks', headers=headers)

print(response)

##data = response.json()
##tracks = data["items"]

#https://accounts.spotify.com/authorize?client_id=dd7fe34060af45b7a94dd4b10ba95dab&response_type=code&redirect_uri=http://localhost:8000/callback&scope=user-library-read


