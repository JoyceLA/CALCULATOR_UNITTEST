#!/usr/bin/env python
import unittest
##COMANDO DE JECUCION-> python ut.py
class TestEjemplo(unittest.TestCase): #Formato de la herencia
	def test_1(self):
		#pass #Numero automatico que regresa non
		self.assertEqual(1,1)
	def test_2(self):
		self.assertTrue(True)

if __name__=="__main__":#Si se esta ejecutando x modulo entonces hace este
	unittest.main()


