from flask import Flask, render_template, request, json, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    link = TextField('Link:', validators=[validators.required(), validators.Length(max=100)])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])

@app.route('/', methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        link=request.form['link']
        email=request.form['email']
    if form.validate():
        flash('Thank you for using this site!')
    return render_template('WebPage1.html', form=form)

if __name__ == '__main__':
    app.run('localhost', 4469)
#constraints

#data = 'https://shop.havenshop.com/collections/sale-t-shirts'
#data = 'https://shop.havenshop.com/products/undercover-ucv3805-t-shirt-white'
early_page = urlopen(link)
page = BeautifulSoup(early_page, 'html.parser')

dictionary = {}

#while True:
early_page = urlopen(data)
page = BeautifulSoup(early_page, 'html.parser')

part = page.find('div', attrs = {'class', 'product-details'})
hidden_items = part.find_all('input', type='hidden')
for item in hidden_items:
    pass
    #dictionary[url['href'][36:]] = item['value']
    #print(dictionary[url['href'][36:]])
        
'''
Thoughts: How often to check website, save data to quicken? SQL data storage?
print(dictionary['undercover-ucv3809-tee-black'])

for key, value in dictionary.items():
    #print(value)
        
notification
if val in list < 5:
    notify user
if val goes from 0 to + (restock), notify user
if price changes, notify user

Other possible features: auto-buy if it dips to 1, other websites 
'''