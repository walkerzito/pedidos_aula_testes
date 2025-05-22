from estoque import remover_produto
from logger import logger

pedidos = []

def criar_pedido(produto, quantidade):
    try:
        if remover_produto(produto, quantidade):
            pedido = {"produto": produto, "quantidade": quantidade, "finalizado": False}
            pedidos.append(pedido)
            logger.info(f"Pedido criado: {pedido}")
            return pedido
        else:
            raise ValueError("Produto não disponível em estoque.")
    except Exception as e:
        logger.error(f"Erro ao criar pedido: {str(e)}")
        return None

def listar_pedidos():
    return pedidos

def finalizar_pedido(index):
    try:
        if 0 <= index < len(pedidos):
            pedidos[index]["finalizado"] = True
            logger.info(f"Pedido finalizado: {pedidos[index]}")
            return True
        else:
            raise IndexError("Índice de pedido inválido.")
    except Exception as e:
        logger.error(f"Erro ao finalizar pedido: {str(e)}")
        return False
