import requests

# url = "https://hackatime.hackclub.com/api/v1/users/U0829HRSQ76/trust_factor"
# url = "https://hackatime.hackclub.com/api/v1/users/U0829HRSQ76/trust_factor"
# url = "https://hackatime.hackclub.com/api/hackatime/v1/users/current/statusbar/today"
# U081C6XT885
# url = "https://hackatime.hackclub.com/api/hackatime/v1/users/U097HMQUH1N/statusbar/today"

# url = "https://hackatime.hackclub.com/api/v1/users/my/stats"
# url = "https://hackatime.hackclub.com/api/v1/users/current/statusbar/today"
# U097HMQUH1N
# url = "https://hackatime.hackclub.com/api/v1/users/U097HMQUH1N/trust_factor"
# url = "https://hackatime.hackclub.com/api/v1/users/U097HMQUH1N/statusbar/today"
url = "https://hackatime.hackclub.com/api/v1/users/current/statusbar/today"

headers = {
    "Authorization": "Bearer dbf9cad2-6c1e-4f9d-aea1-322a6e9f19da"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  
    print(data)
else:
    print("Error:", response)