"""
Интернет магазин
 """
from flask import Flask, render_template,request




app = Flask(__name__)

@app.route('/')
def startpage():
    menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>',
             }
    title = "Главная страница магазина"

    return render_template("catalog.html", menu=menu)

@app.route('/catalog/')
def catalog():
   menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>'}
   cat_list = [
       {"name":"Кроссовки адидас 1", "price":2500, "kolsklad":10},
       {"name":"Кроссовки адидас 2", "price":1500, "kolsklad":10},
       {"name":"Кроссовки адидас 3", "price":5200, "kolsklad":10}]

   title = "Каталог товаров"
   return render_template("catalog.html", menu=menu, title= title, cat_list = cat_list)

@app.route('/help/')
def help():
   menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>',
             }
   title = "Помощь"
   return render_template("catalog.html", menu=menu, title= title)

if __name__ == '__main__':
    app.run()

#host='0.0.0.0'