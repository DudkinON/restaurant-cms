import os

settings = {
    'base_dir': os.path.dirname(__file__),
    # cash True or False
    'cash': False,

    # set name for apps dir
    'apps_dir': os.path.abspath(os.path.dirname(__file__) + '/apps'),
    # set apps folder name
    'apps_folder_name': 'apps',

    # set routes file
    'routes_file': 'routes.py',

    # set controller file
    'controller': 'controller.py',

    # set list of apps
    'apps': [
        'main',
    ],
}


def get_settings():
    return settings
