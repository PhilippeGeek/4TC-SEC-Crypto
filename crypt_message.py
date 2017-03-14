from sys import stdin

import secrets

e, n = secrets.public
d, _ = secrets.private


def map(c):
    c = ord(c)
    if c in range(97, 97 + 26):
        c = c - 96
    else:
        c = 27
    if c < 10:
        return '0{}'.format(c)
    else:
        return '{}'.format(c)


while True:
    message = stdin.readline()
    message = str(message).lower()
    message = [map(c) for c in message]
    signature = [int(s) for s in message]

    message = str.join('', message)
    message = [message[i:i + 3] for i in range(0, len(message), 3)]
    if len(message[-1]) != 3:
        if len(message[-1]) == 1:
            message[-1] += '00'
        else:
            message[-1] += '0'
    print('Clef du destinataire :')
    e_p, n_p = [int(s) for s in stdin.readline().split(',')]
    message = [str(pow(int(data), e_p, n_p)) for data in message]
    print(str.join(' ', message))

    h = 2
    for data in signature:
        h += h * 2
        h += data

    signature = pow(h % 1000, d, n)
    print('Signature : {}'.format(signature))
