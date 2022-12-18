from flask import Flask, request, render_template

app = Flask(__name__)

# Definindo o usuario e a senha
username = "admin"
password = "1234"

# Rota para exibir o formulario de login
@app.route("/login", methods=["GET"])
def login_form():
  return render_template("login_form.html")

# Rota para processar o login do usuario
@app.route("/login", methods=["POST"])
def login_submit():
  # Obtendo os valores do formulario de login
  input_username = request.form["username"]
  input_password = request.form["password"]

  # Verificando se o usuario e senha digitados sao validos
  if input_username == username and input_password == password:
    return "Voce foi autorizado"
  else:
    return "Voce nao foi autorizado"

if __name__ == "__main__":
  
  app.run()
