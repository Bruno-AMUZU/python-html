from flask import Flask

app = Flask(__name__)
liste  = [("Bruno", "rouge"), ("Tom", "jaune"), ("Willian", "bordeaux"), ("Nicolas", "Bleu")]

@app.route("/")

def index():
    content =""
    content += f"<h1>Liste</h1>"
    content += f"<ul>"
    for nom, couleur in liste:
        content += f'<li><a href="/personne/{nom}/{couleur}">{nom}</a></li>'
    content += "</ul>"
    ""
    return f"""
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        Hello World !
        {content}

    </body>
    </html>    
"""
@app.route("/personne/<nom>/<couleur>")
def personne(nom, couleur):
     return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>{nom}</title>
    </head>
    <body>
        <h1>{nom}</h1>
        <p>{nom} aime la couleur {couleur}.</p>
        <a href="/">Retour à la liste</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
