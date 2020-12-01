from .ReportRepair import run


def test1_1_run():
    instructions = [1721, 979, 366, 299, 675, 1456,]
    expected_out = 514579
    actual_out = run(instructions)
    assert expected_out == actual_out