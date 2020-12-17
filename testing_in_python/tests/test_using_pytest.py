def get_largest_number(array1, array2):

   return max([max(array1), max(array2)])


# def test_largest1():
#    assert get_largest_number([1,3,6,9], [8,7,8])==9, 'Should be 9'

# def test_largest2():
#    assert get_largest_number([29,3,87,26], [16,97,4,12])==97, 'Should be 97'

# def test_largest3():   
#    assert get_largest_number([1,1,1,1,1,1,1], [1,1,1,1,1])==1, 'Should be 1'

def test_largest():
   assert get_largest_number([1,3,6,9], [8,7,8])==9, 'Should be 9'
   assert get_largest_number([1],[2])==1, 'Should raise AssertionError'
   assert get_largest_number([1,1,1,1,1,1,1], [1,1,1,1,1])==1, 'Should be 1'
