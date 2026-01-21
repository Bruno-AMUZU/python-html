def create_index():
    
    # Ouvre (ou crée) un fichier en mode écriture
    with open("index.html", "w") as f:

        f.write('<!DOCTYPE html>' + '\n')
        f.write('<html lang="en">' + '\n')
        f.write('<head>' + '\n')
        f.write('    <meta charset="UTF-8">' + '\n')
        f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">' + '\n')
        f.write('    <title>Document</title>' + '\n')
        f.write('</head>' + '\n')
        f.write('<body>' + '\n')
        f.write('Hello World !' + '\n')
        f.write('</body>' + '\n')
        f.write('</html>' + '\n')

    return True

create_index()
