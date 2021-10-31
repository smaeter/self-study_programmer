pop = []
jpop = []

def collect_songs():
    song = "曲名を入力して下さい："
    ask = "p か j のどちらかを入力してください。qで終わります："

    while True:
        genre = input(ask)
        if genre == "q":
            break
                                                
        if genre == "p":
            p = input(song)
            pop.append(p)
                                                    
        elif genre == "j":
            j = input(song)
            jpop.append(j)
                                                    
        else:
            print("不正な数値です。")

    print("pop songs: " , pop)
    print("jpop songs: " , jpop)

collect_songs()
