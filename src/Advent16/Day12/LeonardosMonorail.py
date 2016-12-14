'''
Created on Dec 12, 2016

@author: venturf2

--- Day 12: Leonardo's Monorail ---

You finally reach the top floor of this building:
a garden with a slanted glass ceiling.
Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies,
you manage to decrypt some of the files you extracted
from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building -
it's a collection of buildings in the nearby area. They're all connected
by a local monorail, and there's another building not far from here!
Unfortunately, being night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover
that the boot sequence expects a password. The password-checking logic
(your puzzle input) is easy to extract, but the code it uses is strange:
it's assembunny code designed for the new computer you just assembled.
You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four registers
(a, b, c, and d) that start at 0 and can hold any integer.
However, it seems to make use of only a few instructions:

cpy x y copies x (either an integer or the value of a register)
into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away (positive means forward;
negative means backward), but only if x is not zero.
The jnz instruction moves relative to itself:
an offset of -1 would continue at the previous instruction,
while an offset of 2 would skip over the next instruction.

For example:

cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
The above code would set register a to 41, increase its value by 2,
decrease its value by 1, and then skip the last dec a
(because a is not zero, so the jnz a 2 skips it), leaving register a at 42.
When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input,
what value is left in register a?
'''


def inc(instruct, registers):
    _, register = instruct.split(' ')
    registers[register] += 1
    return registers, False


def dec(instruct, registers):
    _, register = instruct.split(' ')
    registers[register] -= 1
    return registers, False


def jnz(instruct, registers):
    _, register, value = instruct.split(' ')
    try:
        test = int(register)
    except ValueError:
        test = registers[register]
    if test != 0:
        instruct_ind = int(value)
    else:
        instruct_ind = False
    return registers, instruct_ind


def cpy(instruct, registers):
    _, value, register = instruct.split(' ')
    try:
        value = int(value)
    except ValueError:
        value = registers[value]
    registers[register] = value
    return registers, False


def test_1():
    registers = {'a': 0,
                 'b': 0,
                 'c': 0,
                 'd': 0}
    instructions = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''
    actual_out = run(instructions, registers)
    expected_out = 42
    assert actual_out['a'] == expected_out


def run(instructions, registers):
    instructions = instructions.split('\n')
    instruct_ind = 0
    while instruct_ind < len(instructions):
        instruct = instructions[instruct_ind]
        func = instruct[:3]
        registers, new_ind = globals()[func](instruct, registers)
        if new_ind:
            instruct_ind += new_ind
        else:
            instruct_ind += 1
    return registers


if __name__ == "__main__":
#     test_1()
    registers = {'a': 0,
                 'b': 0,
                 'c': 0,
                 'd': 0}
    with open('PuzzleInput.txt', 'r') as this_file:
        out = run(this_file.read(), registers)
    print(out['a'])
