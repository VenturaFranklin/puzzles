from .ReportRepair import run, run2


def test1_1_run():
    instructions = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    expected_out = 514579
    actual_out = run(instructions)
    assert expected_out == actual_out


def test1_1_run2():
    instructions = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    expected_out = 241861950
    actual_out = run2(instructions)
    assert expected_out == actual_out