print('==========')
print('Set Operations')
print('==========')
A = {10,20,30,40}

B = {30,40,50,60}
print(f'Union of sets: {A.union(B)}')
print(f'Intersection of sets: {A.intersection(B)}')
print(f'Difference A-B: {A.difference(B)}')
print(f'Difference B-A: {B.difference(A)}')
