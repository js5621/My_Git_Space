import sys 

  

def MatrixChain(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    c = [[0 for x in range(n)] for x in range(n)]
    #print(c)
    for i in range(1, n): 
        m[i][i] = 0
        

      #  print(m)
       # print(c)
    for r in range(1, n-1): 
        for i in range(1, n-r): 
            j = i+r
            m[i][j] = sys.maxsize
           
            #print(m)
            for k in range(i, j):
                 
             
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                
                
             
                if q < m[i][j]: 
                    m[i][j] = q
                    c[i][j]= k
                    
    
    def Mat_Order(i,j):
        
        if i == j:
            print(chr(i+64),end='')
            
        else:
            print('(',end='')
            Mat_Order(i,c[i][j])
            Mat_Order(c[i][j]+1,j)
            print(')',end='')
           
    print('곱셈의 순서')
    Mat_Order(1,n-1)
    print("\n")
    return m[1][n-1]     
        

matNum=int(input("행렬의 개수를 입력하시오:"))
if matNum > 10:
    matNum = 10
arr=[]
site = input('각 행렬의 크기를 입력')
listx=site.split(' ')

for i in range(matNum+1):
   
    arr.append(int(listx[i]))


    
size = len(arr) 




print("전체 곱셈의 횟수 " +   str(MatrixChain(arr, size)))   

