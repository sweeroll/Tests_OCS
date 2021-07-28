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

    @pytest.mark.parametrize("id_user", [1, 2, 3])
    def test_get_users_id_list(self, client, id_user):
        """ Проверка GET запроса на юзера по id c разными значениями."""
        response = client.get_users_id(UsersResponse, id_user=id_user)
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
        """ Проверка Post запроса на создание юзера с невалидными данными (first name)."""
        data = User(first_name=str(first_name))
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"

    @pytest.mark.parametrize("second_name", [None, 1234, True])
    def test_post_user_second_name(self, client, second_name):
        """ Проверка Post запроса на создание юзера с невалидными данными (second name)."""
        data = User(second_name=str(second_name))
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"

    @pytest.mark.parametrize("age", [None, 1234, True])
    def test_post_user_age(self, client, age):
        """ Проверка Post запроса на создание юзера с невалидными данными (age)."""
        data = User(age=str(age))
        response = client.post_users(data, UsersResponsePost)
        assert response.status_code == 201, "Check response"
