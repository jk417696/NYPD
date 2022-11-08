def persona(matrix):
    n = len(matrix)
    info = 'Nie ma osobistosci'
    for i in range(n):
        check = 0
        if matrix[i]==[1]*n:
            check = 1
            for j in range(n):
                if i!=j and matrix[j][i]==1:
                    check = 0
            if check == 1:
                info = 'Osoba '+ str(i)+ ' jest osobistoscia'
                return info
    return info


mat = [[1,0,1,1], [1,1,1,1], [0,0,1,1], [1,1,1,1]]
print(persona(mat))







