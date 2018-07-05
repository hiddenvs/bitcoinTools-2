#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prerequisites:
    1.安装python3.6
    2.安装protobuf,  pip3 install protobuf
    3.去学习下protobuf,
    4.protoc --python_out=. .\messages.proto
    5.
"""

import messages_pb2 as tz_messages
import types_pb2
import config_pb2
import storage_pb2

import struct

"""
param:
input:
    @string_input, e.g. '3f 23 23 00  26 00 00 00  28 08 b1 80  80 80 08 08  80 80 80 80  08 08 80 80  80 80 08 08  00 08 00 12 05 48 65 6c  6c 6f 1a 07  42 69 74 63  6f 69 6e 20  04 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
"""

def str2int (string_input, output_file_name = 'message.bin'):
    this_str = string_input
    str_list = this_str.split()  #string & list

    msg_id = int(str_list[3] + str_list[4], 16)
    print('Message ID:', msg_id)
    msg_size = int(str_list[5] + str_list[6] + str_list[7] + str_list[8], 16)
    print('Message Size:', msg_size)

    this_bin = []  # interger & list
    for a in str_list:
        this_bin.append( int(a, 16))
        
    this_bin = this_bin[9:9+msg_size:]  # delet ?## , msg_id, msg_size
    this_len = len(this_bin)

    fp = open(output_file_name, 'wb')
    binbuf = struct.pack(str(this_len)+'B', *this_bin)
    fp.write(binbuf)
    fp.close()
    return [msg_id, binbuf]


"""
function: 反序列化, 从给定的二进制str解析得到message对象
"""
def Deserialization(msg_id, message):
    if msg_id == 38:
        print('MessageType_SignMessage: ', message)
        signmessage = tz_messages.SignMessage()
        signmessage.ParseFromString(message)
        print(signmessage)
        print('Type:', type(signmessage.message))  # print int class
        print('Len:', len(signmessage.message))
        for val in signmessage.message:
            print(val)
    elif msg_id == 39:
        print('MessageType_VerifyMessage: ', message)
        verify_message = tz_messages.VerifyMessage()
        verify_message.ParseFromString(message)  # SerializeToOstream
        print(verify_message)
    elif msg_id == 40:
        print('MessageType_MessageSignature: ', message)
        signature_message = tz_messages.MessageSignature()
        signature_message.ParseFromString(message)
        print(signature_message)
        hex_list = []
        for val in signature_message.signature:
            hex_list.append(hex(val))
        print('Signature:', hex_list)
    elif msg_id == 0:
        print('MessageType_Initialize: ', message)
        init_message = tz_messages.Initialize()
        init_message.ParseFromString(message)
        print(init_message)
    elif msg_id == 55:
        print('MessageType_GetFeatures: ', message)
        getFeatures_message = tz_messages.GetFeatures()
        getFeatures_message.ParseFromString(message)
        print(getFeatures_message)
    elif msg_id == 17:
        print('MessageType_Features: ', message)
        features_message = tz_messages.Features()
        features_message.ParseFromString(message)
        print(features_message)
        
    elif msg_id == 11:
        print('MessageType_GetPublicKey: ', message)
        GetPublicKey_message = tz_messages.GetPublicKey()
        GetPublicKey_message.ParseFromString(message)
        print(GetPublicKey_message)
    elif msg_id == 12:
        print('MessageType_PublicKey: ', message)
        PublicKey_message = tz_messages.PublicKey()
        PublicKey_message.ParseFromString(message)
        print(PublicKey_message)
    elif msg_id == 29:
        print('MessageType_GetAddress: ', message)
        GetAddress_message = tz_messages.GetAddress()
        GetAddress_message.ParseFromString(message)
        print(GetAddress_message)
    elif msg_id == 30:
        print('MessageType_Address: ', message)
        Address_message = tz_messages.Address()
        Address_message.ParseFromString(message)
        print(Address_message)
    else:
        print('Unrecognized Message Id, Please modify the program.')

def main():

    buffer_sign = '3f 23 23 00  26 00 00 00  28 08 b1 80  80 80 08 08  80 80 80 80  08 08 80 80  80 80 08 08  00 08 00 12 \
        05 68 65 6c  6c 6f 1a 07  42 69 74 63  6f 69 6e 20  04 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_signature = '3f 23 23 00  28 00 00 00  67 0a 22 33  4a 59 4c 50  34 6b 4a 41  6b 73 63 59  54 53 45 70  70 74 32 4b \
        67 51 37 63  72 59 74 46  52 48 52 33  42 12 41 23  d2 9b 4a 99  77 ec 59 53  88 1f f5 e8  76 d1 50 ca \
        3f e6 c7 68  5b 21 24 a6  07 30 46 8a  62 8e 7b 4a  11 46 57 61  8c 05 a5 27  79 d2 a3 d3  4c d7 b6 32 \
        a0 d3 16 73  1f 2a 74 43  d7 76 0a 91  23 ba 60 4c  67 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_verify = '3f 23 23 00  27 00 00 00  77 0a 22 33  4c 56 52 6a  79 79 48 65  64 6d 39 66  77 64 73 4a  72 4a 71 47 \
        55 44 39 44  62 55 6b 6e  41 59 46 78  43 12 41 24  e5 9a 65 63  bb fa 01 8d  a3 08 40 6d  0c 83 61 46 \
        33 6e 20  76 0f 1d 17  a6 29 1e 7c  d6 08 c3 bc  4f 48 7c 2a  c8 a1 30 95  39 b2 8a c5  da 7a 0e 80 \
        ad f6 36 84  8c e2 65 2f  c2 75 a0 2d  cd 7a b2 58  93 1a 05 48  65 6c 6c 6f  22 07 42 69  74 63 6f 69 \
        6e 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'

    buffer_init = '3f 23 23 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_getfeature = '3f 23 23 00  37 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_features = '3f 23 23 00  11 00 00 00  8b 0a 11 62  69 74 63 6f  69 6e 74 72  65 7a 6f 72  2e 63 6f 6d  10 01 18 06 \
        20 02 32 18  35 38 30 43  37 34 36 39  43 44 43 37  39 43 32 32  34 31 38 44  36 42 39 30  38 01 40 00 \
        52 06 61  6e 64 72 65  77 60 01 6a  14 c9 11 3f  d3 f5 fc d7  8e 9e 56 0d  ba c7 5e d5  aa e3 59 eb \
        2d 72 20 af  b4 cf 7a 4a  57 96 10 0e  d5 41 6b 75  12 1b c7 10  08 c2 a2 fd  54 49 bd 8f  63 cc 22 a6 \
        a7 d6 80  78 00 80 01  01 88 01 00  98 01 00 a0  01 00 aa 01  01 31 00 00  00 00 00 00  00 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'

    buffer_getPublicKey1 = '3f 23 23 00  0b 00 00 00  1b 08 b1 80  80 80 08 08  80 80 80 80  08 08 80 80  80 80 08 22  07 42 69 74 \
        63 6f 69 6e  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_getPublicKey2 = '3f 23 23 00  0b 00 00 00  1d 08 b1 80  80 80 08 08  80 80 80 80  08 08 80 80  80 80 08 08  00 22 07 42 \
        69 74 63 6f  69 6e 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_pubkey1 = '3f 23 23 00  0c 00 00 00  c6 0a 53 08  03 10 bb e0  f7 8a 0c 18  80 80 80 80  08 22 20 14  bc fd 3c 68 \
        1a 62 06 27  3c 35 b1 b1  2c 99 94 e3  12 65 4e 61  0b fd 96 a4  34 83 5e 10  eb 61 dc 32  21 03 4d 02 \
        4d 05 ae  24 9e c5 5a  33 66 8c 6a  4c e5 c7 6f  d9 79 18 e9  4f a2 27 97  c4 5d 0c 6b  f3 f8 27 12 \
        6f 78 70 75  62 36 44 35  43 6a 75 53  51 44 59 73  5a 32 6d 69  51 4b 39 6b  5a 75 6b 32  79 44 63 58 \
        36 62 64  62 59 61 42  36 32 6e 57  31 50 48 42  34 7a 54 31  52 59 79 42  6b 64 38 6a  6e 73 72 4d \
        79 6d 50 46  53 5a 38 5a  63 44 72 73  50 55 35 73  65 52 32 4b  6a 47 76 6f  50 68 71 41  50 59 52 62 \
        41 69 6d  53 73 41 4e  63 74 78 56  66 6a 46 65  33 6d 00 00  00 00 00 00  00 00 00 00  00 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    buffer_pubkey2 = '3f 23 23 00  0c 00 00 00  c2 0a 4f 08  04 10 e2 fb  ac f6 04 18  00 22 20 b3  27 6d aa 95  ce e0 59 84 \
        93 99 8d 8a  80 29 0e 74  91 6d 83 e3  f2 5d 5e 90  ad 37 6f ca  52 2b 22 32  21 02 01 1b  d7 25 2e 7f \
        7a 48 65  f2 cb 70 c9  2e c7 41 9b  00 dd 54 07  d8 f8 dc 2c  1d 08 6c 27  cb 73 22 12  6f 78 70 75 \
        62 36 45 37  56 66 58 4c  77 75 70 4b  33 52 53 56  4b 4e 4e 45  6f 72 44 64  72 76 32 79  45 75 36 68 \
        63 57 61  74 55 78 51  45 62 4a 52  4d 33 4b 46  53 39 76 75  7a 7a 55 33  45 4b 4b 4d  4a 74 41 6e \
        71 32 52 47  56 34 73 53  62 7a 70 59  50 59 4a 75  35 35 77 44  36 6a 5a 47  58 74 54 48  76 38 68 7a \
        33 6f 36  58 6b 53 67  65 39 31 66  71 53 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 '

    buffer_GetAddress = '3f 23 23 00  1d 00 00 00  23 08 b1 80  80 80 08 08 \
        80 80 80 80  08 08 80 80  80 80 08 08  00 08 00 12 \
        07 42 69 74  63 6f 69 6e  18 00 28 04  00 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 '
    buffer_Address = '3f 23 23 00  1e 00 00 00  24 0a 22 33  4c 79 4e 42 \
        56 53 41 51  71 50 31 73  73 75 41 46  58 71 63 45 \
        46 50 72 4e  43 74 62 73  77 54 67 58  39 00 00 00 \
        00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 '

    buffer_test = '3f 23 23 00 28 00 00 00 67 0a 22 31 39 35 54 32 \
        35 41 62 35 44 75 39 44 36 37 75 32 42 6d 44 76 \
        46 64 39 50 68 4c 61 64 52 7a 72 7a 78 12 41 20 \
        fe e2 43 ec 4f 1a f9 2a 73 09 f6 a5 43 d5 7a ee \
        04 1e a7 69 74 57 96 53 ff 9b f3 d8 6a c3 af 34 \
        1b 66 52 f5 a1 16 30 b8 cb f8 61 33 5b b5 95 68 \
        1d b7 13 af 0 3a a6 94 1a 69 58 bf 8f 18 e1 96 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
    
    message_info = str2int(buffer_test)
    Deserialization(message_info[0], message_info[1])
    

if __name__ == '__main__':
    main()
