import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string_password, meaning_value",
    [
        ('Pass@word1', True),
        ('qwerty', False),
        ('Str@ng', False)
    ]
)
def test_check_password(
        string_password,
        meaning_value
) -> None:
    assert check_password(string_password) == meaning_value
