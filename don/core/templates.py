from jinja2 import Environment, PackageLoader, select_autoescape
from don.router import get
env = Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)