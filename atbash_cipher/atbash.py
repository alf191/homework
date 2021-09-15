import string

def atbash_code(j: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    y = j.lower().replace(' ','').translate(str.maketrans(' ', ' ', string.punctuation + '—'))

    return y.translate(str.maketrans(alphabet + alphabet.upper(), alphabet[::-1] + alphabet.upper()[::-1]))

def len_5(b: str):

    for i in range(0, len(b), 5):
        print(b[i: i + 5], end=' ')


print(len_5(atbash_code("Bambarbia, Kirgudu")))
