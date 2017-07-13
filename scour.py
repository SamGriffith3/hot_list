import requests
from bs4 import BeautifulSoup
import os
import reusables
import getpass


def search():
    # Determine the website(s) to be searched
    # website_1 = input("First Site: ")  Enable this later as user input variable
    website_1 = "http://www.jimshorkey.com/used-vehicles/#action=im_ajax_call&perform=get_results&_post_id=5&page=1&show_all_filters=false&order=ASC&orderby=price" 

    r = requests.get(website_1).text

    # Scraping the site
    local_csv_file = "C:\\Users\\{}\\Documents\\first.csv".format(getpass.getuser()) # So it works on both mine and yours

    soup = BeautifulSoup(r, 'html.parser')

    data = []
    if os.path.exists(local_csv_file):
        data = reusables.csv_to_list(local_csv_file)  # Cheating because I already wrote this code

    for item in soup.find_all('li', attrs={"class": "result-row"}):
        a_link = item.find('a', attrs={'class': 'result-title hdrlnk'})
        datetime = item.find('time', attrs={'class': 'result-date'})['datetime']
        new_row = [datetime, a_link.text,
                   website_1 + a_link['href'].lstrip("/")]
        if new_row in data:
            continue
        data.append(new_row)
        print("Adding {}".format(a_link.text))
        
    for item in soup.find_all('postingbody', attrs={"class": "result-row"}):
        

    reusables.list_to_csv(data[-100:], local_csv_file)

    print("done")


search()
