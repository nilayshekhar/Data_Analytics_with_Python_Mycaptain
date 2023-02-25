def set_operations ():
    n1 = int(input('Enter range for A: '))

    set1 = set()

    for _ in range(n1):
        item1 = int(input('Enter Item: '))
        set1.add(item1)

    n2 = int(input('Enter range for B: '))
    set2 = set()

    for _ in range(n2):
        item2 = int(input('Enter Item: '))
        set2.add(item2)

    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    symmetric_difference_set = set1.symmetric_difference(set2)

    print(f'Union: {union_set}')
    print(f'Intersection: {intersection_set}')
    print(f'Difference: {difference_set}')
    print(f'Symmetric Difference: {symmetric_difference_set}')

set_operations()