from flask import Flask, render_template, request, json, flash, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time, smtplib, pymysql, subprocess

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

conn = pymysql.connect(host='localhost', port = 3307, user='root', passwd='shoot72',db='userinfo') 
cursor = conn.cursor()

class ReusableForm(Form):
    link = TextField('Link:', validators=[validators.required(), validators.Length(max=100)])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])

@app.route('/', methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        if form.validate():
            link=request.form['link']
            email=request.form['email']
   
            flash('You will be notified on any changes in stock or price')
            
            insert(link, email)
    return render_template('WebPage1.html', form=form)
#constraints

def scrapeData(link, email):
    data = 'https://shop.havenshop.com/products/undercover-ucv3805-t-shirt-white'
    early_page = urlopen(data)
    page = BeautifulSoup(early_page, 'html.parser')

    price = page.find('div', attrs = {'class', 'price-main'})
    new_price = price.find('span', attrs = {'class', 'highlight'})
    part = page.find('div', attrs = {'class', 'product-details'})
    hidden_items = part.find_all('input', type='hidden')
    stock = ''
    for item in hidden_items:
        stock += str(item['value'])
    tup = (stock, new_price)
    return tup

def insert(link, email):
    tup = scrapeData(link, email)
    stock = tup[0]
    new_price = tup[1]
    query = "INSERT INTO HAVEN(email, page, stock, price) \
    VALUES ('%s', '%s', '%s', '%s')" % (email, link, stock, new_price.text)
    try:
        cursor.execute(query)
        conn.commit()
    except:
        conn.rollback()


def getTable():
    qu = "Select * from haven"
    cursor.execute(qu)
    pls = cursor.fetchall()
    return pls

def update(link, email):
    tup = scrapeData(link, email)
    new_stock = tup[0]
    new_price = tup[1]
    new_stock = '1111'
    query = "UPDATE HAVEN SET stock = %s, price = %s \
    WHERE email = %s AND page = %s AND (stock != %s OR price != %s)"
    val = (new_stock, new_price.text, email, link, new_stock, new_price.text)
    try:
        cursor.execute(query, val)
        conn.commit()
        mail(link, email, new_stock, new_price)
    except:
        conn.rollback()
    
    if new_stock == '0000':
        return False
    return True

def mail(link, email, stock, price):
    #try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("stock.webapp.notification@gmail.com", "shoot72!")

    message = "Details for product" + link + "Price: " + price + "Small stock: " + stock[0] \
    + "Medium stock: " + stock[1] + "Large stock: " + stock[2] + "Extra large stock: " + stock[3] \
    + "This message was sent from... If you wish to stop receiving messages ..."
    server.sendmail("stock.webapp.notification@gmail.com", email, message)
    server.quit()
    #except:
        #print('Error')

if __name__ == '__main__':
    app.run('localhost', 4469)

#Other possible features: auto-buy if it dips to 1, other websites 
