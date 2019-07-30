from flask import Flask,url_for,flash,session,render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from form import formulario
from usuario import Usuario
from dao import UsuarioDAO

app= Flask(__name__,template_folder='template')
app.secret_key ='chave'

Bootstrap(app)
app.config["SECRET_KEY"] = "a secret key you won't forget"
app.config["BABEL_DEFAULT_LOCALE"] = "pt"	
babel = Babel(app)

@app.route('/')
def home():
    form = formulario()
    return render_template('index.html', form = form)

@app.route('/alterar',methods=['GET','POST'])
def alterar():
    form = formulario()
    if form.validate_on_submit():
        dao = UsuarioDAO()
        pessoa = Usuario(nome=request.form['nome'],login=request.form['login'],altura=request.form['altura'],senha=request.form['senha'],idade=request.form['idade'],email=request.form['email'])
        dao.salvar(pessoa)
        return ('sucesso')

    else:
        return render_template('index.html',form=form,pessoa=pessoa)

    return redirect(url_for('lista'))

def main():
    app.env ='development'
    app.run(debug=True, port=5020)

if __name__ =='__main__':
    main()
