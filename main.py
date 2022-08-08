def mux(val: int, inverted: int, use_inverted: bool):
    return inverted if use_inverted else val


def full_adder(a, b, carry_in):
    result_xor = a ^ b
    carry_out = (a and b) or (carry_in and result_xor)

    result = carry_in ^ result_xor

    return result, carry_out


def ula(a: int, b: int, a_invert: bool, b_invert: bool, carry_in: int):
    a = mux(a, int(not a), a_invert)
    b = mux(b, int(not b), b_invert)
    result_and = a and b
    result_or = a or b
    full_adder(result_and, result_or, carry_in)


def main():
    a = [1, 0, 1, 0]
    b = [0, 0, 0, 1]
    carry_in = 0

    # for i in range(len(a)):
    #     result = ula(a[i], b[i], a_invert=False, b_invert=False, carry_in=carry_in)
    #     print(result)


if __name__ == '__main__':
    main()
