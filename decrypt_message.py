from sys import stdin

import secrets

e, n = secrets.public
d, _ = secrets.private


def unmap(c):
    c = int(c)
    if c == 27:
        return ' '
    else:
        return chr(c+96)


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
    print('Entrer le message reçu :')
    message = stdin.readline()
    print('Entrer la signature reçu :')
    sig = stdin.readline()
    print('Entrez la clef publique de l\'expéditeur :')
    e_p, n_p = [int(s) for s in stdin.readline().split(',')]

    message = str.split(message, ' ')
    message = [str(pow(int(data), d, n)) for data in message]
    for i in range(0, len(message)):
        if len(message[i]) == 1:
            message[i] = '00'+message[i]
        elif len(message[i]) == 2:
            message[i] = '0'+message[i]

    message = str.join('', message)
    message = [message[i:i + 2] for i in range(0, len(message), 2)]
    if message[-1] == '00':
        message = message[0:-1]
    message = [unmap(c) for c in message]
    message = str.join('', message)

    print('Message : {}'.format(message))

    signature = [int(map(s)) for s in message]
    h = 2
    for data in signature:
        h += h * 2
        h += data
    h_m = h % 1000

    if h_m == pow(int(sig), e_p, n_p):
        print('Signature valide !')
    else:
        print('Signature invalide')
