import json
import lxml.html
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
        return json.loads(tree.cssselect('script.js-productPageJson')[0].text_content())

    def get_number_of_products(self, query):
        """ Print the number of products """
        total_amount = 0
        ocado_json = self.get_products(query)
        for section in ocado_json['sections']:
            total_amount += int(section['actualSize'])
        print(f'{total_amount} product(s) found for `{query}`')
