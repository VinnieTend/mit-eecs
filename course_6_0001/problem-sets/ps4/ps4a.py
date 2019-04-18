# Problem Set 4A
# Name: angelichorsey
# Collaborators: None
# Time Spent: like 5 hours, jeez recursion can be tricky

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

#   base case as a single character only has 1 permutation
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        
#       I need to determine what it means programmatically to have the
#       recursive case to be the iterations of a loop.
#         
#       strip the sequence's first character and return its permutations to
#       loop through
        
#       really need to come back to this to see how I can explain it...
        for permutation in get_permutations(sequence[1:]):
            for i in range(len(permutation)+1):
                permutations.append(permutation[:i] + sequence[:1] \
                                    +permutation[i:])
        return permutations
        # could also return without duplicates
        #return list(set(permutations))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input = 'yo'
    print('Input:', example_input)
    print('Expected Output:', ['yo', 'oy'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'wat'
    print('Input:', example_input)
    print('Expected Output:', ['wat', 'wta', 'twa', 'taw', 'awt', 'atw'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'rrr'
    print('Input:', example_input)
    print('Expected Output:', ['rrr']*6)
    print('Actual Output:', get_permutations(example_input))