import requests

token = 'ABCDREFG123456789'

res = requests.get('http://192.168.2.136:8000/api/v1/check-token/',
                    headers={"User-Agent": "Mozilla/5.0 "
                                     "(Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/96.0.4664.110 Safari/537.36",
                        "Authorization": f"Bearer {token}",
                        "FUCKINGSHIT": "shit-post"
                       })

print(res.text)