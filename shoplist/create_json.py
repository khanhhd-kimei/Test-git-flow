#! /usr/bin/python

import json
from collections import OrderedDict
from pprint import pprint

locales = {
	"fr": "fr_FR",
	"ge": "de_DE",
	"it": "it_IT",
	"po": "pl_PL",
	"ru": "ru_RU",
	"sp": "es_ES"
}

json_file='shop-list-en_GB.json'
mapping_file='mapping.json'

with open(mapping_file) as mapping_load:
	with open(json_file) as json_load:
		shoplist_data = json.load(json_load)
		mapping_data = json.load(mapping_load)

		for key, locale in locales.items():
			data = []

			for shoplist in  shoplist_data:
				tmp = OrderedDict(shoplist)
				tmp["name"] = mapping_data[shoplist["name"].upper()][key].title()
				data.append(tmp)

			output_filename = "shop-list-" + locale + ".json"
			with open(output_filename, 'w') as outfile:
				json.dump(data, outfile)
				

##############################################

# _list = {
# 	"CN" : "China",
# 	"HK" : "Hongkong",
# 	"KR" : "Korea",
# 	"GB" : "UnitedKingdom",
# 	"RU" : "Russia",
# 	"RS" : "Serbia",
# 	"BA" : "Bosna",
# 	"ME" : "Montenegro",
# 	"BG" : "Bulgaria",
# 	"FR" : "France",
# 	"ES" : "Spain",
# 	"AD" : "Andorra",
# 	"PT" : "Portugal",
# 	"IT" : "Italy",
# 	"AT" : "Austria",
# 	"NL" : "Netherland",
# 	"BE" : "Belgium",
# 	"SK" : "Slovakia",
# 	"CZ" : "Czech Republic",
# 	"PL" : "Poland",
# 	"LT" : "Lithuania",
# 	"CH" : "Swiss",
# 	"UA" : "Ukraine",
# 	"US" : "America",
# 	"CA" : "Canada"
# }
# mapping_file='mapping.json'
# with open(mapping_file) as mapping_load:
# 	mapping_data = json.load(mapping_load)
# 	data = OrderedDict()
# 	for key, locale in locales.items():
# 		tmp = OrderedDict(_list)
# 		for k, v in _list.items():
# 			tmp[k] = mapping_data[v.upper()][key]
# 		data[locale] = tmp
# 	print json.dumps(data)
# 	