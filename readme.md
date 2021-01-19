flask shell w terminalu
exit()
request.endpoint - aktualny endpoint

babel.cfg
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel init -i messages.pot -d app/translations -l hr
Now edit the translations/de/LC_MESSAGES/messages.po file as needed
pybabel compile -d app/translations
na koniec podpiąć pod babel @babel.localeselector
pybabel update -i messages.pot -d app/translations (w przypadku update'u)
https://flask-babel.tkte.ch/

https://www.mydevil.net/oferta.html
revolut