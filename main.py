from typing import Literal, Union


def mux(val: int, inverted: int, use_inverted: bool):
    return inverted if use_inverted else val


def full_adder(a, b, carry_in):
    result_xor = a ^ b
    carry_out = (a and b) or (carry_in and result_xor)
    result = carry_in ^ result_xor
    return result, carry_out


class Alu:
    def __init__(self):
        self.last_calculation_was_overflow: Literal[0, 1] = 0
    
    def receive_entries(self, a: int, b: int, a_invert: int, b_invert: int, carry_in: int, is_the_last_bit: bool = False):
        a = mux(a, int(not a), a_invert)
        b = mux(b, int(not b), b_invert)
        result_and = a and b
        result_or = a or b

        result, carry_out = full_adder(a, b, carry_in)
        
        if is_the_last_bit and carry_out == 1:
            self.last_calculation_was_overflow = 1
        
        return result, carry_out

    def overflow(self):
        return self.last_calculation_was_overflow


def main():
    pass


if __name__ == '__main__':
    main()
