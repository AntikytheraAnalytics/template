''' Module level doc string
'''
import unittest

class BasicTestCase(unittest.TestCase):
    ''' class level doc string
    '''

    def setUp(self):
        ''' non empty
        '''
        pass

    def tearDown(self):
        ''' non empty
        '''
        pass

    def test_basic(self):
        ''' non empty
        '''
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
