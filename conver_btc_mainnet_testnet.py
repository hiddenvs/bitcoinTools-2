#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install base58

            Mainnet | Testnet
        ----------------------------
prikey |     0x80      0xef
pubkey |   0x03/0x02  0x03/0x02
adds   |   0x00/0x05   0x6f

"""

import base58

def str2int(buffer='8076f1b95aa61d6c8464ae303acc62eaafbec152157a3ad00b5ae7edf085ec4b6501'):
    buffer = ''.join(buffer.split())
    # print(buffer)
    i=0
    a = []
    while i<len(buffer):
        a.append(int(buffer[i:i+2:],16))
        i = i+2
    return a

def main():

    string_input = input('Input string:\n')
    # print(string_input)
    type_input = input('This is\n\
        1.Bitcoin private key\n\
        2.public key\n\
        3.address\n\
        Please input the index\n')
    if type_input == '1':
        type_input = 'prikey'
    elif type_input == '2':
        type_input = 'pubkey'
    elif type_input == '3':
        type_input = 'address'
    # print(type_input)

    try:
        str2int(string_input)
    except ValueError:
        string_type = 'base58ckeck'
    else:
        string_type = 'stringHEX'
    # print(string_type)

    if string_type == 'base58ckeck':  # Decode
        hex_string = base58.b58decode_check(bytes(string_input, 'ascii')).hex()
        bs58ck_string = bytes(string_input, 'ascii')
    else:
        hex_string = string_input
        bs58ck_string = base58.b58encode_check(bytes(str2int(string_input)))

    if type_input == 'prikey':
        mainnet_hex_string = '80' + hex_string[2::]
        testnet_hex_string = 'ef' + hex_string[2::]
    elif type_input == 'pubkey':
        mainnet_hex_string = hex_string
        testnet_hex_string = hex_string
    elif type_input == 'address':
        mainnet_Bitcoinn_hex_string = '00' + hex_string[2::]
        mainnet_ScriptPayment_hex_string = '05' + hex_string[2::]
        testnet_hex_string = '6f' + hex_string[2::]
            
    if type_input != 'address':
        print('Mainnet')
        print('Decode:', mainnet_hex_string)
        print('Encode:', base58.b58encode_check(bytes(str2int(mainnet_hex_string))))

        print('Testnnet')
        print('Decode:', testnet_hex_string)
        print('Encode:', base58.b58encode_check(bytes(str2int(testnet_hex_string))))
    else:
        print('Mainnet')
        print('Bitcoin address')
        print('Decode:', mainnet_Bitcoinn_hex_string)
        print('Encode:', base58.b58encode_check(bytes(str2int(mainnet_Bitcoinn_hex_string))))

        print('Script payment address')
        print('Decode:', mainnet_ScriptPayment_hex_string)
        print('Encode:', base58.b58encode_check(bytes(str2int(mainnet_ScriptPayment_hex_string))))

        print('Testnnet')
        print('Decode:', testnet_hex_string)
        print('Encode:', base58.b58encode_check(bytes(str2int(testnet_hex_string))))


if __name__ == '__main__':
    main()
