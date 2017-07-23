


def index(reg):

    form = reg.form
    first_name = form['name']
    return """
    <html lang="pl">
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
 """ + first_name + """
</body>
</html>
    """
