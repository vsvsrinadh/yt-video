import requests

url = 'http://127.0.0.1:8000/download'
data = {
    'url': 'https://www.youtube.com/watch?v=your_video_id',
    'quality': 'best'
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
