#!/usr/bin/env python
from encode import PasswordHash

def comp_hash(pc, psw1, psw2):
    print( "[COMP_HASH] psw1 = %s, psw2 = %s" % (psw1, psw2));
    psw1 = pc.encrypt(psw1)
    if pc.decrypt(psw1) == psw2:
        print("[COMP_HASH] true")
    else:
        print("[COMP_HASH] false")

def printPsw(pc, password):
    print( "[INPUT] %s" % password);
    print( "[OUTPUT] %s" % pc.encrypt(password));

def main():
    pc = PasswordHash()
    psw1 = 'pass123';
    psw2 = '123pass';
    printPsw(pc, psw1)
    printPsw(pc, psw2)
    comp_hash(pc, psw1, psw1)
    comp_hash(pc, psw1, psw2)

if __name__ == '__main__':
    main()
