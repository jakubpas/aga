
def index(req):

    form = req.form
    first_name = form['name']
    sure_name = form['sure_name']
    city = form['city']
    rank = form['rank']
    return """
    <html lang="pl">
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
 """ + first_name + """ ala ma kota ocena: """ + rank + """city:""" + city + """ sure_name""" + sure_name + """
</body>
</html>
    """
