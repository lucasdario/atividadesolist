from flask import Flask, render_template
from textwrap import dedent
from function import sum, subtract, multiply, division

app = Flask(__name__)


@app.route('/')
def index():
    welcome = '<h3>-- Calculadora --</h3><hr/>'
    menu = dedent('''
    <a href='/soma'>
        <h4>Operação de soma</h4>
    </a>
    <a href='/sub'>
        <h4>Operação de subtração</h4>
    </a>
    <a href='/multi'>
        <h4>Operação de multiplicação</h4>
    </a>
    <a href='/div'>
        <h4>Operação de divisão</h4>
    </a>   
    ''')
    return f"{welcome}{menu}"


@app.route('/soma')
def sum_function():
    number1 = 10
    number2 = 20
    result = sum(number1, number2)
    return (f'O resultado da soma de {number1} + {number2} é igual <b>=> {result}</b></br>{home_page()}')
    # return render_template('sum.html', n1=number1, n2=number2, r=result)


@app.route('/sub')
def sub_function():
    number1 = 50
    number2 = 25
    result = subtract(number1, number2)
    return (f'O resultado da subtração de {number1} - {number2} é igual a <b>=> {result}</b></br>{home_page()}')


@app.route('/multi')
def multi_function():
    number1 = 10
    number2 = 20
    result = multiply(number1, number2)
    return (f'O resultado da multiplicação de {number1} * {number2} é igual a <b>=> {result}</b></br>{home_page()}')


@app.route('/div')
def div_function():
    number1 = 100
    number2 = 20
    result = division(number1, number2)
    return (f'O resultado da divisão de {number1} / {number2} é igual a <b>=> {result}</b></br>{home_page()}')


def home_page():
    return dedent('''
    <a href='/'>
        <h4>Voltar ao início</h4>
    </a>    
    ''')


app.debug = True
app.run()
