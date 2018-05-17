from pyramid.view import view_config

from uk_groceries.ocado.search import OcadoSearcher

ocadosearcher = OcadoSearcher()

@view_config(route_name='ocado', renderer='json')
def get_ocado(request):
    query = request.matchdict['query']
    return ocadosearcher.get_products(query)
