from ..main import Alu

def test_ula_sum():
    # Somando 10 mais 1
    a = [1, 0, 1, 0]
    b = [0, 0, 0, 1]
    carry_in = 0

    alu = Alu()
    sum_res = []
    for i in range(len(a)-1, -1, -1):
        result, carry_out = alu.receive_entries(a[i], b[i], a_invert=0, b_invert=0, carry_in=carry_in)
        carry_in = carry_out
        sum_res.append(result)

    sum_res = list(reversed(sum_res))
    eleven = [1, 0, 1, 1]
    assert sum_res == eleven


def test_ula_sub():
    # Subtraindo 10 menos 1
    a = [1, 0, 1, 0]
    b = [0, 0, 0, 1]
    carry_in = 1
    sub_res = []
    alu = Alu()
    for i in range(len(a)-1, -1, -1):
        result, carry_out = alu.receive_entries(a[i], b[i], a_invert=0, b_invert=1, carry_in=carry_in)
        carry_in = carry_out
        sub_res.append(result)
    sub_res = list(reversed(sub_res))
    nine = [1, 0, 0, 1]
    assert sub_res == nine


def test_ula_overflow():
    """Somando 8 mais 8 deve dar overflow"""
    a = [1, 0, 0, 0]
    b = [1, 0, 0, 0]

    carry_in = 0
    alu = Alu()

    for i in range(len(a)-1, -1, -1):
        result, carry_out = alu.receive_entries(
            a[i],
            b[i],
            a_invert=0,
            b_invert=0,
            carry_in=carry_in,
            is_the_last_bit=True if i == 0 else False,
        )
        carry_in = carry_out
    assert alu.overflow() == 1
