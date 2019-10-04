#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
#
# class AcmeProductTests(unittest.TestCase):
#     def test_stealability(self):
#         prod2 = Product('2nd Product')
#         # kept getting error when I did assertEqual
#         # AssertionError: <bound method Product.stealability of <ac[36 chars]748>> != 0.5
#         # so tried with assertLess(prod2.stealability, 0.50)
#         # now giving TypeError: '<' not supported between instances of 'method' and 'float'
#
#         self.assertEqual(prod2.stealability, 0.50)
#
#     def test_explode(self):
#         bomb = Product('napalm')
#         # same thing when I try to do a test on explode().
#         # i just inputted 5 to see what it does...
#         # the trouble I'm having (I think) is testing for the if/else
#         #... statements?
#         self.assertEqual(bomb.explode, 5)

        # Hmm, what if I test instead one of the parameters from Class,
        # and not the method?
        # stealability is composed of price and weight.
    def testPrice(self):
        product_3 = Product('3rd Product')
        self.assertEqual(product_3.price, 10)

    def testWeight(self):
        product_4 = Product('4th Product')
        self.assertEqual(product_4.weight, 20)

        # doing both the testPrice and testWeight game me an ok test.
        # now how do I apply that with regards to stealability and exploding?

if __name__ == '__main__':
    unittest.main()
