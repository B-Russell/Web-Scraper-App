from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('WebPage1.html')

if __name__ == '__main__':
    app.run('localhost', 4469)


#site = input('Enter a Haven web address')
#constraints

#data = 'https://shop.havenshop.com/collections/sale-t-shirts'
data = 'https://shop.havenshop.com/products/undercover-ucv3805-t-shirt-white'
early_page = urlopen(data)
page = BeautifulSoup(early_page, 'html.parser')

dictionary = {}

part = page.find('div', attrs = {'class', 'product-details'})
hidden_items = part.find_all('input', type='hidden')
for item in hidden_items:
    dictionary[url['href'][36:]] = item['value']
    print(dictionary[url['href'][36:]])
        
'''
Thoughts: How often to check website, save data to quicken? SQL data storage?
print(dictionary['undercover-ucv3809-tee-black'])

for key, value in dictionary.items():
    #print(value)
        
notification
if val in list < 5:
    notify user
if val goes from 0 to + (restock), notify user

Other possible features: auto-buy if it dips to 1, other websites 
'''