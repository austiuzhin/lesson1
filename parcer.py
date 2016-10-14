import requests
from bs4 import BeautifulSoup

data_list = []

def parse(url):
	 r = requests.get(url)
	 soup = BeautifulSoup(r.content, "html.parser")
	 data = soup.find_all("div", {"class": "serp-item__content"})
	 for item in data:
	 	try:
	 		metro_station = item.find_all("div", {"class": "serp-item__solid serp-item__metro"})[0].text
	 		# print(str(metro_station))
	 		distance = item.find_all("div", {"class": "serp-item__distance"})[0].text
	 		data_list.append({
		 		"station": metro_station.replace("\n",""),
		 		"distance": distance.replace("\t","").replace("\n","")
		 		})
	 	except IndexError:
	 		pass
	 print(data_list)
	 # metro_station = data[0].find_all("div", {"class": "serp-item__solid serp-item__metro"})[0].text
	 # print(str(metro_station)	

def send_to_txt(some_list):
	for item in some_list:
		row_text = item.get("station") + ";" + item.get("distance")
		with open("parser.txt","a", encoding = "utf-8") as row:
			row.write(row_text + "\n")

if __name__ == "__main__":
	parse("http://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room9=1&type=4")
	send_to_txt(data_list)

	
