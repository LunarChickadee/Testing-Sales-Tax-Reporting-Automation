import itertools


numbers = [1, 2, 3, 7, 7, 9, 10]
target = 10

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

print(result)