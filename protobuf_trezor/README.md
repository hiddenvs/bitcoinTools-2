# Test script of trezor protobuf is trezor_protobuf_test.py.

## Development environment
win10
python3.6

## Note
1.0x3f 0x23 0x23 is prefix that is a new protobuf message.
2.0x3f is a prefix for linking 64-byte messages.
3.script Input is a string e.g.
    '3f 23 23 00  26 00 00 00  28 08 b1 80  80 80 08 08  80 80 80 80  08 08 80 80  80 80 08 08  00 08 00 12 05 48 65 6c  6c 6f 1a 07  42 69 74 63  6f 69 6e 20  04 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00'
    a.delete 0x3f in the second article.
    b.keep 0x3f 0x23 0x23 in the first article.