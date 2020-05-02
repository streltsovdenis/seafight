import sys

import time
from random import randint, choice
from ships import Ships
from oreol import Oreol


class HiddenBoard:
    def __init__(self):
        self.board = [["‎⬜"] * 10 for _ in range(10)]

    def __repr__(self):
        numbs = [" ", " ⓪", " ①", " ②", " ③", " ④", " ⑤", " ⑥", " ⑦", " ⑧", " ⑨"]
        print(" ".join([_ for _ in numbs]))
        stg = ""
        numbs = [" ⓪ ", " ① ", " ② ", " ③ ", " ④ ", " ⑤ ", " ⑥ ", " ⑦ ", " ⑧ ", " ⑨ "]
        for c, _ in enumerate(self.board):
            stg += str(numbs[c]) + " ".join(_) + "\n"
        return stg


class Board(HiddenBoard):
    def __init__(self):
        super().__init__()
        self.ships = Ships()
        self.p2 = list()
        self.p3 = list()
        self.p4 = list()
        for _ in self.ships.desk1():
            self.board[_[0]][_[1]] = "‎🚣"
        for _ in self.ships.desk2():
            self.board[_[0]][_[1]] = "‎⛵"
            self.p2.append(_)
        for _ in self.ships.desk3():
            self.board[_[0]][_[1]] = "‎🚢"
            self.p3.append(_)
        for _ in self.ships.desk4():
            self.board[_[0]][_[1]] = "‎⛴ "
            self.p4.append(_)

    def get_ships(self):
        return self.p2, self.p3, self.p4


