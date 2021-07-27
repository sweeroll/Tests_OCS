import attr


@attr.s
class User:
    first_name: str = attr.ib(default="maxim")
    second_name: str = attr.ib(default="rodionov")
    age: str = attr.ib(default="18")


@attr.s
class UserIdBody:
    id: int = attr.ib(default="3")


@attr.s
class UsersResponsePost:
    data: list = attr.ib()


@attr.s
class UsersResponseDelete:
    message: str = attr.ib()

@attr.s
class UsersResponse:
    data: dict = attr.ib()
