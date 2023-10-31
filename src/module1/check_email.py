import re


def check_email(email: str) -> bool:
    """
    Функиця проверки корректности мэйл адреса
    :param email:  str
    :return: bool
    """
    pattern = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+"
    return (
        True
        if re.fullmatch(pattern, email)
        else "e-mail non correct"
        if len(email) == 0
        else False
    )
