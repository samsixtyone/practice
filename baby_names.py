import re
import requests


r = requests.get("https://www.ssa.gov/oact/babynames/decades/names2010s.html")
print (r.status_code)

print (r.headers)

print(r.json())
