from ..main import full_adder


def test_full_adder():
    adder_out = [
        full_adder(0, 0, 0),
        full_adder(0, 0, 1),
        full_adder(0, 1, 0),
        full_adder(0, 1, 1),
        full_adder(1, 0, 0),
        full_adder(1, 0, 1),
        full_adder(1, 1, 0),
        full_adder(1, 1, 1),
    ]

    truth_table_carry_out = [0, 0, 0, 1, 0, 1, 1, 1]
    truth_table_result = [0, 1, 1, 0, 1, 0, 0, 1]

    result = list(zip(truth_table_result, truth_table_carry_out))
    assert adder_out == result
