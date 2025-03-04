import struct

K = [
    int(abs(2**32 * abs(i))) for i in [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
    ]
]

S = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

IV = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def left_rotate(x, amount):
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5_pad(message):
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    message += struct.pack('<Q', original_bit_len)
    return message

def md5(message):
    if isinstance(message, str):
        message = message.encode()

    message = md5_pad(message)

    a, b, c, d = IV

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        M = struct.unpack('<16I', chunk)

        A, B, C, D = a, b, c, d

        for j in range(64):
            if j < 16:
                F = (B & C) | (~B & D)
                g = j
            elif j < 32:
                F = (D & B) | (~D & C)
                g = (5*j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                g = (3*j + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7*j) % 16

            F = (F + A + K[j] + M[g]) & 0xFFFFFFFF
            A, D, C, B = D, (B + left_rotate(F, S[j])) & 0xFFFFFFFF, B, C

        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF

    return ''.join(f'{x:08x}' for x in [a, b, c, d])
    
text = "Hello, World!"
print("MD5 Hash:", md5(text))
