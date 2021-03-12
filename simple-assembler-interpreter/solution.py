"""
ID: 58e24788e24ddee28e000053

This is the first part of this kata series. Second part is here.

We want to create a simple interpreter of assembler which will support the following instructions:

    mov x y - copies y (either a constant value or the content of a register) into register x
    inc x - increases the content of the register x by one
    dec x - decreases the content of the register x by one
    jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant),
    but only if x (a constant or a register) is not zero

Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction,
 while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will execute them.
The program ends when there are no more instructions to execute, then it returns a dictionary with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.
"""

def check_num_str(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def simple_assembler(program):

    program = [i.split() for i in program]
    variables = dict()
    
    i = 0

    while i < len(program):

        command = program[i]

        if command[0] == 'mov':
            if command[2].isalpha(): variables[command[1]] = int(variables[command[2]])
            else: variables[command[1]] = int(command[2])

            i += 1
            continue
        
        elif command[0] == 'inc':
            variables[command[1]] += 1
            i += 1
            continue
        
        elif command[0] == 'dec':
            variables[command[1]] -= 1
            i += 1
            continue

        else:
            validate = command[1] if check_num_str(command[1]) else variables[command[1]]

            steps = int(command[2]) if check_num_str(command[2]) else variables[command[2]]

            i = i + steps if validate != 0 else i + 1
            continue
    
    return variables
            






code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
print(simple_assembler(code.splitlines()), {'a': 1})

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
print(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})