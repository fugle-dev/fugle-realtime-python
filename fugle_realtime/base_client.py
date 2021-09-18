class BaseClient(object):
    def __init__(self, api_token=None, api_version=None, url=None):
        self.config = {'api_token': api_token, 'api_version': api_version, 'url': url }

    def set_api_token(self, api_token):
        self.config['api_token'] = api_token

    def set_api_version(self, api_version):
        self.config['api_version'] = api_version
