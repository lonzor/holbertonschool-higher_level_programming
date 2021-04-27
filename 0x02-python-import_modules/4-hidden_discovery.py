#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    mod = dir(hidden_4)
    for names in mod:
        if names[:2] != "__":
            print(names)
