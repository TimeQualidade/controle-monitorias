
import cgi
import json
import os

form = cgi.FieldStorage()
monitor = form.getvalue("monitor")
meta_diaria = int(form.getvalue("meta_diaria"))
meta_mensal = int(form.getvalue("meta_mensal"))

nova_meta = {
    "monitor": monitor,
    "meta_diaria": meta_diaria,
    "meta_mensal": meta_mensal
}

file_path = "metas_performance.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        metas = json.load(f)
else:
    metas = []

# Atualiza ou adiciona meta
atualizado = False
for i, meta in enumerate(metas):
    if meta["monitor"] == monitor:
        metas[i] = nova_meta
        atualizado = True
        break
if not atualizado:
    metas.append(nova_meta)

with open(file_path, "w") as f:
    json.dump(metas, f, indent=4)

print("Content-type: text/html
")
print("<html><body><h2>Metas salvas com sucesso!</h2><a href='index.html'>Voltar</a></body></html>")
