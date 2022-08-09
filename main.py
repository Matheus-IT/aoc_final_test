def mux(val: int, inverted: int, use_inverted: bool):
    return inverted if use_inverted else val


def full_adder(a, b, carry_in):
    result_xor = a ^ b
    carry_out = (a and b) or (carry_in and result_xor)
    result = carry_in ^ result_xor
    return result, carry_out


def alu(a: int, b: int, a_invert: int, b_invert: int, carry_in: int):
    a = mux(a, int(not a), a_invert)
    b = mux(b, int(not b), b_invert)
    result_and = a and b
    result_or = a or b
    return full_adder(a, b, carry_in)


def main():
    pass


if __name__ == '__main__':
    main()
