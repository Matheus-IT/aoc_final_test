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
    return full_adder(a, b, carry_in)


def main():
    # Somando 10 mais 1
    a = [1, 0, 1, 0]
    b = [0, 0, 0, 1]
    carry_in = 0

    sub_res = []
    for i in range(len(a)-1, -1, -1):
        result, carry_out = ula(a[i], b[i], a_invert=False, b_invert=False, carry_in=carry_in)
        carry_in = carry_out
        sub_res.append(result)

    sub_res =sub_res[::-1]
    print(sub_res)
    

if __name__ == '__main__':
    main()
