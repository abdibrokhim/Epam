# Data Types. Tuples. Task 2
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements. 
# The pairs should be formed as in the example. If there is only one element in the list, return [] instead.

# Example:

# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
# >>> get_pairs([1])
# []

from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # print('lst[1:]: ', lst[1:])

    return list(zip(lst, lst[1:]))
    # return list(zip([1, 2, 3, 8, 9], [2, 3, 8, 9]))

print(get_pairs([1, 2, 3, 8, 9])) # [(1, 2), (2, 3), (3, 8), (8, 9)]