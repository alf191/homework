import math


def Perimetr(diametr):
    print(math.pi * d)

def squaere(diametr):
    l = d / 2
    print(math.pi * (l * l))
if __name__ == "__main__":
    d = int(input("Diametr skoworodki: "))
    print(Perimetr(d))
    print(squaere(d))

    
    Zadanie2.
    
    
    def find_entrance (f, n):

    x = n // (f * 4)
    e = x + 1
    print(e)
def find_floor(f, n):
    z = n % (f * 4)
    b = z // 4
    fl = b + 1
    print(fl)
if __name__ == "__main__":
    floors = int(input("Chislo etazei: "))
    flat_noom = int(input("Nomer kwartiry: "))
    entrance = find_entrance(floors, flat_noom)
    floor = find_floor(floors, flat_noom)
    print(entrance, floor)

    print()
