import requests
import csv
from bs4 import BeautifulSoup


page = requests.get('https://students.flinders.edu.au/my-course/course-rules/masters')

soup = BeautifulSoup(page.text, 'html.parser')

# Create a file to write to, add headers row
f = csv.writer(open('anshu.csv', 'w'))
f.writerow(['courses_name', 'Flinders_uni_links'])

name_list = soup.find('ul',class_='dropdown_menu__list dropdown-menu')
name_list_items = name_list.find_all('a')

for name in name_list_items:
    courses_name = name.contents[0]
    Flinders_uni_links = 'https://students.flinders.edu.au/my-course/course-rules/masters' + name.get('href')
    f.writerow([courses_name, Flinders_uni_links])







