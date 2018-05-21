from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.cors')
    config.add_cors_preflight_handler()
    config.add_route('ocado', '/ocado/{query}')
    config.add_route('sainsburys', '/sainsburys/{query}')
    config.scan()
    return config.make_wsgi_app()
