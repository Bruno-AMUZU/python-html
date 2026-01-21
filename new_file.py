from flask import Flask

app = Flask(__name__)
liste  = [("Bruno", "rouge"), ("Tom", "jaune"), ("Willian", "vert"), ("Nicolas", "Bleu")]

@app.route("/")

def index():

    template = ""

    if liste != []:

        template += f"<ul> Liste des prénoms"

        for i in range(len(liste)):

            template += f"<li> {liste[i][0]} </li>"

        template += f"</ul>"


    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        Hello World !
        {template}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
