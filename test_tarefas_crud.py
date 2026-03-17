import unittest
from tarefas_crud import Tarefa, validar_data

class TestTarefaCRUD(unittest.TestCase):
        # Erro: criar tarefa com título só de espaços
        def test_criar_tarefa_titulo_espacos(self):
            tarefa = Tarefa(self.next_id, "   ", "Desc", "2024-03-17")
            self.assertEqual(tarefa.titulo, "")

        # Erro: criar tarefa com data inválida (formato errado)
        def test_criar_tarefa_data_formato_errado(self):
            tarefa = Tarefa(self.next_id, "Teste", "Desc", "17-03-2024")
            self.assertFalse(validar_data(tarefa.data))

        # Erro: deletar tarefa inexistente
        def test_deletar_tarefa_inexistente(self):
            tarefas = {}
            with self.assertRaises(KeyError):
                del tarefas[123]

        # Erro: acessar atributo de tarefa removida
        def test_acessar_tarefa_removida(self):
            tarefa = Tarefa(self.next_id, "Teste", "Desc", "2024-03-17")
            tarefas = {self.next_id: tarefa}
            del tarefas[self.next_id]
            with self.assertRaises(KeyError):
                _ = tarefas[self.next_id]
    def setUp(self):
        self.tarefas = {}
        self.next_id = 1

    def test_criar_tarefa_nome_valido(self):
        tarefa = Tarefa(self.next_id, "Estudar Python", "Aprofundar em testes", "2024-03-17")
        self.tarefas[self.next_id] = tarefa
        self.assertIn(self.next_id, self.tarefas)
        self.assertEqual(self.tarefas[self.next_id].titulo, "Estudar Python")

    def test_criar_tarefa_nome_vazio(self):
        tarefa = Tarefa(self.next_id, "", "Descrição", "2024-03-17")
        self.tarefas[self.next_id] = tarefa
        self.assertEqual(self.tarefas[self.next_id].titulo, "")

    def test_remover_tarefa_id_valido(self):
        tarefa = Tarefa(self.next_id, "Tarefa", "Desc", "2024-03-17")
        self.tarefas[self.next_id] = tarefa
        del self.tarefas[self.next_id]
        self.assertNotIn(self.next_id, self.tarefas)

    def test_remover_tarefa_id_inexistente(self):
        with self.assertRaises(KeyError):
            del self.tarefas[999]

    def test_validar_data_valida(self):
        self.assertTrue(validar_data("2024-03-17"))

    def test_validar_data_invalida(self):
        self.assertFalse(validar_data("2024-31-12"))

    # Cenário alternativo: criar tarefa com data vazia
    def test_criar_tarefa_data_vazia(self):
        tarefa = Tarefa(self.next_id, "Teste", "Desc", "")
        self.assertFalse(validar_data(tarefa.data))

    # Cenário alternativo: atualizar tarefa inexistente
    def test_atualizar_tarefa_inexistente(self):
        tarefas = {}
        with self.assertRaises(KeyError):
            tarefas[999].titulo = "Novo título"

    # Cenário alternativo: deletar todas as tarefas e tentar listar
    def test_listar_tarefas_vazia(self):
        tarefas = {}
        # Simula a função listar_tarefas, espera que não haja tarefas
        self.assertEqual(len(tarefas), 0)

    # Cenário alternativo: criar várias tarefas e verificar se todas aparecem
    def test_criar_varias_tarefas(self):
        for i in range(1, 6):
            tarefa = Tarefa(i, f"Tarefa {i}", "Desc", "2024-03-17")
            self.tarefas[i] = tarefa
        self.assertEqual(len(self.tarefas), 5)
        for i in range(1, 6):
            self.assertIn(i, self.tarefas)

if __name__ == "__main__":
    unittest.main()
