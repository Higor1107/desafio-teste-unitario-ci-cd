import unittest
from tarefas_crud import Tarefa, validar_data

class TestTarefaCRUD(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