class GamePlay:
    def __init__(self, auto=False):
        self.brd = Board()
        self.orl = Oreol()

        self.auto = auto
        if self.auto:
            self.hborb = HiddenBoard()

        self.start_strategy = 0
        self.strgy = list()
        self.killed = {"‎🚣": [], "‎⛵": [], "‎🚢": [], "‎⛴ ": []}
        self.wounded = {
            "‎⛵": {1: [], 2: [], 3: []},
            "‎🚢": {1: [], 2: []},
            "‎⛴ ": {1: []},
        }
        self.ships = self.brd.get_ships()
        for c, _ in enumerate(self.ships):
            if c == 0:
                self.wounded["‎⛵"][1].append(_[0])
                self.wounded["‎⛵"][1].append(_[1])
                self.wounded["‎⛵"][2].append(_[2])
                self.wounded["‎⛵"][2].append(_[3])
                self.wounded["‎⛵"][3].append(_[4])
                self.wounded["‎⛵"][3].append(_[5])
            elif c == 1:
                self.wounded["‎🚢"][1].append(_[0])
                self.wounded["‎🚢"][1].append(_[1])
                self.wounded["‎🚢"][1].append(_[2])
                self.wounded["‎🚢"][2].append(_[3])
                self.wounded["‎🚢"][2].append(_[4])
                self.wounded["‎🚢"][2].append(_[5])
            else:
                self.wounded["‎⛴ "][1].append(_[0])
                self.wounded["‎⛴ "][1].append(_[1])
                self.wounded["‎⛴ "][1].append(_[2])
                self.wounded["‎⛴ "][1].append(_[3])

    def get_oreol(self):
        return self.orl.oreol

    def strategy(self, fc, sc):
        if fc + 1 <= 9 and [fc + 1, sc] not in self.orl.oreol:
            self.strgy.append([fc + 1, sc])
        if fc - 1 >= 0 and [fc - 1, sc] not in self.orl.oreol:
            self.strgy.append([fc - 1, sc])
        if sc + 1 <= 9 and [fc, sc + 1] not in self.orl.oreol:
            self.strgy.append([fc, sc + 1])
        if sc - 1 >= 0 and [fc, sc - 1] not in self.orl.oreol:
            self.strgy.append([fc, sc - 1])
        if self.strgy == []:
            if fc + 1 <= 9 and self.brd.board[fc + 1][sc] == "❌":
                self.strgy.append([fc + 2, sc])
            elif fc - 1 >= 0 and self.brd.board[fc - 1][sc] == "❌":
                self.strgy.append([fc - 2, sc])
            elif sc + 1 <= 9 and self.brd.board[fc][sc + 1] == "❌":
                self.strgy.append([fc, sc + 2])
            elif sc - 1 >= 0 and self.brd.board[fc][sc - 1] == "❌":
                self.strgy.append([fc, sc - 2])
        return choice(self.strgy)

    def move(self, coord1, coord2):
        self.strgy.clear()
        self.status = ""

        def wounded(ship, fc, sc):
            self.status = f"{fc}, {sc} - РАНИЛ!"
            for k, v in self.wounded[ship].items():
                if [fc, sc] in v:
                    self.wounded[ship][k].remove([fc, sc])
                    self.killed[ship].append([fc, sc])
                    self.orl.add_wounded(fc, sc)
                    for _ in self.orl.o_wounded:
                        self.brd.board[_[0]][_[1]] = "‎⬛"
                        if self.auto:
                            self.hborb.board[_[0]][_[1]] = "‎⬛"
                    if [fc, sc] not in self.orl.oreol:
                        self.orl.oreol.append([fc, sc])
                    if len(self.wounded[ship][k]) == 0:
                        self.status = f"{fc}, {sc} - УБИЛ!"
                        self.start_strategy = 2
                        self.strgy.clear()
                        oreol(fc, sc)
                        break
            return self.status

        def oreol(fc, sc):
            self.status = f"{fc}, {sc} - УБИЛ!"
            self.orl.add_oreol(fc, sc)
            if [fc, sc] not in self.killed[self.brd.board[fc][sc]]:
                self.killed[self.brd.board[fc][sc]].append([fc, sc])
            if len(self.killed[self.brd.board[fc][sc]]) > 1:
                if self.brd.board[fc][sc] == "‎⛵":
                    lastval = self.killed[self.brd.board[fc][sc]][-2:]
                elif self.brd.board[fc][sc] == "‎🚢":
                    lastval = self.killed[self.brd.board[fc][sc]][-3:]
                else:
                    lastval = self.killed[self.brd.board[fc][sc]]
                if lastval[0][0] == lastval[1][0]:
                    mn = min(lastval)
                    mx = max(lastval)
                    if [mn[0], mn[1] - 1] not in self.orl.oreol and mn[1] - 1 >= 0:
                        self.orl.oreol.append([mn[0], mn[1] - 1])
                    elif [mx[0], mx[1] + 1] not in self.orl.oreol and mx[1] + 1 <= 9:
                        self.orl.oreol.append([mx[0], mx[1] + 1])
                else:
                    mn = min(lastval)
                    mx = max(lastval)
                    if [mn[0] - 1, mn[1]] not in self.orl.oreol and mn[0] - 1 >= 0:
                        self.orl.oreol.append([mn[0] - 1, mn[1]])
                    elif [mx[0] + 1, mx[1]] not in self.orl.oreol and mx[0] + 1 <= 9:
                        self.orl.oreol.append([mx[0] + 1, mx[1]])
            for _ in self.orl.oreol:
                if _ != [fc, sc] and self.brd.board[_[0]][_[1]] != "❌":
                    self.brd.board[_[0]][_[1]] = "‎⬛"
                    if self.auto:
                        self.hborb.board[_[0]][_[1]] = "‎⬛"

            return self.status

        time.sleep(0.5)
        if self.brd.board[coord1][coord2] == "‎⬜":
            self.brd.board[coord1][coord2] = "‎⬛"
            if self.auto:
                self.hborb.board[coord1][coord2] = "‎⬛"
            self.orl.oreol.append([coord1, coord2])
            self.status = f"{coord1}, {coord2} - МИМО!"
            if self.auto:
                self.start_strategy = 0
            else:
                if self.start_strategy == 2:
                    self.start_strategy = 0
            print(self.status)
        elif self.brd.board[coord1][coord2] == "‎🚣":
            self.status = oreol(coord1, coord2)
            self.brd.board[coord1][coord2] = "❌"
            if self.auto:
                self.hborb.board[coord1][coord2] = "❌"
            self.orl.oreol.append([coord1, coord2])
            self.start_strategy = 2
            print(self.status)
        elif self.brd.board[coord1][coord2] == "‎⛵":
            self.status = wounded(self.brd.board[coord1][coord2], coord1, coord2)
            self.brd.board[coord1][coord2] = "❌"
            if self.auto:
                self.hborb.board[coord1][coord2] = "❌"
            self.orl.oreol.append([coord1, coord2])
            print(self.status)
            if self.status == f"{coord1}, {coord2} - РАНИЛ!":
                self.start_strategy = 1
                if self.auto is not True:
                    strategy = self.strategy(coord1, coord2)
                    self.move(strategy[0], strategy[1])
        elif self.brd.board[coord1][coord2] == "‎🚢":
            self.status = wounded(self.brd.board[coord1][coord2], coord1, coord2)
            self.brd.board[coord1][coord2] = "❌"
            if self.auto:
                self.hborb.board[coord1][coord2] = "❌"
            self.orl.oreol.append([coord1, coord2])
            print(self.status)
            if self.status == f"{coord1}, {coord2} - РАНИЛ!":
                self.start_strategy = 1
                if self.auto is not True:
                    strategy = self.strategy(coord1, coord2)
                    self.move(strategy[0], strategy[1])
        elif self.brd.board[coord1][coord2] == "‎⛴ ":
            self.status = wounded(self.brd.board[coord1][coord2], coord1, coord2)
            self.brd.board[coord1][coord2] = "❌"
            if self.auto:
                self.hborb.board[coord1][coord2] = "❌"
            self.orl.oreol.append([coord1, coord2])
            print(self.status)
            if self.status == f"{coord1}, {coord2} - РАНИЛ!":
                self.start_strategy = 1
                if self.auto is not True:
                    strategy = self.strategy(coord1, coord2)
                    self.move(strategy[0], strategy[1])
        elif self.start_strategy == 1 and self.auto is False:
            strategy = self.strategy(coord1, coord2)
            self.move(strategy[0], strategy[1])
        else:
            self.status = f"{coord1}, {coord2} - СЮДА ХОДИТЬ НЕЛЬЗЯ!"
        return self.start_strategy


