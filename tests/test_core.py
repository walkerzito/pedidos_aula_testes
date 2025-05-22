import unittest
from core import criar_pedido, listar_pedidos, finalizar_pedido
from estoque import adicionar_produto, cadastrar_produto

class TestGerenciamentoPedidos(unittest.TestCase):
    def setUp(self):
        cadastrar_produto("Mouse", 10)
        adicionar_produto("Teclado", 5)

    def test_criar_pedido_sucesso(self):
        pedido = criar_pedido("Mouse", 2)
        self.assertIsNotNone(pedido)
        self.assertEqual(pedido["produto"], "Mouse")

    def test_finalizar_pedido(self):
        criar_pedido("Teclado", 1)
        sucesso = finalizar_pedido(0)
        self.assertTrue(sucesso)
        pedidos = listar_pedidos()
        self.assertTrue(pedidos[0]["finalizado"])

    def test_finalizar_pedido_invalido(self):
        sucesso = finalizar_pedido(999)
        self.assertFalse(sucesso)

if __name__ == "__main__":
    unittest.main()
