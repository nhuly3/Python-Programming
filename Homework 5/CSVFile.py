import requests
from pathlib import Path

url="https://raw.githubusercontent.com/csbfx/advpy122-data/master/California_housing.csv"
path=Path("California_housing.csv")
result=requests.get(url)

with open(path, "wb") as file:
  file.write(result.content)

print("Downloaded.")
