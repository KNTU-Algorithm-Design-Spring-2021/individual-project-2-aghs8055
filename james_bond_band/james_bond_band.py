import json
with open("words_dictionary.json", 'r') as fp:
    words=json.load(fp)
string=input().lower()
n=len(string)
path=[-1]*(n+1)
path[n]=n
dp=[[-1]*(n+1) for i in range(n+1)]
dp[-1][-1]=""
for i in range(n-1,-1,-1):
    for j in range(n,i,-1):
        if string[i:j] in words and path[j]!=-1:
            dp[i][j]=path[j]
            path[i]=j
            break
i=0
while i!=n:
    print(string[i:path[i]],end=" ")
    i=path[i]
