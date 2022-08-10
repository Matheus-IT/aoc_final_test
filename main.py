from functools import reduce
from typing import List, Literal


def mux(val: int, inverted: int, use_inverted: int):
    return inverted if use_inverted else val


def full_adder(a, b, carry_in):
    result_xor = a ^ b
    carry_out = (a and b) or (carry_in and result_xor)
    result = carry_in ^ result_xor
    return result, carry_out


class Alu:
    def __init__(self, a: List[int], b: List[int]):
        self.last_calculation_was_overflow: Literal[0, 1] = 0
        self.last_result: List[int] = []
        self.n1 = a
        self.n2 = b

    def do_sum(self):
        sum_res = []
        carry_in = 0
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=0,
                carry_in=carry_in,
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            sum_res.append(result)
        self.last_result = list(reversed(sum_res))
        return self.last_result

    def subtract(self):
        sub_res = []
        carry_in = 1
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=1,
                carry_in=carry_in,
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            sub_res.append(result)
        self.last_result = list(reversed(sub_res))
        return self.last_result

    def process_entries(
        self,
        a: int,
        b: int,
        a_invert: int,
        b_invert: int,
        carry_in: int,
        is_the_most_significant_valid_bit: bool,
    ):
        a = mux(a, int(not a), a_invert)
        b = mux(b, int(not b), b_invert)
        result_and = a and b
        result_or = a or b

        result, carry_out = full_adder(a, b, carry_in)

        if is_the_most_significant_valid_bit and carry_out == carry_in:
            self.last_calculation_was_overflow = 1

        return result, carry_out

    def overflow(self):
        return self.last_calculation_was_overflow

    def the_last_result_was_zero(self):
        return not reduce(lambda n1, n2: n1 or n2, self.last_result)


def main():
    pass


if __name__ == "__main__":
    main()
