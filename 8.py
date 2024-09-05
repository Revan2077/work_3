def islamic_nickname():
    travels = input()
    
    if travels == 'YYY' or travels == 'YYN' or travels == 'YNY' or travels == 'YNN':
        print('Haji')
    elif travels == 'NYY' or travels == 'NYN':
        print('Karbalaee')
    elif travels == 'NNY':
        print('Mashti')
    elif travels == 'NNN':
        print('Agha')
    else:
        return

islamic_nickname()
