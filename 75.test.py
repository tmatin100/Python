# pyllnt
# pyflakes  
# PEP8

# unitttest : https://docs.python.org/3/library/unittest.html

import unittest
# import the name of the file you want to run unit test on 
import main 

# we create a test class and  inherit the TestCase funcion from he unittest module
class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self): 
        '''HIIIIIII!!!!!'''
        test_param = 10 
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print('cleaning up')

# only run this code if this is the main file thats being run 
if __name__ == '__main__':
    unittest.main()
