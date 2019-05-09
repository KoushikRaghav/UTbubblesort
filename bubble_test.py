import unittest
import bubble
class knownvalues(unittest.TestCase):
	def test_sort(self):
		arr = [64, 34, 25, 12, 22, 11, 90]
		result = bubble.bubblesort(arr)
		expected = 11 12 22 25 34 64 90 
		self.assertEqual(expected,result)

if __name__ == '__main__':
	unittest.main()
