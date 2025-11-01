import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, verify_result",
    [
        pytest.param("Ab1!xyz", False,
                     id="password to short"),
        pytest.param("Abcdefghijklmn1!Z", False,
                     id="password to long"),
        pytest.param("password1!", False,
                     id="password has no capital letter"),
        pytest.param("Password!!", False,
                     id="password has no digits"),
        pytest.param("Password1", False,
                     id="password has no special symbols"),
        pytest.param("Password1?", False,
                     id="password has not allowed symbol"),
        pytest.param("Pass word1!", False,
                     id="password has not allowed symbol"),
        pytest.param("Passwörd1@", False,
                     id="password has not allowed symbol"),
        pytest.param("Пароль1@", False,
                     id="password has not allowed symbol"),
        pytest.param("A1!aaaaaA1!aaaaa", True,
                     id="password is valid"),
        pytest.param("@A1!a_aAa", True,
                     id="password has is valid"),
    ]
)
def test_check_password(password: str, verify_result: bool) -> None:
    assert check_password(password) == verify_result
