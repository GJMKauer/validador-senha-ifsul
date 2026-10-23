"""
Arquivo de teste para a função `validar_senha` presente no arquivo `main.py`.
Este arquivo contém testes unitários que verificam se a função `validar_senha` está
funcionando corretamente de acordo com os critérios especificados.
"""

from main import validar_senha


def test_validar_senha_invalida_com_menos_de_8_caracteres():
    """
    Validação com senha que possui menos de 8 caracteres.
    """
    assert validar_senha("Abc123") is False
    assert validar_senha("A1b2C3") is False
    assert validar_senha("1234567") is False


def test_validar_senha_invalida_sem_letra():
    """
    Validação com senha que não possui letras.
    """
    assert validar_senha("12345678") is False
    assert validar_senha("!@#$%^&*") is False
    assert validar_senha("1234!@#$") is False


def test_validar_senha_invalida_sem_letra_maiuscula():
    """
    Validação com senha que não possui letras maiúsculas.
    """
    assert validar_senha("abcdefghi") is False
    assert validar_senha("abc12345") is False
    assert validar_senha("abc!@#$%") is False


def test_validar_senha_invalida_sem_numero():
    """
    Validação com senha que não possui dígitos números.
    """
    assert validar_senha("Abcdefgh") is False
    assert validar_senha("Abc!@#$%") is False
    assert validar_senha("Abcdefgh!") is False


def test_validar_senha_invalida_com_todos_os_criterios_falhos():
    """
    Validação com senha que falha em todos os critérios.
    """
    assert validar_senha("abc") is False
    assert validar_senha("123") is False
    assert validar_senha("!@#") is False


def test_validar_senha_valida():
    """
    Validação com senha válida que atende a todos os critérios.
    """
    assert validar_senha("ABC12345") is True
    assert validar_senha("Abc12345") is True
    assert validar_senha("A1b2C3d4") is True


def test_validar_senha_que_falha():
    """
    Validação que falha de verdade apenas para demonstração.
    """
    assert validar_senha("ABC12345") is False
