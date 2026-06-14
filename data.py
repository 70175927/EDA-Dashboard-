import urllib.request
import os

os.makedirs("data", exist_ok=True)

print("Downloading airports...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat",
    "data/airports.dat"
)
print("Downloading routes...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat",
    "data/routes.dat"
)
print("Downloading airlines...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat",
    "data/airlines.dat"
)
print("All files downloaded successfully!")
