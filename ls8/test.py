class Test:
    def __init__(self):
        self.table = {}
        self.table[0b10100000] = self.set
        self.table["operand_a"] = 0
        self.table["operand_b"] = 0

    def set(self, opA, opB):
        print(opA)
        print(opB)
        self.table["operand_a"] = opA
        self.table["operand_b"] = opB
        print(self.table["operand_a"])
        print(self.table["operand_b"])


test = Test()
operA = 1
operb = 2
test.table[0b10100000](operA, operb)