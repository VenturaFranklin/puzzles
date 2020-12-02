from .challenge import run, run2


def test1_1_run():
    instructions = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    expected_out = 2
    actual_out = run(instructions)
    assert expected_out == actual_out


def test1_1_run2():
    instructions = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    expected_out = 1
    actual_out = run2(instructions)
    assert expected_out == actual_out