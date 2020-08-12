import random

#make a 4*4 matrix
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

#add 2 at random position
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2

#getting the current status of game
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'Game not end'

    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return 'Game not end'
    
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'Game not end'

    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'Game not end'

    return 'Lost'

# compress the matrix 
def compress(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)

    changed=False
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    changed=True
                pos+=1
    
    return new_mat,changed

#merge the two number which are same and at continous position
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                changed=True
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
    return mat,changed

#reverse the matrix
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

#transpose of matrix
def transpos(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


#movement of numbers
def move_left(mat):
    new_mat,changed1=compress(mat)
    new_mat,changed2=merge(new_mat)
    changed=changed1 or changed2
    final_mat,changed3=compress(new_mat)
    return final_mat ,changed

def move_right(mat):
    reverse_mat=reverse(mat)
    new_mat,changed1=compress(reverse_mat)
    new_mat,changed2=merge(new_mat)
    changed=changed1 or changed2
    new_mat,changed3=compress(new_mat)
    final_mat=reverse(new_mat)
    return final_mat ,changed

def move_up(mat):
    transpos_mat=transpos(mat)
    new_mat1,changed1=compress(transpos_mat)
    new_mat2,changed2=merge(new_mat1)
    changed=changed1 or changed2
    new_mat3,changed3=compress(new_mat2)
    final_mat=transpos(new_mat3)
    return final_mat ,changed

def move_down(mat):
    transpos_mat=transpos(mat)
    reverse_mat=reverse(transpos_mat)
    new_mat,changed1=compress(reverse_mat)
    new_mat,changed2=merge(new_mat)
    changed=changed1 or changed2
    new_mat,changed3=compress(new_mat)
    new_mat=reverse(new_mat)
    final_mat=transpos(new_mat)
    return final_mat ,changed


