from pyramid.view import view_config

OCADO = {
    'mutti': {
        'name': 'Mutti',
        'description': 'Tomatoes'
    },
    'rice dream': {
        'name': 'Rice Dream',
        'description': 'Milk'
    }
}

@view_config(route_name='ocado', renderer='json')
def get_ocado(request):
    query = request.matchdict['query']
    return OCADO[query]
