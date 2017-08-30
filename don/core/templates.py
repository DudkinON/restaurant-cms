from don.dependencies.jinja2 import Environment, select_autoescape, \
    FileSystemLoader
from settings import settings


def render(template, *args, **kwargs):
    paths = []
    for path in settings['apps']:
        paths.append(settings['templates'] + '/' + path)
    paths.append(settings['templates'])
    env = Environment(
        loader=FileSystemLoader(paths),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True
    )
    return env.get_template(template).render(*args, **kwargs)

