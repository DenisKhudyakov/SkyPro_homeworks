from src.module1.check_email import check_email


def test_check_email_with_valid_email() -> None:
    """
    проверяет, что функция
    check_email
    корректно обрабатывает правильно написанный email
    :return:
    """
    assert check_email("denis.hudyakov@mail.ru") is True


def test_check_email_with_invalid_email() -> None:
    """
    проверяет, что функция
    check_email
    корректно обрабатывает неправильно написанный email.
    :return: None
    """
    assert check_email("denis.hudyakovmail.ru") is False
    assert check_email("denigsfdgfdsakov@mailu") is False


def test_check_email_with_empty_email() -> None:
    """
    проверяет, что функция
    check_email
    корректно обрабатывает пустой email
    :return: None
    """
    assert check_email("") == "e-mail non correct"
