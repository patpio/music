flask shell w terminalu
exit()
request.endpoint - aktualny endpoint

babel.cfg
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel init -i messages.pot -d app/translations -l hr
pybabel compile -d app/translations
na koniec podpiąć pod babel
pybabel update

https://www.mydevil.net/oferta.html
revolut