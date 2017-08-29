import importlib
import os
from re import match
from urllib.parse import urlparse, parse_qs


class Router:
    def __init__(self, path, settings):
        self.uri = urlparse(path)
        self.query = self.uri.query
        self.route = self.uri.path[1:].split('/')[0]
        self.settings = settings
        self.apps_dir = settings['apps_dir']
        self.controller = ''
        self.action = ''
        self.app = ''

    def run(self):
        return self.uri.path[1:]

    def get_route(self):
        """Return current route.

        :return string:
        """
        return self.route

    def get_settings(self):
        """Return dictionary of settings.

        :return dict:
        """
        return self.settings

    def cut_extension(self, string):
        """Get string and replace extension '.py' on ''.

        :param string:
        :return string:
        """
        return string.replace('.py', '')

    def get_routes_path(self, app):
        """Get string app return path to routes file.

        :param app:
        :return string:
        """
        return os.path.abspath(self.settings['apps_dir'] + '/' + app + '/' + self.settings['routes_file'])

    def build_path(self, folder_name, app, routes_file):
        """Build module path.

        :param folder_name:
        :param app:
        :param routes_file:
        :return string:
        """
        return '{}.{}.{}'.format(folder_name, app, routes_file)

    def get_list_routes(self, name):
        """Return the list of tuple.

        :param name:
        :return:
        """
        file = importlib.import_module(name)
        return file.routes

    def set_action(self, action):
        """Set current action.

        :param action:
        :return void:
        """
        self.action = action

    def set_app(self, app):
        """Set current app.

        :param app:
        :return void:
        """
        self.action = app

    def get_app(self):
        """Return current app

        :return string:
        """
        return self.app

    def get_controller(self):
        for app in self.settings['apps']:
            # check the file exist
            if os.path.isfile(self.get_routes_path(app=app)):
                routes_file = self.cut_extension(self.settings['routes_file'])
                name = self.build_path(self.settings['apps_folder_name'], app, routes_file=routes_file)
                routes = self.get_list_routes(name)
                for route in routes:
                    if match(route[0], self.route):
                        self.set_app(app)
                        self.set_action(route[1])
                        controller_file = self.cut_extension(self.settings['controller'])
                        return self.build_path(self.settings['apps_folder_name'], app, controller_file)
            else:
                return None

    def run_action(self):
        current_controller = self.get_controller()
        if current_controller is not None:
            self.controller = importlib.import_module(current_controller)
            return getattr(self.controller, self.action)(self.action)




if __name__ == '__main__':
    pass
else:
    Router = Router
