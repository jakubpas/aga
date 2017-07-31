#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import database module
import sqlite3

# main function
def index(req):

    # get data from form
    info = req.form
    first_name = info['name']
    last_name = info['sure_name']
    city = info['city']
    rank = info['rank']

    if not all((first_name, last_name, city, rank)):
        return '''
<html lang="pl">
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css" />
<head>
<body>
    <div class="wrapper">
          <h1>Ocena strony</h1>
          <div class="wrapper-content contact">
                <hr>
                Prosze uzupełnić wszystkie pola<p>

        </div>
    <div>
</body>
</html>'''

    #database connection
    conn = sqlite3.connect('/var/www/aga/ranks.db')
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS ratings (first_name text, last_name text, city text, rank int)''')

    # Insert a row of data`
    c.execute("INSERT INTO ratings  VALUES (?,?,?,?)",(first_name, last_name, city, rank))
    conn.commit()

    # Get ranks number and average
    rating_num = str(c.execute("SELECT COUNT(*) as num FROM ratings").fetchone()[0])
    average = str(round(c.execute("SELECT AVG(rank) as average FROM  ratings").fetchone()[0],1))
    conn.close()

# Display result
    return """
<html lang="pl">
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css" />
<head>
<body>
    <div class="wrapper">
          <h1>Ocena strony</h1>
          <div class="wrapper-content contact">

                <hr>

                Dziekujemy za wystawienie oceny stronie<p>

                Twoje imie to: """ + first_name + """ <p>
                Twoje nazwisko to: """ + last_name + """ <p>
                Twoje miast to: """ + city + """ <p>
                Twoja ocena to: """ + rank + """ <p>

                <hr>

                Liczba dotychczasowych ocen to: """ + rating_num + """
                Średnia wszystkich ocen to: """ + average + """

        </div>
    <div>
</body>
</html>