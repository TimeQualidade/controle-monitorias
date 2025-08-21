
import cgi
import json
import os

form = cgi.FieldStorage()
ficha = {
    "canal": form.getvalue("canal"),
    "consultor": form.getvalue("consultor"),
    "monitor": form.getvalue("monitor"),
    "cliente": form.getvalue("cliente"),
    "contato": form.getvalue("contato"),
    "destino": form.getvalue("destino"),
    "contrato": form.getvalue("contrato"),
    "duracao": form.getvalue("duracao")
}

file_path = "fichas_monitoria.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        fichas = json.load(f)
else:
    fichas = []

fichas.append(ficha)

with open(file_path, "w") as f:
    json.dump(fichas, f, indent=4)

print("Content-type: text/html
")
print("<html><body><h2>Ficha salva com sucesso!</h2><a href='index.html'>Voltar</a></body></html>")
