import unittest
from painel_tarefas import executar_painel

class TestPainelTarefas(unittest.TestCase):
    def test_nenhuma_tarefa(self):
        msg = executar_painel("Rodrigo", "Sao Paulo", [])
        self.assertEqual(msg, "Nenhuma tarefa cadastrada.")

    def test_rotina_leve(self):
        msg = executar_painel("Rodrigo", "Sao Paulo", ["Estudar Python"])
        self.assertEqual(msg, "Rodrigo de Sao Paulo: rotina leve hoje!")

        msg2 = executar_painel("Rodrigo", "Sao Paulo", ["Estudar Python", "Fazer compras"])
        self.assertEqual(msg2, "Rodrigo de Sao Paulo: rotina leve hoje!")

    def test_rotina_cheia(self):
        tarefas = ["Estudar Python", "Fazer compras", "Treinar academia", "Reuniao de trabalho"]
        msg = executar_painel("Rodrigo", "Sao Paulo", tarefas)
        self.assertEqual(msg, "Rodrigo de Sao Paulo: rotina cheia! Organize prioridades.")

if __name__ == "__main__":
    unittest.main()
