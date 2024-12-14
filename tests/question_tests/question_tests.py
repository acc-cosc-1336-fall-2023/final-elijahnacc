#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.c_functions import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        initial_strand = "GATATATGCATATACTT"
        second_strand = "ATAT"
        print(get_most_likely_ancestor_consensus(initial_strand, second_strand))
        position1, position2, position3 = get_most_likely_ancestor_consensus(initial_strand, second_strand)
        self.assertEqual(position1, 2)
        self.assertEqual(position2, 4)
        self.assertEqual(position3, 10)