def check_win(tab): 
    #Verifica vitória ou empate
    combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in combos:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] != " ":
            return True, tab[combo[0]]  # vitória
    if " " not in tab:
        return "empate", None          # empate
    return False, None                 # jogo continua
