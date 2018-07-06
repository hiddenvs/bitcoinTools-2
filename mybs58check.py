#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install base58
"""

import base58

def str2int(buffer='8076f1b95aa61d6c8464ae303acc62eaafbec152157a3ad00b5ae7edf085ec4b6501'):
    buffer = ''.join(buffer.split())
##    print(buffer)
    i=0
    a = []
    while i<len(buffer):
        a.append(int(buffer[i:i+2:],16))
        i = i+2
    return a

def main():
    
    """Decode"""
    print('Decode: ', (base58.b58decode_check(b'195T25Ab5Du9D67u2BmDvFd9PhLadRzrzx')).hex())

    """Encode"""
    print('Encode: ', \
          base58.b58encode_check(\
              bytes(\
                  str2int('6f589863a5e966f33bf1e28c5cc2833fb3ab278647'))))
    
if __name__ == '__main__':
    main()
