import unittest
from tarefas_crud import Tarefa, validar_data

class TestTarefaCRUD(unittest.TestCase):
    def setUp(self):
        self.tarefas = {}
        self.next_id = 1

    def test_titulo_varios(self):
        # Testa vários títulos válidos e inválidos
        titulos_validos = [f"Tarefa {i}" for i in range(25)]
        titulos_invalidos = ["", "   ", "\n", "\t"]
        for titulo in titulos_validos:
            with self.subTest(titulo=titulo):
                tarefa = Tarefa(self.next_id, titulo, "Desc", "2024-03-17")
                self.assertEqual(tarefa.titulo, titulo.strip())
        for titulo in titulos_invalidos:
            with self.subTest(titulo=titulo):
                tarefa = Tarefa(self.next_id, titulo, "Desc", "2024-03-17")
                self.assertEqual(tarefa.titulo, "")

    def test_datas_varias(self):
        # Testa várias datas válidas e inválidas
        datas_validas = [f"2024-03-{str(i).zfill(2)}" for i in range(1, 21)]
        datas_invalidas = ["2024-02-30", "2024-13-01", "2024-00-10", "2024-03-32", "2024-31-12", "", "17-03-2024"]
        for data in datas_validas:
            with self.subTest(data=data):
                self.assertTrue(validar_data(data))
        for data in datas_invalidas:
            with self.subTest(data=data):
                self.assertFalse(validar_data(data))

    def test_criar_e_deletar_varias_tarefas(self):
        # Cria e deleta várias tarefas
        for i in range(1, 16):
            tarefa = Tarefa(i, f"Tarefa {i}", "Desc", "2024-03-17")
            self.tarefas[i] = tarefa
        self.assertEqual(len(self.tarefas), 15)
        for i in range(1, 16):
            del self.tarefas[i]
        self.assertEqual(len(self.tarefas), 0)

    def test_remover_inexistente_varias_vezes(self):
        # Tenta remover vários IDs inexistentes
        for i in range(100, 110):
            with self.subTest(i=i):
                with self.assertRaises(KeyError):
                    del self.tarefas[i]

    def test_atualizar_inexistente_varias_vezes(self):
        # Tenta atualizar vários IDs inexistentes
        for i in range(200, 210):
            with self.subTest(i=i):
                with self.assertRaises(KeyError):
                    self.tarefas[i].titulo = "Novo"

    def test_criar_tarefas_combinacoes(self):
        # Cria tarefas com várias combinações de título, descrição e data
        for i in range(1, 11):
            for data in ["2024-03-17", "2024-02-29", "2024-12-31"]:
                tarefa = Tarefa(i, f"Tarefa {i}", f"Desc {i}", data)
                self.assertEqual(tarefa.titulo, f"Tarefa {i}")
                self.assertEqual(tarefa.descricao, f"Desc {i}")
                self.assertEqual(tarefa.data, data)

    def test_acessar_tarefa_removida_varias_vezes(self):
        # Cria e remove tarefas, depois tenta acessar
        for i in range(1, 6):
            tarefa = Tarefa(i, f"Tarefa {i}", "Desc", "2024-03-17")
            self.tarefas[i] = tarefa
        for i in range(1, 6):
            del self.tarefas[i]
            with self.subTest(i=i):
                with self.assertRaises(KeyError):
                    _ = self.tarefas[i]

    def test_listar_tarefas_vazia(self):
        self.assertEqual(len(self.tarefas), 0)

    def test_criar_varias_tarefas_e_verificar(self):
        for i in range(1, 21):
            tarefa = Tarefa(i, f"Tarefa {i}", "Desc", "2024-03-17")
            self.tarefas[i] = tarefa
        self.assertEqual(len(self.tarefas), 20)
        for i in range(1, 21):
            self.assertIn(i, self.tarefas)

if __name__ == "__main__":
    unittest.main()
