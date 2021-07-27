from models.users import User, UsersResponse, UsersResponsePost
import pytest


class TestUsers:
    def test_get_users(self, client):
        """ Проверка GET запроса на всех юзеров."""
        response = client.get_users(UsersResponse)
        assert response.status_code == 200, "Check response"

    def test_get_users_id(self, client):
        """ Проверка GET запроса на юзера по id."""
        response = client.get_users_id(UsersResponse, id_user="2")
        assert response.status_code == 200, "Check response"

    @pytest.mark.parametrize("id_user", [1, 2, 3]) #1,2,3 - магические числа, они обычно плохо смотрятся в таком виде. Мб стоит сделать генерацию? 
    def test_get_users_id_list(self, client, id_user):
        """ Проверка GET запроса на юзера по id c разными значениями."""
        response = client.get_users_id(UsersResponse, id_user=id_user)
        # print('\n', response.content) - этот комментарий для кого?
        assert response.status_code == 200, "Check response"

    def test_post_user(self, client):
        """ Проверка Post запроса на создание юзера с валидными данными.
        first_name = maxim
        second_name = rodionov
        age = 18
        """
        data = User()
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"

    @pytest.mark.parametrize("first_name", [None, 1234, True])
    def test_post_user_name(self, client, first_name):
        """ Проверка Post запроса на Создание юзера с невалидными данными (first name)."""
        data = User(first_name=str(first_name))
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"

    @pytest.mark.parametrize("second_name", [None, 1234, True])
    def test_post_user_second_name(self, client, second_name):
        """ Проверка Post запроса на Создание юзера с невалидными данными (second name)."""
        data = User(second_name=str(second_name))
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"

    @pytest.mark.parametrize("age", [None, 1234, True])
    def test_post_user_age(self, client, age):
        """ Проверка Post запроса на Создание юзера с невалидными данными (age)."""
        data = User(age=str(age)) #обычно от такого рода конструкций ()(()()) стараются избавляться, выносить из скобок для удобности чтения. Хз как у питонистов)
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"
