from flask import Flask, render_template

app = Flask(__name__)

# Definindo produtos como um dicionário
produtos = {
    'geleia-de-morango': {
        'nome': 'Geleia de Morango',
        'preco': 'R$ 24,90',
        'imagem': 'geleia1.png',
        'descricao': 'Frasco de 200ml',
    },
    'geleia-de-manga-com-maracuja': {
        'nome': 'Geleia de Manga com Maracujá',
        'preco': 'R$ 26,90',
        'imagem': 'geleia2.png',
        'descricao': 'Frasco de 200ml',
    },
    'geleia-de-goiaba': {
        'nome': 'Geleia de Goiaba',
        'preco': 'R$ 25,90',
        'imagem': 'geleia3.png',
        'descricao': 'Frasco de 200ml',
    },
    'geleia-de-frutas-vermelhas': {
        'nome': 'Geleia de Frutas Vermelhas',
        'preco': 'R$ 24,90',
        'imagem': 'geleia4.png',
        'descricao': 'Frasco de 200ml',
    },
    'geleia-de-pimenta': {
        'nome': 'Geleia de Pimenta',
        'preco': 'R$ 26,90',
        'imagem': 'geleia5.png',
        'descricao': 'Frasco de 200ml',
    },
    'licor-de-cafe': {
        'nome': 'Licor de Café',
        'preco': 'R$ 49,90',
        'imagem': 'licores1.png',
        'descricao': 'Garrafa de 500ml',
    },
    'licor-de-maracuja': {
        'nome': 'Licor de Maracujá',
        'preco': 'R$ 44,90',
        'imagem': 'licores2.png',
        'descricao': 'Garrafa de 500ml',
    },
    'licor-de-chocolate': {
        'nome': 'Licor de Chocolate',
        'preco': 'R$ 50,90',
        'imagem': 'licores3.png',
        'descricao': 'Garrafa de 500ml',
    },
    'licor-de-baunilha': {
        'nome': 'Licor de Baunilha',
        'preco': 'R$ 48,90',
        'imagem': 'licores4.png',
        'descricao': 'Garrafa de 500ml',
    },
    'licor-de-amendoas': {
        'nome': 'Licor de Amêndoas',
        'preco': 'R$ 47,90',
        'imagem': 'licores5.png',
        'descricao': 'Garrafa de 500ml',
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quemsomos.html')

@app.route('/produtos')
def lista_produtos():
    return render_template('produto.html', produtos=produtos)

@app.route('/produto/<produto_id>')
def produto_detalhes(produto_id):
    produto = produtos.get(produto_id)
    if produto:
        return render_template('productpage.html', produto=produto)
    else:
        return "Produto não encontrado", 404

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota para o carrinho
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
