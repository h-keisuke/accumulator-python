import unittest

function = __import__('accumulator')
handler = function.lambda_handler


class TestFunction(unittest.TestCase):

    def test_function(self):
        event = [10, 20, 30]
        context = {'requestid': '1234'}
        result = handler(event, context)
        self.assertEqual(60, result)


if __name__ == '__main__':
    unittest.main()
