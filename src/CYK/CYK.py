def CYKParser(token, CNF):
    N = len(token)
    T = [[set([]) for j in range(N)] for i in range(N)]
    for i in range(0, N):
        for left, rule in CNF.items():
            for right in rule:    
                if len(right) == 1 and right[0] == token[i]:
                    T[i][i].add(left)
        for j in range(i, -1, -1):     
            for k in range(j, i):  
                for left, rule in CNF.items():
                    for right in rule:
                        if len(right) == 2 and right[0] in T[j][k] and right[1] in T[k + 1][i]:
                            T[j][i].add(left)
    if 'S' in T[0][N-1]:
        print("Selamat, program kamu bisa di compile 🤣")
    else:
        print("Maaf anda kurang beruntung, silahkan coba lagi 😔")
      
if __name__ == "__main__":
    pass