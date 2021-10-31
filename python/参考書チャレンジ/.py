def hangman(word):
    wrong = 0
    stages = ["",
              "________         ",
              "|                ",
              "|       |        ",
              "|       |        ",
              "|       ○       ",
              "|       |        ",
              "|　  ／ | ＼     ",
              "|       |        ",
              "|    ／   ＼     ",
              "|"
              ]
    rletters = list(word)
    board = ["_"] * len(list(word))
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("_".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print("".join(board))
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))

list = ["cat","dog","human","pig"]
import random
rdm_num = random.randint(0,len(list))
print(list[rdm_num])
rdm_word = list[rdm_num]
print(type(rdm_word))
hangman(rdm_word)
