def cykParse(w, R):
    n = len(w)
    T = [[set([]) for j in range(n)] for i in range(n)]
    for j in range(0, n):
      for left, rule in R.items():
        for right in rule:    
          if len(right) == 1 and right[0] == w[j]:
            T[j][j].add(left)

      
      for i in range(j, -1, -1):     
        for k in range(i, j):  
          for left, rule in R.items():
            for right in rule:
              if len(right) == 2 and right[0] in T[i][k] and right[1] in T[k + 1][j]:
                T[i][j].add(left)
  
    if 'S' in T[0][n-1]:
        print("Selamat program kamu bisa di compile 🤣")
    else:
        print("maaf anda kurang beruntung,silahkan coba lagi 😔")
      
if __name__ == "__main__":
  pass