# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK




import requests
from pprint import pprint


OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': '7510839',
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': 5.89
}

token = '9784a85441e6cb4da4db9321ab2fe8b8ec461fc75a4c6f8ccb9c8e66e4437a3d5de'


class Users_vk:

    def __init__(self, uid):
        self.uid = uid

    def __and__(self, another):
        params = {
            'target_uid': another.uid,
            'access_token': token,
            'v': 5.95
        }
        url = 'https://api.vk.com/method/friends.getMutual'
        response = requests.get(url, params).json()
        list_id = response['response']
        users = []
        for id in list_id:
            users.append(Users_vk(id))
        return users

    def __str__(self):
        return f'https://vk.com/id{self.uid}'


user1 = Users_vk(4466997)
user2 = Users_vk(6997446)
pprint(user1 & user2)
print(user1)






















# params = {
#     'source_uid': 6547548,
#     'target_uid': 7454555,
#     'v': 5.21
# }
#
#
# class User:
#
#     def __and__(self, other_user):
#         response = requests.get(
#         'https://api.vk.com/method/friends.getMutual/get',
#         params
#         )
#         return response.json()
#
#
# uid1 = User()
# uid2 = User()
# mutial_list = uid1&uid2

