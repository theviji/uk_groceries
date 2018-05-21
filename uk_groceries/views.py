from pyramid.view import view_config

try:
    from uk_groceries.ocado.search import OcadoSearcher
    from uk_groceries.sainsburys.search import SainsburysSearcher
except:
    import os.path, sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from uk_groceries.ocado.search import OcadoSearcher
    from uk_groceries.sainsburys.search import SainsburysSearcher

ocadosearcher = OcadoSearcher()
sainsburyssearcher = SainsburysSearcher()

@view_config(route_name='ocado', renderer='json')
def get_ocado(request):
    query = request.matchdict['query']
    return ocadosearcher.get_products(query)

@view_config(route_name='sainsburys', renderer='json')
def get_sainsburys(request):
    query = request.matchdict['query']
    return sainsburyssearcher.get_products(query)
