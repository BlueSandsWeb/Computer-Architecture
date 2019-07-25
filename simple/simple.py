import sys
​
PRINT_BEEJ     = 1
HALT           = 2
PRINT_NUM      = 3
SAVE_REGISTER  = 4
PRINT_REGISTER = 5
PUSH           = 6
POP            = 7
​
memory = [0] * 128
​
register = [0] * 8   # 8 registers
sp = 7
​
pc = 0 # Program Counter, points to currently-executing instruction
​
running = True
​
if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} filename")
    sys.exit(1)
​
try:
    with open(sys.argv[1]) as f:
        address = 0
​
        for line in f:
            num = line.split("#", 1)[0]
​
            if num.strip() == '':  # ignore comment-only lines
                continue
​
            #print(int(num))
            memory[address] = int(num)
            address += 1
​
except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)

registers[sp] = 127
​
while running:
    command = memory[pc]
​
    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
​
    elif command == PRINT_NUM:
        operand = memory[pc + 1]
        print(operand)
        pc += 2
​
    elif command == SAVE_REGISTER:
        value = memory[pc + 1]
        regnum = memory[pc + 2]
        register[regnum] = value
        pc += 3
​
    elif command == PRINT_REGISTER:
        regnum = memory[pc + 1]
        print(register[regnum])
        pc += 2
​
    elif command == HALT:
        running = False
        pc += 1
    
    elif command == PUSH:
        resgisters[sp] -= 1             # decrement the stack pointer
        regnum = memory[pc + 1]         # get the register number operand
        value = registers[regnum]       # get the value from that register
        memory[registers[sp]] = value   # store that value in memory at the sp
        pc += 2

    elif command == POP:
        value = memory[registers[sp]]   # get value from memory at AT
        regnum = memory[pc + 1]         # get the register number operand
        registers[regnum] = value       #store the value from the stack in the register
        registers[sp] += 1              # increment the stack pointer
        pc += 2

    elif command == CALL:
        return_address = pc + 2                 # get address of instruction right after this CALL instruction
        resgisters[sp] -= 1                     # decrement the stack pointer
        memory[registers[sp]] = return_address  # store that value in memory at the stack pointer
        
        regnum = memory[pc + 1]
        subroutine_address = register[regnum]
        pc = subroutine_address
    
    elif command == RET:
        return_address = memory[register[sp]]
        register[sp] += 1
        pc = return_address

    else:
        print(f"unknown instruction {command}")
        sys.exit(1)
    