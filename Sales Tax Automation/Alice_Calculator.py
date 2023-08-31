import itertools

#put your numbers here
numbers = [1.2, 2.2, 3.3, 7.1, 7.2, 9.2, 10]
#put the target amount here
target = 11.6

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

print(result)