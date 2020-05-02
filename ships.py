from random import randint
from random import choice
from oreol import Oreol


def rand_coordinate():
    return randint(0, 9)


def random_sign(fcoord, scoord):
    if fcoord == 0 and scoord not in (0, 9):
        sign = choice([[fcoord + 1, scoord], [fcoord, scoord + 1], [fcoord, scoord - 1]])
    elif fcoord == 9 and scoord not in (0, 9):
        sign = choice([[fcoord - 1, scoord], [fcoord, scoord + 1], [fcoord, scoord - 1]])
    elif scoord == 0 and fcoord not in (0, 9):
        sign = choice([[fcoord, scoord + 1], [fcoord + 1, scoord], [fcoord - 1, scoord]])
    elif scoord == 9 and fcoord not in (0, 9):
        sign = choice([[fcoord, scoord - 1], [fcoord + 1, scoord], [fcoord - 1, scoord]])
    elif fcoord == 9 and scoord == 0:
        sign = choice([[fcoord - 1, scoord], [fcoord, scoord + 1]])
    elif fcoord == 0 and scoord == 9:
        sign = choice([[fcoord + 1, scoord], [fcoord, scoord - 1]])
    elif fcoord == 9 and scoord == 9:
        sign = choice([[fcoord - 1, scoord], [fcoord, scoord - 1]])
    elif fcoord == 0 and scoord == 0:
        sign = choice([[fcoord + 1, scoord], [fcoord, scoord + 1]])
    else:
        sign = choice([[fcoord + 1, scoord], [fcoord - 1, scoord], [fcoord, scoord + 1], [fcoord, scoord - 1]])
    return sign


class Ships:

    def __init__(self):
        orl = Oreol()
        self._oreol = orl
        self.ships = list()

    # 1P = 4
    def desk1(self):
        while len(self.ships) <= 3:
            fcoord = rand_coordinate()
            scoord = rand_coordinate()
            if [fcoord, scoord] not in self._oreol.oreol:
                self.ships.append([fcoord, scoord])
                self._oreol.add_oreol(fcoord, scoord)
        return self.ships

    # 2P = 3
    def desk2(self):
        self.ships.clear()
        while len(self.ships) <= 4:
            fcoord = rand_coordinate()
            scoord = rand_coordinate()
            sign = random_sign(fcoord, scoord)
            if [fcoord, scoord] not in self._oreol.oreol and sign not in self._oreol.oreol:
                self.ships.append([fcoord, scoord])
                self._oreol.add_oreol(fcoord, scoord)
                self.ships.append(sign)
                self._oreol.add_oreol(sign[0], sign[1])
        return self.ships

    # 3P = 2
    def desk3(self):
        self.ships.clear()
        while len(self.ships) <= 3:
            fcoord = rand_coordinate()
            scoord = rand_coordinate()
            sign = random_sign(fcoord, scoord)
            if fcoord == sign[0]:
                if max(scoord, sign[1]) + 1 > 9:
                    res = min(scoord, sign[1]) - 1
                else:
                    res = max(scoord, sign[1]) + 1
                sign2 = [fcoord, res]
            else:
                if max(fcoord, sign[0]) + 1 > 9:
                    res = min(fcoord, sign[0]) - 1
                else:
                    res = max(fcoord, sign[0]) + 1
                sign2 = [res, scoord]

            if [fcoord, scoord] not in self._oreol.oreol and sign not in self._oreol.oreol and sign2 not in self._oreol.oreol:
                self.ships.append([fcoord, scoord])
                self._oreol.add_oreol(fcoord, scoord)
                self.ships.append(sign)
                self._oreol.add_oreol(sign[0], sign[1])
                self.ships.append(sign2)
                self._oreol.add_oreol(sign2[0], sign2[1])
        return self.ships

    # 4P = 1
    def desk4(self):
        self.ships.clear()
        while len(self.ships) <= 1:
            fcoord = rand_coordinate()
            scoord = rand_coordinate()
            sign = random_sign(fcoord, scoord)
            if fcoord == sign[0]:
                if max(scoord, sign[1]) + 1 > 9:
                    res = min(scoord, sign[1]) - 1
                else:
                    res = max(scoord, sign[1]) + 1
                sign2 = [fcoord, res]
            else:
                if max(fcoord, sign[0]) + 1 > 9:
                    res = min(fcoord, sign[0]) - 1
                else:
                    res = max(fcoord, sign[0]) + 1
                sign2 = [res, scoord]

            if fcoord == sign[0] == sign2[0]:
                if max(scoord, sign[1], sign2[1]) + 1 > 9 and min(scoord, sign[1], sign2[1]) != 0:
                    res = min(scoord, sign[1], sign2[1]) - 1
                else:
                    res = max(scoord, sign[1], sign2[1]) + 1
                sign3 = [fcoord, res]
            else:
                if max(fcoord, sign[0], sign2[0]) + 1 > 9 and min(fcoord, sign[0], sign2[0]) != 0:
                    res = min(fcoord, sign[0], sign2[0]) - 1
                else:
                    res = max(fcoord, sign[0], sign2[0]) + 1
                sign3 = [res, scoord]

            if (
                [fcoord, scoord] not in self._oreol.oreol
                and sign not in self._oreol.oreol
                and sign2 not in self._oreol.oreol
                and sign3 not in self._oreol.oreol
            ):
                self.ships.append([fcoord, scoord])
                self._oreol.add_oreol(fcoord, scoord)
                self.ships.append(sign)
                self._oreol.add_oreol(sign[0], sign[1])
                self.ships.append(sign2)
                self._oreol.add_oreol(sign2[0], sign2[1])
                self.ships.append(sign3)
                self._oreol.add_oreol(sign3[0], sign3[1])
        return self.ships
