#!/usr/bin/env python

import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
	
	def test_suma_2_mas_2(self): #self se refiere al mismo objeto/por convencion todos los metodos deben llevar test
		cal = Calculator()		
		self.assertEqual(4, cal.summa(2,2))
	def test_resta_30_menos_X(self):
		cal = Calculator()
		self.assertEqual(26.5,cal.resta(30,3.5))
	def test_divide_30_entre_10(self):
		cal = Calculator()
		self.assertEqual(3,cal.divide(30,10))
	def test_multiplica_4_por_15(self):
		cal = Calculator()
		self.assertEqual(60,cal.multiplica(4,15))
if __name__ == "__main__":
	unittest.main()