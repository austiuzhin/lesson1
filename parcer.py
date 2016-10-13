import requests
from bs4 import BeautifulSoup

#here we define the function that gets data - use it with every loaded page

# 	with open("parser.txt","a",encoding = "utf-8") as write_down:
# 		write_down.write(metro_station)

data_list = []

def parse(url):
	 r = requests.get(url)
	 soup = BeautifulSoup(r.content, "html.parser")
	 data = soup.find_all("div", {"class": "serp-item__content"})
	 for item in data:
	 	metro_station = item.find_all("div", {"class": "serp-item__solid serp-item__metro"})[0].text
	 	distance = item.find_all("div", {"class": "serp-item__distance"})[0].text
	 	data_list.append({
	 		"station": metro_station,
	 		"distance": distance
	 		})
	 	

if __name__ == "__main__":
	parse("http://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room9=1&type=4")


	

