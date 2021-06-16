class Color:
    def __init__(self, R, G, B):
        self.RGB=(R,G,B)
        self.negative=(255-R, 255-G, 255-B)

class Cube:
    def __init__(self, id, weight, colors, height, width, depth):
        self.id=id
        self.weight=weight
        self.colors=colors
        self.heights=[height, width, depth, depth, width, height]

def print_cubes_seq(cubes):
    print("The sequence of cubes is: "+" ".join([str(cube.id) for cube in cubes]))

def print_cubes_routiotion(p, i, j):
    if i==-1:
        return
    print_cubes_routiotion(p, i-1, p[i][j])
    print(j+1, end=" ")
    return

def solve(cubes):
    n=len(cubes)
    cubes.sort(key=lambda x: x.weight, reverse=True)
    dp=[[0]*(6) for i in range(n)]
    p=[[None]*6 for i in range(n)]
    for i in range(6):
        dp[0][i]=cubes[0].heights[i]
        p[0][i]=-1
    for i in range(1,n):
        for j in range(6):
            for k in range(6):
                if dp[i-1][k]+cubes[i].heights[j]>dp[i][j] and cubes[i].colors[j].RGB==cubes[i-1].colors[5-k].negative:
                    dp[i][j]=dp[i-1][k]+cubes[i].heights[j]
                    p[i][j]=k
    print("The highest height is: {}".format(max(dp[-1])))
    print_cubes_seq(cubes)
    print("The routiotion of cubes are:", end=" ")
    print_cubes_routiotion(p, n-1, dp[-1].index(max(dp[-1])))
    print()

if __name__=="__main__":
    print("Note: In this program we numbering each side of each cube in this way:")
    print("Down=1, Left=2, Front=3, Back=4, Right=5, Up=6")
    print("In the solution, each number represents the side number of the cube at the bottom.")
    n=int(input("Enter number of cubes: "))
    cubes=[]
    for i in range(n):
        id=i+1
        print("Cube #{}:".format(id))
        weight=int(input("Weight: "))
        colors=[]
        for j in range(6):
            R, G, B=map(int,input("Enter color of side #{}: ".format(j+1)).split())
            colors.append(Color(R, G, B))
        height, width, depth=map(int,input("Enter height, width and depth: ").split())
        cubes.append(Cube(id, weight, colors, height, width, depth))
    solve(cubes)
