def print_line(p,i):
        if i<0:
            return 1
        next_line=print_line(p,p[i]-1)
        print("Line {}: Word {} to {}".format(next_line, p[i]+1, i+1))
        return next_line+1
def calc(m, sum_size, i, j):
    temp=(m-(i-j)-(sum_size[i+1]-sum_size[j]))
    if i==len(sum_size)-2 and temp>0:
        return 0
    if temp>=0:
        return temp**3
    else:
        return float("inf")
m=int(input("Enter size of each line: "))
w=list(map(int,input("Enter size of each word: ").split()))
p=[0]*len(w)
sum_size=[0]
for i in w:
    sum_size.append(sum_size[-1]+i)
dp=[0]*len(w)
for i in range(len(w)):
    dp[i]=calc(m, sum_size, i, 0)
    for j in range(1,i+1):
        temp=calc(m, sum_size, i, j)
        if temp+dp[j-1]<dp[i]:
            dp[i]=temp+dp[j-1]
            p[i]=j
print_line(p,len(w)-1)
print("Minimum cost is:", dp[-1])
