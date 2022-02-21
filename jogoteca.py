from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import InserDataUser

app = Flask(__name__)
app.secret_key = 'lucasaquino'




@app.route('/')
def games():
    return render_template('lista.html', titulo='Jogos', jogos=lista)



@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', nextpage=url_for('novo')))
    return render_template('novo.html', titulo='Cadastro')



@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('games'))



@app.route('/login')
def login():
    nextpage = request.args.get('nextpage')
    return render_template('login.html', titulo='Login', nextpage=nextpage)



@app.route('/autenticar', methods=['POST',])
def autenticar():

    if request.form['usuario'] in listaUsers:

        user = listaUsers[request.form['usuario']]

        if user.senha == request.form['senha']:

            session['usuario_logado'] = user.id

            flash(f'{user.nome} Login Sucess')

            nextpage2 = request.form['nextpage']            
            return redirect(nextpage2)
    else:
        flash('Login Not Sucess')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum User Connect')
    return redirect(url_for('games'))

app.run(debug=True)
