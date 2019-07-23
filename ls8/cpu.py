"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.register = [0] * 8
        self.ram = [0] * 256
        self.pc = 0

        pass

    def load(self):
        """Load a program into memory."""



        if len(sys.argv) is not 2:
            print(f"usage: {sys.argv[0]} <filename>")
            sys.exit(1)
        
        try:
            address = 0
            program_name = sys.argv[1]

            with open(program_name) as f:
                for line in f:
                    num = line.split("#", 1)[0]

                    if num.strip() == '':  # ignore comment-only lines
                        continue
                    self.ram[address] = bin(num)
                    address += 1
            
            print(self.ram)

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value
        pass

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        running = True

        while running:

            IR = self.pc
            operand_a = self.ram_read(IR + 1)
            operand_b = self.ram_read(IR + 2)
            # print("IR: ", IR)
            # print("self.ram[IR]: ", bin(self.ram[IR]))
            if self.ram[IR] == 0b00000001:
                running = False
            
            elif self.ram[IR] == 0b10000010:
                self.register[operand_a] = operand_b
                self.pc += 3
            
            elif self.ram[IR] == 0b01000111:
                # print("THINGS")
                # print("operand_a: ", operand_a)
                print(f'{self.register[operand_a]}')
                self.pc += 2
            
cpu = CPU()
# # cpu.ram_write(55, 0)
# # print(f"CPU RAM: {cpu.ram}")
# # print(f"CPU RAM_READ: {cpu.ram_read(0)}" )
cpu.load()
# cpu.run()