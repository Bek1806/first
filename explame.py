import requests
from bs4 import BeautifulSoup as BS
        
file = open('explame_html.html', encoding = 'utf-8')

html = file.read()
soup = BS(html, 'html.parser')

#print(soup)

main_div = soup.find('div', class_ = 'container')
#print(main_div)

navigation = main_div.find('div', class_='navigation')
#print(navigation)

ul = navigation.find('ul', class_='info')
#print(ul)

li_list = ul.find_all('li')
#print(li_list)
#for i in li_list:
#    print(i.text)
content = main_div.find('div', class_='content')
#print(content)

#posts = content.find_all('div', class_='post')
#print(posts)
#for post in posts:
    #title = post.find ('h2', class_='title').text
    #print(title)
foot =content.find('div',class_='footer')

foots = foot.find_all('div', class_='footer-box')
for i in foots:
    title = i.find('p', class_='footer-title').text
    #print(title)


aba = content.find('div', class_='footer')
#print(aba)
abab = aba.find('div', class_='') 
print(abab)

