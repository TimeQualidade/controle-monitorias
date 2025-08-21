
import cgi
import json
import os

form = cgi.FieldStorage()
time = form.getvalue("time")
consultor = form.getvalue("consultor")
status = form.getvalue("status")
observacao = form.getvalue("observacao")

if status == "nao_realizada" and not observacao:
    print("Content-type: text/html
")
    print("<html><body><h2>Erro: Observação obrigatória para monitoria não realizada.</h2><a href='index.html'>Voltar</a></body></html>")
    exit()

registro = {
    "time": time,
    "consultor": consultor,
    "status": status,
    "observacao": observacao
}

file_path = "status_monitorias.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        registros = json.load(f)
else:
    registros = []

registros.append(registro)

with open(file_path, "w") as f:
    json.dump(registros, f, indent=4)

print("Content-type: text/html
")
print("<html><body><h2>Status salvo com sucesso!</h2><a href='index.html'>Voltar</a></body></html>")
