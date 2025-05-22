from logger import logger

estoque = {}

def adicionar_produto(nome, quantidade):
    try:
        if nome in estoque:
            estoque[nome] += quantidade
        else:
            estoque[nome] = quantidade
        logger.info(f"Produto '{nome}' adicionado com {quantidade} unidades.")
    except Exception as e:
        logger.error(f"Erro ao adicionar produto '{nome}': {str(e)}")

def remover_produto(nome, quantidade):
    try:
        if nome in estoque and estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            logger.info(f"{quantidade} unidades do produto '{nome}' foram removidas do estoque.")
            return True
        else:
            logger.warning(f"Produto '{nome}' não disponível ou quantidade insuficiente.")
            return False
    except Exception as e:
        logger.error(f"Erro ao remover produto '{nome}': {str(e)}")
        return False

def cadastrar_produto(nome, quantidade_inicial):
    try:
        if nome in estoque:
            logger.warning(f"Produto '{nome}' já está cadastrado.")
        else:
            estoque[nome] = quantidade_inicial
            logger.info(f"Produto '{nome}' cadastrado com {quantidade_inicial} unidades.")
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto '{nome}': {str(e)}")
