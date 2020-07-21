def minion_game(string):
    vowel_player = 0
    cons_player = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowel_player += len(string) - i
        else:
            cons_player += len(string) - i
    
    if cons_player > vowel_player:
        print('Stuart '+str(cons_player))
    elif vowel_player > cons_player:
        print('Kevin '+str(vowel_player))
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)