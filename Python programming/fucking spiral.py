num = int(input())
mtrx = [[0] * num for i in range(num)]
start, end, counter = 0, num-1, 1
while counter <= (num ** 2):
    for i in range(start,end+1):
        mtrx[start][i] = counter
        counter += 1
    start += 1
    for j in range(start,end+1):
        mtrx[j][end] = counter
        counter += 1
    start,end=end,start
    end-=1
    start-=1
    for k in range(start,end-1,-1):
        mtrx[start+1][k] = counter
        counter += 1
    end+=1
    for s in range(start,end-1,-1):
        mtrx[s][end-1] = counter
        counter += 1
    start,end=end,start

for i in mtrx:
    print('\t')
    for j in i:
        print(j, end=' ')
