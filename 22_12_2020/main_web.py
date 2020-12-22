from flask import Flask, render_template
from functions import list_category, list_martkeplaces, list_sub_category


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/marketplace')
def marketplace():
    list_ = list_martkeplaces()
    return render_template('lists.html', list=list_, path='/categorias')


@app.route('/categorias')
def categories():
    list_ = list_category()
    return render_template('lists.html', list=list_, path='/subcategorias')


@app.route('/subcategorias')
def sub_categories():
    list_ = list_sub_category()
    return render_template('list_sub.html', list=list_)


app.debug = True
app.run()
