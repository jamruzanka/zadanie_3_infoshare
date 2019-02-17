file = 'zadanie_4_triangle_big.txt'
GreatList = []
with open(file) as f:
    tri = f.readlines()
    for line in tri:
        GreatList.append([int(x) for x in line.strip().split(" ")])

def solve(triangle):
    while len(triangle) > 1:
        last_one = triangle.pop()
        second_last = triangle.pop()
        summed_row = []
        for i in range(len(second_last)):
            summed_row.append(max(last_one[i], last_one[i+1]) + second_last[i])
        triangle.append(summed_row)
    return triangle[0][0]
print(solve(GreatList))
