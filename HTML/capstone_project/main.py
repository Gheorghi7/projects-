import requests
from bs4 import BeautifulSoup
from work_with_selenium import WWS

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
data = response.text
sol = WWS()


def main():
    for i in range(len(price_for_m)):
        sol.work(price_for_m[i], address_for_m[i], link_for_m[i])


def arr(main_ls: list):
    ls = []
    for i in main_ls:
        if i.text[:len(i.text) - 4:].strip().find('+'):
            ls.append(i.text[:len(i.text) - 4:].strip().replace('+', ''))

        elif i.text[:len(i.text) - 4:].strip().find('+ 1'):
            ls.append(i.text[:len(i.text) - 4:].strip().replace('+ 1', ' '))
        else:
            ls.append(i.text[:len(i.text) - 4:].strip())

    return ls


def arr_for_links(main_arr: list):
    link_arr = []
    for i in main_arr:
        link_arr.append(i.get('href').strip())
    return link_arr


bs_data = BeautifulSoup(data, 'html.parser')
price = bs_data.find_all(class_='PropertyCardWrapper')
address = bs_data.find_all(name='address')
link = bs_data.find_all(class_='property-card-link')

price_for_m = arr(price)
address_for_m = arr(address)
link_for_m = arr_for_links(link)
if __name__ == '__main__':
    main()
