# list1 = ['a' , 'c' , 'g', 'f' ,'a' , 'f'];
# list2 = [];
# #list2 = ['a','c','g','f']
# 
# for s in list1:
#     if s not in list2:
#         list2.append(s);
# print(list2);     
# 
# 
# list1 = ['a' , 'c' , 'g', 'f' ,'a' , 'f'];
# list2 = ['a' , 'c' , 'g', 'b' , 'f'];
# list3 = []
# 
# for n in list1 and list2:
#     if n not in list3:
#         list3.append(n);
# 
# print(list3)   


import unittest
from itertools import groupby


def compress_string(data):
    compressed = "".join(["{0}{1}".format(k, sum(1 for i in g))
                          for k, g in groupby(data)])

    if len(compressed) > len(data):
        return data
    else:
        return compressed


print(compress_string('aabcccccaaaa'));

class MyTest(unittest.TestCase):

    def test_compress_string(self):
        self.assertEqual(compress_string('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(compress_string('abcd'), 'abcd')
        self.assertEqual(compress_string('tTTttaAbBBBccDd'), 'tTTttaAbBBBccDd')

if __name__ == '__main__':
    unittest.main()
    