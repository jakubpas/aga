
def index(req):

    form = {'name': 'jakub', 'sure_name': 'pas'}

    form = req.form
    first_name = form['name']
    rank = form['rank']
    return """
    <html lang="pl">
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
 """ + first_name + """ ala ma kota ocena: """ + rank + """
</body>
</html>
    """
