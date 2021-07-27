from models.users import UserIdBody, UsersResponseDelete
import pytest


class TestDeleteUsers:
    @pytest.mark.parametrize("user_id", [3, 4, 5])
    def test_delete_user_body(self, client, user_id):
        """ Проверка Delete запроса на Удаление юзера передавая id в body."""
        data = UserIdBody(id=int(user_id))
        response = client.delete_users(data, UsersResponseDelete)
        assert response.status_code == 200, "Check response"

    @pytest.mark.parametrize("id_user", [6, 7, 8, 9, 10, 11, 12])
    def test_delete_users_id(self, client, id_user):
        """ Проверка Delete запроса на Удаление юзера передавая id в body."""
        response = client.delete_users_id(UsersResponseDelete, id_user=id_user)
        assert response.status_code == 200, "Check response"
