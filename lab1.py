import requests

print(requests.__version__)

r1 = requests.get('http://google.com')

r2 = requests.get('http://raw.githubusercontent.com/gskeates/cmput404_lab1/master/lab1.py')
print(r2.text)
