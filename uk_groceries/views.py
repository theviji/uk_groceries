from pyramid.view import view_config

try:
    from uk_groceries.ocado.search import OcadoSearcher
except:
    import os.path, sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from uk_groceries.ocado.search import OcadoSearcher

ocadosearcher = OcadoSearcher()

@view_config(route_name='ocado', renderer='json')
def get_ocado(request):
    query = request.matchdict['query']
    return ocadosearcher.get_products(query)
