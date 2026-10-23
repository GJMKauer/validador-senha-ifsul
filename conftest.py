"""
Arquivo de configuração do pytest para adicionar descrições aos testes.
"""


def pytest_itemcollected(item):
    """
    Adiciona a descrição do teste ao nome do item coletado.
    """
    if item.obj.__doc__:
        doc = " ".join(item.obj.__doc__.split())
        setattr(item, "_nodeid", f"{item.nodeid} -> [{doc}]")
