To get all strings for translation:

`pybabel extract -F babel.cfg -o messages.pot .`    


To init po file (first time):

`pybabel init -i messages.pot -d ./app/translations  -l el_GR`    


To update exist po file:

`pybabel update -i messages.pot -d ./app/translations`    


To compile po file to mo:

`pybabel compile -f -d ./app/translations`