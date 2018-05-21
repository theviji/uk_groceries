import json
import lxml.html
import requests

class SainsburysSearcher(object):
    """ Defines the SainsburysSearcher """
    def get_products(self, query):
        """ Retrieve products from Sainsburys """
        params = {
            'catalogId': 10123,
            'langId': 44,
            'storeId': 10151,
            'top_category': '',
            'pageSize': 36,
            'orderBy': 'RELEVANCE',
            'beginIndex': 0,
            'hideFilters': True,
            'categoryFacetId1': '',
            'searchTerm': query,
        }
        response = requests.get(url='https://www.sainsburys.co.uk/webapp/wcs/stores/servlet/SearchDisplayView',
                                params=params)
        tree = lxml.html.fromstring(response.content)
        items = []
        for product in tree.cssselect('ul.productLister div.product'):
            item = {
                'link': product.cssselect('div.productNameAndPromotions h3 a')[0].get('href'),
                'name': product.cssselect('div.productNameAndPromotions h3 a')[0].text_content().strip(),
                'image': product.cssselect('div.productNameAndPromotions h3 a img')[0].get('src'),
                'price': product.cssselect('div.pricing p.pricePerUnit')[0].text_content().strip().strip('/unit').replace(u"\u00a3", "")[1:],
            }
            if item['link'].startswith('https://www.sainsburys.co.uk'):
                items.append(item)
        
       
        return {'items' : items}
