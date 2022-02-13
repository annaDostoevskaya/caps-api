'''
import requests

res = requests.post('http://192.168.2.136:8000/posting-data/',
              headers={"User-Agent": "Mozilla/5.0 "
                                     "(Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/96.0.4664.110 Safari/537.36"},
              json={'name': 'Kristina', 'age': 20})

print(res.text)
'''
