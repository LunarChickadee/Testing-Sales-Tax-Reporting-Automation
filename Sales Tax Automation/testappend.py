inp = "[1, 2, 3]"
lst = [int(x) for x in re.findall(r'\d+', inp)]
print(lst)  # [1, 2, 3]