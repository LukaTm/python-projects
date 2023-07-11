from bs4 import BeautifulSoup



with open('website.html',encoding='utf-8') as web: # encoding fixed  the error
    contents = web.read()

soup = BeautifulSoup(contents, 'html.parser') #help soup understand these contents | if error use import lxml and parser vieta lxml
#print(soup.title) # bus - <title>Angela's Personal Site</title>
#print(soup.title.name) # bus - title
#print(soup.title.string) # bus - Angela's Personal Site
#print(soup) # visu kas ir soup tikai ne indented
#print(soup.prettify()) # visu kar is sopu bet indented smuki
#print(soup.a) # first anchor tag that it finds
#print(soup.li) # ^

all_anchor_tags = soup.find_all(name='a') # ALL anchor tags | pielavu kludu find_all SKATIES KA NAV NEPAREIZS TE KAUT KUR ARI

for tag in all_anchor_tags:
    print(tag.getText()) # gonna loop and only get anchor text
    print(tag.get('href')) # only tag href linki - https://angelabauer.github.io/cv/hobbies.html

heading = soup.find(name='h1',id='name') # samekle ne find_all tikai vienu kam ir h1 jo var but vairaki un pec id = 'name'
section_heading = soup.find(name='h3', class_='heading') # class_ jo nevar class jo python create class vinam liekas
#print(section_heading.text) # Books and Teaching
#print(section_heading.name) #h3
#print(section_heading.get('class)) # ['heading']

company_url = soup.select_one(selector='p a') # the first matching ITEM  -  <a href="https://www.appbrewery.co/">The App Brewery</a>
company_uasdadsa = soup.select_one(selector='#name') # id  | keyword argument not neseciary
company_class_dbwds = soup.select('.heading') # a list cause many - [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]





