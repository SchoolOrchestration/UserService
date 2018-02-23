from django.conf import settings
import requests


class Consumer:
    def __init__(self, username=None, kong_id=None):
        self.username = username
        self.kong_id = kong_id

    @classmethod
    def create(cls, username):
        cls.username = username
        response = requests.post(
            '{}/consumers/'.format(settings.KONG_ADMIN_URL),
            data={
                'username': cls.username
            }
        )
        if response.status_code == 201:
            cls.kong_id = response.json()['id']
            return cls


class ConsumerACL:
    def __init__(self, username):
        self.username = username

    def create(self):
        groups = self.username.split('.')[1:]

        for group in groups:
            response = requests.post(
                '{}/consumers/{}/acls'.format(
                    settings.KONG_ADMIN_URL,
                    self.username
                ),
                data={
                    'group': group
                }
            )
            if response.status_code != 201:
                return False


class GlobalACL:
    def __init__(self, username):
        response = requests.get(
            '{}/plugins'.format(
                settings.KONG_ADMIN_URL)
        )
        self.username = username
        self.plugin_id = None
        if response.status_code == 200:
            for plugin in response.json()['data']:
                if 'acl' in plugin['name']:
                    self.plugin_id = plugin['id']

    def update(self):
        groups = self.username.split('.')[1:]
        response = requests.post(
            '{}/{}'.format(
                settings.KONG_ADMIN_URL,
                self.plugin_id
            ),
            data={
                'config.whitelist': self._comma_seperated_groups(groups)
            }
        )
        import ipdb;ipdb.set_trace()
        if response.status_code != 201:
            return False

    def _comma_seperated_groups(self, groups):
        group_list = ''
        for group in groups:
            if ',' in group_list:
                '{}, {}'.format(group_list, group)
            else:
                '{},'.format(group)
        return group_list
