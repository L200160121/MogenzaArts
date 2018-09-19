class pohon():
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = pohon(9)
B = pohon(10)
C = pohon(6)
D = pohon(22)

A.kiri = B; A.kanan = C
B.kiri = D

def PO(sp):
    if sp is not None:
        print sp.data
        PO (sp.kiri)
        PO (sp.kanan)

def IO(sp):
    if sp is not None:
        IO (sp.kiri)
        print sp.data
        IO (sp.kanan)

def PoO(sp):
    if sp is not None:
        PoO (sp.kiri)
        PoO (sp.kanan)
        print sp.data



PO(A)
print "\n"
IO(A)
print "\n"
PoO(A)
