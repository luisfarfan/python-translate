from googletrans import Translator

from constants import animals

animals_translations = []
translator = Translator()
translations = translator.translate(animals, src='en', dest='es')
for translation in translations:
    animals_translations.append({'english': translation.origin, 'spanish': translation.text})

print(animals_translations)

import json
with open('animals.translate.json', 'w') as outfile:
    json.dump(animals_translations, outfile)

