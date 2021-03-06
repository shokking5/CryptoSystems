#!/usr/bin/env python3
# -- coding: utf-8 --

from elgamal import *


def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] To string')
    print('[4] Exit')
    return input()


elg = Generate()  # 1024 default

while True:
    choice = menu()

    if choice == '1':
        m = input('\nPlaintext > ').strip()
        print('\nEncrypted: ' + str(elg.encrypt(m)))

    elif choice == '2':
        print('\nCipher > ')
        a = int(input('a > ').strip())
        b = int(input('b > ').strip())
        m = elg.decrypt(a, b)
        print('\nDecrypted: ' + str(m))

    elif choice == '3':
        m = int(input("\nHex > ").strip())
        print("\nMessage: " + unhexlify(hex(m)[2:]).decode("utf-8"))
    elif choice == '4':
        print('Bye!')
        break

    else:
        continue
