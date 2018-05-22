import json
import lxml.html
import re
import requests

class OcadoSearcher(object):
    """ Defines the OcadoSearcher """
    def get_products(self, query):
        """ Retrieve products from Ocado """
        params = {
            'clearTabs': 'yes',
            'isFreshSearch': 'true',
            'entry': query,
        }
        response = requests.get(url='https://www.ocado.com/webshop/getSearchProducts.do',
                                params=params)
        tree = lxml.html.fromstring(response.content)
        json_response = json.loads(tree.cssselect('script.js-productPageJson')[0].text_content())
        items = []
        for section in json_response['sections']:
            for fop in section['fops']:
                try:
                    item = {
                        'name': fop['product']['name'],
                        'link': 'https://www.ocado.com' + fop['product']['simplifiedBopUrl'],
                        'image': 'https://www.ocado.com' + fop['product']['imageSrc'],
                        'quantity': re.sub(r"(\d.*) per pack", r"x\1", fop['product']['catchWeight']),
                        'brand': fop['product']['brand'],
                        'price': fop['product']['price']['currentPrice'].replace('&pound;', ''),
                    }
                    items.append(item)
                except:
                    pass # no product in this item
                
        return {'items' : items}

    def get_number_of_products(self, query):
        """ Print the number of products """
        total_amount = 0
        ocado_json = self.get_products(query)
        for section in ocado_json['sections']:
            total_amount += int(section['actualSize'])
        print(f'{total_amount} product(s) found for `{query}`')
