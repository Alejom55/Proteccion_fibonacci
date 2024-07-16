import unittest
from app import app, fibonacci, sendEmailWithFibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        result = fibonacci(0, 0, 1)
        self.assertEqual(result, [0])

    def test_fibonacci_one(self):
        result = fibonacci(1, 0, 1)
        self.assertEqual(result, [0, 1])

    def test_fibonacci_sequence(self):
        result = fibonacci(5, 0, 1)
        self.assertEqual(result, [5, 3, 2, 1, 1, 1, 0])

    def test_sendEmailWithFibonacci(self):
        response_data = {
            "sequence": [0, 1, 1, 2, 3],
            "current_seconds": 10,
            "minutes": 15
        }
        result = sendEmailWithFibonacci(response_data)
        self.assertIn("Email sent successfully", result)

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fibonacci_endpoint(self):
        response = self.app.get('/fibonacci')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"sequence":', response.data)

    def test_fibonacciTime_valid(self):
        response = self.app.get('/fibonacci/12:34:56')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"sequence":', response.data)

    def test_fibonacciTime_invalid(self):
        response = self.app.get('/fibonacci/invalid_time_format')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid time format', response.data)

if __name__ == '__main__':
    unittest.main()