#tkinter ile arayüz yapilacak cogu fonks. ve degisken isimleri turkceye cevirelecek.
#YEKTA OKDAN 210404053


#tahtayi 4x4 olarak tasarlamak uzere hucrelerini yaratiyoruz.
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3]+ '|' + board[4])
    print('-+-+-')
    print(board[5] + '|' + board[6] + '|' + board[7]+ '|' + board[8])
    print('-+-+-')
    print(board[9] + '|' + board[10] + '|' + board[11]+ '|' + board[12])
    print('-+-+-')
    print(board[13] + '|' + board[14] + '|' + board[15]+ '|' + board[16])
    print("\n")



#tahtadaki tum sutunlarin bos olup olmadigini kontrol eden kisim. eger bos ise true degil ise false donuyor.
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


#eger sutun bos ise kullanicidan alinan degere gore bos hucreye yerlesim yaptiriyoruz.
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Oyuncu X kazandı!!")
                exit()
            else:
                print("Oyuncu O kazandı!")
                exit()

        return

#yerlestirilmek istenen hucre doluysa hata ciktisi alip yeni bir girdi istiyoruz.
    else:
        print("Buraya yerleşemez!")
        position = int(input("Lütfen yeni pozisyon giriniz:  "))
        insertLetter(letter, position)
        return


#tum satir ve sutunların birbiriyle kontrolü saglaniyor. Yanyana olup olmamaları kazananı belirledigi icin bu durumda satır ve sutunlardaki hucrelerın yanyana olup olmadıklarını kontrol edıyoruz.
#orn XXXX veya OOOO
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1]==board[4] and board[1] != ' '):
        return True
    elif (board[5] == board[6] and board[5] == board[7] and board[5]==board[8] and board[5] != ' '):
        return True
    elif (board[9] == board[10] and board[9] == board[11] and board[9]==board[12] and board[9] != ' '):
        return True
    elif (board[13]==board[14]and board[13]==board[15] and board[13] == board[16]and board[13]!= ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] != ' '):
        return True
    elif (board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] != ' '):
        return True
    elif (board[3] == board[7] and board[3] == board[11] and board[3] == board[15] and board[3] != ' '):
        return True
    elif (board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] != ' '):
        return True
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16]  and board[1] != ' '):
        return True
    elif (board[13] == board[10] and board[13] == board[7] and board[13]==board[4]and board[13] != ' '):
        return True
    else:
        return False

#basta bilgisayar olan sonradan kullanici olarak tasarladigim girdi sahibinin kontrolleride burada saglaniyor.
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == mark):
        return True
    elif (board[5] == board[6] and board[5] == board[7]and board[5] == board[8] and board[5] == mark):
        return True
    elif (board[9] == board[10] and board[9] == board[11]and board[9] == board[12] and board[9] == mark):
        return True
    elif (board[13] == board[14]and board[13]==board[15]and board[13] == board[16]and board[13]== mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9]and board[1] == board[13] and board[1] == mark):
        return True
    elif (board[2] == board[6] and board[2] == board[10]and board[2] == board[14] and board[2] == mark):
        return True
    elif (board[3] == board[7] and board[3] == board[11]and board[3] == board[15] and board[3] == mark):
        return True
    elif (board[4] == board[8] and board[4] == board[12]and board[4] == board[16] and board[4] == mark):
        return True
    elif (board[1] == board[6] and board[1] == board[11]and board[1] == board[16]  and board[1] == mark):
        return True
    elif (board[13] == board[10] and board[13] == board[7] and board[13] == board[4]and board[13] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

#Oyuncu 2'nin girdisinin alindigi kisim.
def playerMove():
    position = int(input("'O' icin yeni pozisyon giriniz:  "))
    insertLetter(player, position)
    return
#Oyuncu 1'in girdisinin alindigi kisim.
def botMove():
    position = int(input("'X' icin yeni pozisyon giriniz:  "))
    insertLetter(bot, position)
    return


#def compMove():
   # bestScore = -800
    #bestMove = 0
    #for key in board.keys():
        #if (board[key] == ' '):
            #board[key] = bot
            #score = minimax(board, 0, False)
            #board[key] = ' '
            #if (score > bestScore):
                #bestScore = score
                #bestMove = key

    #nsertLetter(bot, bestMove)
    #return


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
         5: ' ', 6: ' ', 7: ' ', 8: ' ',
         9: ' ', 10: ' ', 11: ' ', 12: ' ',
         13: ' ', 14: ' ', 15: ' ', 16: ' '}

printBoard(board)
print("İlk biglisayar basliyor.. Bol sans!")
print("Tablo sutunlari..")
print("1, 2, 3, 4 ")
print("5, 6, 7, 8 ")
print("9, 10, 11, 12 ")
print("13, 14, 15, 16")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not checkForWin():
    botMove()
    playerMove()
