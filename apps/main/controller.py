from don.core.templates import render


def index(args):
    # return render('index.html')
    return render(template='index.html', app=args['app'])


def search(args):
    return args


def page(args):
    return args
