from don.core.templates import render


def restaurants(args):
    # return render('index.html')

    return render(template='index.html', args=args)


def new(args):
    return args


def delete(args):
    return args


def edit(args):
    return args
