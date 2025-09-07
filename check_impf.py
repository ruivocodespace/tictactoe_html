def check_imp(tab2, simbol, int_user): 
    if 0 <= int_user < 9:
        if tab2[int_user] == " ":
            tab2[int_user] = simbol
            return True  
    return False
