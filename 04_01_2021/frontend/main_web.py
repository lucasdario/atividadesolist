import sys
sys.path.append('.')
from backend.functions import *
from flask import Flask, render_template, request


app = Flask(__name__)
boot()


@app.route('/')
def index():
    return render_template('menu.html', title='Olist - Marketplaces')


@app.route('/marketplace')
def marketplace():
    list_ = list_martkeplaces()
    return render_template('lists.html', list=list_, path='/categorias', title='Olist - Marketplaces')


@app.route('/categorias')
def categories():
    list_ = list_category()
    return render_template('lists.html', list=list_, path='/subcategorias', title='Olist - Marketplaces')


@app.route('/subcategorias')
def sub_categories():
    list_ = list_sub_category()
    return render_template('list_sub.html', list=list_, title='Olist - Marketplaces')


@app.route('/register')
def register():
    name = request.args.get('name')
    option = request.args.get('option')
    return_msg = ''
    return_msg_class = ''
    if option == 'marketplace':
        if name:
            if add_marketplace(name):
                return_msg = 'Marketplace cadastrado com sucesso.'
                return_msg_class = 'notification is-primary'
            else:
                return_msg = 'Ops =( Parece que algo deu errado, tente novamente mais tarde!'
                return_msg_class = 'notification is-warning'
        return render_template('register.html', title='Olist - Marketplaces', msg_label='Novo marketplace', type='marketplace',
                               msg_return=return_msg, msg_class=return_msg_class)
    elif option == 'category':
        if name:
            if add_category(name):
                return_msg = 'Categoria cadastrado com sucesso.'
                return_msg_class = 'notification is-primary'
            else:
                return_msg = 'Ops =( Parece que algo deu errado, tente novamente mais tarde!'
                return_msg_class = 'notification is-warning'
        return render_template('register.html', title='Olist - Marketplaces', msg_label='Nova categoria', type='category',
                               msg_return=return_msg, msg_class=return_msg_class)
    elif option == 'subcategory':
        if name:
            if add_subcategory(name):
                return_msg = 'Sub-categoria cadastrado com sucesso.'
                return_msg_class = 'notification is-primary'
            else:
                return_msg = 'Ops =( Parece que algo deu errado, tente novamente mais tarde!'
                return_msg_class = 'notification is-warning'
        return render_template('register.html', title='Olist - Marketplaces', msg_label='Nova sub-categoria', type='subcategory',
                               msg_return=return_msg, msg_class=return_msg_class)
    else:
        return render_template('menu.html', title='Olist - Marketplaces')


app.debug = True
app.run()
