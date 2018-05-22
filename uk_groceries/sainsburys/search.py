import json
import lxml.html
import requests

class SainsburysSearcher(object):
    """ Defines the SainsburysSearcher """
    
    def get_brands(self, tree):
        return [brand.text_content() for brand in tree.cssselect('div.topBrands label')]
    
    def set_brand(self, item, brands):
        for brand in brands:
            if brand in item['name']:
                return brand
    
    def get_products(self, query):
        """ Retrieve products from Sainsburys """
        params = {
            'catalogId': 10123,
            'langId': 44,
            'storeId': 10151,
            'top_category': '',
            'pageSize': 100,
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
        brands = self.get_brands(tree)
        print(brands)
        for product in tree.cssselect('ul.productLister div.product'):
            item = {
                'name': ' '.join(product.cssselect('div.productNameAndPromotions h3 a')[0].text_content().strip().split(' ')[:-1]),
                'link': product.cssselect('div.productNameAndPromotions h3 a')[0].get('href'),
                'image': product.cssselect('div.productNameAndPromotions h3 a img')[0].get('src'),
                'price': product.cssselect('div.pricing p.pricePerUnit')[0].text_content().strip().strip('/unit').replace(u"\u00a3", "")[1:],
                'quantity': product.cssselect('div.productNameAndPromotions h3 a')[0].text_content().strip().split(' ')[-1]
            }
            item['brand'] = self.set_brand(item, brands)
            if item['link'].startswith('https://www.sainsburys.co.uk'):
                items.append(item)

        return {'items' : items}
