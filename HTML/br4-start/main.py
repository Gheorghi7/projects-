from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=popular&n=100")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
data = soup.find_all(bgcolor='#EEEEEE')
for i in data:
    name = i.find(class_='t').getText()
    sec = i.find(class_='l').getText()
    with open('top_100_movies_of_all_time.txt', 'a', encoding='utf-8') as wr_txt:
        wr_txt.write(f"{sec}) {name}\n")


