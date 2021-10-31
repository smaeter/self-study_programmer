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
            win = True
            input("")
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))
        input("")
        
crt_list = ["cat","dog","human","pig"]
import random
hangman(random.choice(crt_list))
