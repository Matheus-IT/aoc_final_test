from ..main import alu

def test_ula_sum():
    # Somando 10 mais 1
    a = [1, 0, 1, 0]
    b = [0, 0, 0, 1]
    carry_in = 0

    sum_res = []
    for i in range(len(a)-1, -1, -1):
        result, carry_out = alu(a[i], b[i], a_invert=0, b_invert=0, carry_in=carry_in)
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
    for i in range(len(a)-1, -1, -1):
        result, carry_out = alu(a[i], b[i], a_invert=0, b_invert=1, carry_in=carry_in)
        carry_in = carry_out
        sub_res.append(result)
    sub_res = list(reversed(sub_res))
    nine = [1, 0, 0, 1]
    assert sub_res == nine
