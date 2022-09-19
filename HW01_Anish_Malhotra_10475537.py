import unittest
def classify_triangle(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if (a + b> c) and (b + c > a) and (c + a > b):
        if(a == b) and (b == c): return "The Triangle is equilateral"
        elif (a == b) or (b == c) or (c==a): return "The Triangle is isosceles"
        elif (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b): return "The Triangle is right angle"
        else: return ("The Triangle is scalen")
    else: return ("Triangle is not possible with the given input")

class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        """ test classify triangle function
            :rtype: None
            :return: None
        """
        message = 'yay passed'
        self.assertEqual(classify_triangle(3, 4, 5), 'The Triangle is right angle')
        self.assertEqual(classify_triangle(2, 3, 3), 'The Triangle is isosceles')
        self.assertEqual(classify_triangle(10, 15, 30), 'Triangle is not possible with the given input')
        self.assertEqual(classify_triangle(19, 12, 11), 'The Triangle is scalen')
        self.assertEqual(classify_triangle(3,3,3), 'The Triangle is equilateral')
        

    def testSet2(self): 
        """ test classify triangle function
            :rtype: None
            :return: None
        """

        self.assertNotEqual(classify_triangle(233, 233, 233), 'The Triangle is isosceles')
        self.assertNotEqual(classify_triangle(1, 2, 3), 'The triangle is scalen')
        self.assertEqual(classify_triangle(10, 10, 1), 'The triangle is scalen') 
        

    def testSet3(self):
        """ test classify triangle function
            :rtype: None
            :return: None
        """

        self.assertNotEqual(classify_triangle(10, 10, 9), 'The Triangle is right angle')
        self.assertEqual(classify_triangle(3, 4, 5), 'The Triangle is equilateral')

if __name__ == '__main__':
    
    unittest.main()
