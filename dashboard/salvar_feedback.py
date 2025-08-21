
import cgi
import json
import os

form = cgi.FieldStorage()
consultor = form.getvalue("consultor")
criterios = list(map(float, form.getvalue("criterios").split(",")))
pesos = list(map(float, form.getvalue("pesos").split(",")))
observacao = form.getvalue("observacao")
melhoria = form.getvalue("melhoria")

if len(criterios) != len(pesos):
    print("Content-type: text/html
")
    print("<html><body><h2>Erro: número de critérios e pesos deve ser igual.</h2><a href='index.html'>Voltar</a></body></html>")
    exit()

nota = round(sum(c * p for c, p in zip(criterios, pesos)) / sum(pesos), 2)

feedback = {
    "consultor": consultor,
    "nota": nota,
    "observacao": observacao,
    "melhoria": melhoria
}

file_path = "feedbacks.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        feedbacks = json.load(f)
else:
    feedbacks = []

feedbacks.append(feedback)

with open(file_path, "w") as f:
    json.dump(feedbacks, f, indent=4)

print("Content-type: text/html
")
print(f"<html><body><h2>Feedback enviado com sucesso! Nota calculada: {nota}</h2><a href='index.html'>Voltar</a></body></html>")
