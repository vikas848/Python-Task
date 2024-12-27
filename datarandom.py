import requests
response = requests.get("https://randomuser.me/api/")
a = response.json()

b = (a["results"])

c = (b[0])
 
gender = (c["gender"])

title = (c["name"]["title"])

first = (c["name"]["first"])

last = (c["name"]["last"]) 

date = (c["dob"]["date"])

age = (c["dob"]["age"])

fullname = title + " "+ first + " " + last   + " " + date +" "+ str(age)

print(fullname)

Country = (c["location"]["country"])

state = (c["location"]["state"])

city = (c["location"]["city"])

postcode = (c["location"]["postcode"])


post= Country +" "+ state +" "+ city +" "+ str(postcode)

print(post)

username = (c["login"]["username"])

password = (c["login"]["password"])

email = (c["email"])

userId = username +" "+ password +" "+ email

print(userId)