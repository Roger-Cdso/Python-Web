from flask import Flask, render_template


app = Flask('Meu App')

posts = [
    {
        'titulo':'primeira postagem',
        'texto': 'teste1'

    },
    {
        'titulo':'segunda postagem',
        'texto': 'teste2'
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts #mock das postagens
    return render_template('exibir_entradas.html',entradas=entradas)











