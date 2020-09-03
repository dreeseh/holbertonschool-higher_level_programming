#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for ch in dir(hidden_4):
        if ch[0] != "_":
            print("{}".format(ch))
