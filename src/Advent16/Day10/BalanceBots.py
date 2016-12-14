'''
Created on Dec 12, 2016

@author: venturf2

--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing
small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it
has two microchips, and once it does, it gives each one to a different bot or
puts it in a marked "output" bin. Sometimes,
bots take microchips from "input" bins, too.

Inspecting one of the microchips,
it seems like they each contain a single number;
the bots must use some logic to decide what to do with each chip.
You access the local control computer and download the bots' instructions
(your puzzle input).

Some of the instructions specify that a specific-valued microchip should be
given to a specific bot; the rest of the instructions indicate what a given
bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
Initially, bot 1 starts with a value-3 chip,
and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2)
to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips;
it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips;
it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip,
output bin 1 contains a value-2 microchip,
and output bin 2 contains a value-3 microchip. In this configuration,
bot number 2 is responsible for comparing value-5
microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible
for comparing value-61 microchips with value-17 microchips?
'''


def parse_bot(line):
    info = line.split(' ')
    bot = info[1]
#     type_1 = info[3]
    loc_1 = info[5]
    loc_num_1 = info[6]
#     type_2 = info[8]
    loc_2 = info[10]
    loc_num_2 = info[11]
    return {bot: ((loc_1, loc_num_1),
                  (loc_2, loc_num_2))}


def parse_value(line):
    info = line.split(' ')
    val = info[1]
    bot = info[5]
    return bot, val


def extend_bot_vals(bots, bot, val):
    if bot in bots:
        bots[bot].append(val)
    else:
        bots[bot] = [val]


def parse_instructions(instructions):
    parsed = {}
    bots = {}
    count = 0
    for line in instructions:
        if line.startswith('bot'):
            parsed.update(parse_bot(line))
        else:
            bot, val = parse_value(line)
            extend_bot_vals(bots, bot, val)
            count += 1
    for bot in parsed:
        if bot not in bots:
            bots[bot] = []
    return parsed, bots, count


def test_1():
    test_instructions = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''
    test_instructions = test_instructions.split('\n')
    testing = ('5', '2')
    actual_out = run(test_instructions, testing)
    expected_out = '2'
    assert actual_out == expected_out


def run(instructions, test):
    parsed_instr, bots, count = parse_instructions(instructions)
    while count > 0:
        for bot in bots:
            if len(bots[bot]) > 1:
                low, high = parsed_instr[bot]
                low_type, low_bot = low
                if (test[0] in bots[bot]) & (test[1] in bots[bot]):
                    return bot
                bots[bot].sort(key=float)
                if low_type == 'bot':
                    extend_bot_vals(bots, low_bot, bots[bot][0])
                else:
                    count -= 1
                high_type, high_bot = high
                if high_type == 'bot':
                    extend_bot_vals(bots, high_bot, bots[bot][1])
                else:
                    count -= 1
                bots[bot] = []

if __name__ == "__main__":
#     test_1()
    test = ('17', '61')
    with open('PuzzleInput.txt', 'r') as this_file:
        out = run(this_file.read().split('\n'), test)
    print(out)
