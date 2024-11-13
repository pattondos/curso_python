import unittest
import cambia_texto

class CambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "qué onda maik"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "qué ONDA MAIK")


if __name__ == '__main__':
    unittest.main()