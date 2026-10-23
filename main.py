"""
Arquivo principal contendo a função de validação de senha.
A função `validar_senha` verifica se a senha atende aos critérios especificados:
- Pelo menos 8 caracteres
- Ao menos 1 dígito
- Ao menos 1 letra maiúscula
Retorna True se a senha for válida, caso contrário retorna False.
"""


def validar_senha(senha):
    """
    Função para validar a senha de acordo com os critérios especificados.
    Retorna True se a senha for válida. Caso contrário, retorna False.
    """
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False

    return True
