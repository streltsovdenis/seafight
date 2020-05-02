class Oreol:
    def __init__(self):
        self.oreol = list()
        self.o_wounded = list()

    def add_oreol(self, fc, sc):
        self.oreol.append([fc, sc])
        if [fc, sc] == [0, 0]:
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc + 1, sc + 1])
        elif [fc, sc] == [0, 9]:
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc + 1, sc - 1])
        elif [fc, sc] == [9, 0]:
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc - 1, sc + 1])
        elif [fc, sc] == [9, 9]:
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc - 1, sc - 1])
        elif fc == 0 and sc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc + 1, sc + 1])
        elif fc == 9 and sc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc - 1, sc + 1])
        elif sc == 0 and fc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc - 1, sc + 1])
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc + 1, sc + 1])
        elif sc == 9 and fc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc - 1, sc - 1])
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc + 1, sc - 1])
        else:
            self.oreol.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc])
            self.oreol.append([fc - 1, sc + 1])
            self.oreol.append([fc, sc - 1])
            self.oreol.append([fc, sc + 1])
            self.oreol.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc])
            self.oreol.append([fc + 1, sc + 1])

    def add_wounded(self, fc, sc):
        if [fc, sc] == [0, 0]:
            self.o_wounded.append([fc + 1, sc + 1])
            self.oreol.append([fc + 1, sc + 1])
        elif [fc, sc] == [0, 9]:
            self.o_wounded.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc - 1])
        elif [fc, sc] == [9, 0]:
            self.o_wounded.append([fc - 1, sc + 1])
            self.oreol.append([fc - 1, sc + 1])
        elif [fc, sc] == [9, 9]:
            self.o_wounded.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc - 1])
        elif fc == 0 and sc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.o_wounded.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc - 1])
            self.o_wounded.append([fc + 1, sc + 1])
            self.oreol.append([fc + 1, sc + 1])
        elif fc == 9 and sc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.o_wounded.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc - 1])
            self.o_wounded.append([fc - 1, sc + 1])
            self.oreol.append([fc - 1, sc + 1])
        elif sc == 0 and fc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.o_wounded.append([fc - 1, sc + 1])
            self.oreol.append([fc - 1, sc + 1])
            self.o_wounded.append([fc + 1, sc + 1])
            self.oreol.append([fc + 1, sc + 1])
        elif sc == 9 and fc in (1, 2, 3, 4, 5, 6, 7, 8):
            self.o_wounded.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc - 1])
            self.o_wounded.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc - 1])
        else:
            self.o_wounded.append([fc - 1, sc - 1])
            self.oreol.append([fc - 1, sc - 1])
            self.o_wounded.append([fc - 1, sc + 1])
            self.oreol.append([fc - 1, sc + 1])
            self.o_wounded.append([fc + 1, sc - 1])
            self.oreol.append([fc + 1, sc - 1])
            self.o_wounded.append([fc + 1, sc + 1])
            self.oreol.append([fc + 1, sc + 1])