def main():
    robotgame = GamePlay()
    mygame = GamePlay(True)

    def outboards(compboard, mybooard):
        dobleboard = ""
        numbs = [" ", " ⓪", " ①", " ②", " ③", " ④", " ⑤", " ⑥", " ⑦", " ⑧", " ⑨"]
        print((" ".join([_ for _ in numbs]) + "  ") * 2)
        numbs = [" ⓪ ", " ① ", " ② ", " ③ ", " ④ ", " ⑤ ", " ⑥ ", " ⑦ ", " ⑧ ", " ⑨ "]
        for c, _ in enumerate(compboard.brd.board):
            dobleboard += numbs[c] + " ".join(_) + " " + numbs[c] + " ".join(mybooard.board[c]) + "\n"
        return dobleboard

    def check_win(gkilled, comp=False):
        if (
            len(gkilled["\u200e🚣"]) == 4
            and len(gkilled["\u200e⛵"]) == 6
            and len(gkilled["\u200e🚢"]) == 6
            and len(gkilled["\u200e⛴ "]) == 4
        ):
            print("=-" * 33)
            if comp:
                print("ТЫ ЛУЗЕР! КОМПЬЮТЕР ВЫИГРАЛ!")
                print(outboards(robotgame, mygame.brd))
            else:
                print("Поздравляем! ПОБЕДА!!!".upper())
                print(outboards(robotgame, mygame.brd))
            sys.exit()

    def robot():
        start = 0
        if choice([True, False]):
            yield
        while True:
            if start == 0:
                oreol = robotgame.get_oreol()
                while True:
                    inp = [randint(0, 9), randint(0, 9)]
                    if inp not in oreol:
                        break
            print("=-" * 33)
            print(f"\t\t\tКОМПЬЮТЕР ХОДИТ: {inp[0]}, {inp[1]}")
            start = robotgame.move(inp[0], inp[1])
            print("--" * 10)
            print(outboards(robotgame, mygame.hborb))
            if start == 2:
                check_win(robotgame.killed, comp=True)
                yield start
                start = 0
            else:
                yield start

    generator = robot()
    print(outboards(robotgame, mygame.hborb))
    for _ in generator:
        if _ == 2:
            continue
        oreol = mygame.get_oreol()
        status = 1
        while status in (1, 2):
            while True:
                try:
                    print("=-" * 33)
                    mymove = [int(_) for _ in input("\t\t\tМОЙ ХОД: ").split()]
                    if 0 <= mymove[0] <= 9 and 0 <= mymove[1] <= 9:
                        if mymove not in oreol:
                            break
                        else:
                            print("СЮДА ХОДИТЬ НЕЛЬЗЯ!")
                    else:
                        continue
                except Exception:
                    print("НЕПРАВИЛЬНЫЙ ВВОД!")
                    continue
            status = mygame.move(mymove[0], mymove[1])
            print("--" * 10)
            print(outboards(robotgame, mygame.hborb))
            check_win(mygame.killed)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("stop")
        sys.exit()
