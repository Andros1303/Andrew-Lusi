#Дитяча гра "Хрестики нолики"
# table of game
table = list(range(1,10))
def draw_table(table):
    print ("-" * 13)
    for i in range(3):
        print ("|", table[0+i*3], "|", table[1+i*3], "|", table[2+i*3], "|")
        print ("-" * 13)
# check mow 
def take_input(token):
    tit = False
    while not tit:
        answer = input("Where will we put " + token+"? ")
        try:
            answer = int(answer)
        except:
            print ("Invalid input. Are you sure you entered the number?")
            continue
        if answer >= 1 and answer <= 9:
            if (str(table[answer-1]) not in "XO"):
                table[answer-1] = token
                tit = True
            else:
                print ("This cell is already occupied")
        else:
            print ("Invalid input. Enter a number from 1 to 9 to walk.")
# check win straik
def check_win(table):
    win_strike = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(3,6,9),(0,4,8),(2,4,6))
    for each in win_strike:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False
# counter of points
def main(table):
    counter = 0
    win = False
    while not win:
        draw_table(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            cwt = check_win(table)
            if cwt:
                print (cwt, "Winning!")
                win = True
                break
        if counter == 9:
            print ("A draw!")
            break
    draw_table(table)
main(table)   