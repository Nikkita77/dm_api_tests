import requests


def test_post_v1_account():
    # Регистрация пользователя
    login = 'nikita11'
    password = '1234567'
    email = f'{login}@mail.ru'

    json_data = {
        'login': 'nikita11',
        'email': email,
        'password': password,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)

    # Получить письма из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    # Получить активационный токен
    ...
    # Активация пользователя
    headers = {
        'accept': 'text/plain',
    }

    response = requests.put('http://5.63.153.31:5051/v1/account/4c6b6585-c630-43c6-aa3f-4638dde53b24', headers=headers)
    print(response.status_code)
    print(response.text)
    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
