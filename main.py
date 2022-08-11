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
            result, carry_out, _ = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=0,
                less=0,
                carry_in=carry_in,
                ula_op=[1, 0],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            sum_res.append(result)
        self.last_result = list(reversed(sum_res))
        return self.last_result

    def do_slt(self):
        sub_res = []
        slt_res = []
        carry_in = 0
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out, res_less = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=1,
                less=0,
                carry_in=carry_in,
                ula_op=[1, 1],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )

            carry_in = carry_out
            sub_res.append(result)

            if i == 0:
                slt_res.append(result)
            else:
                slt_res.append(res_less)

        self.last_result = list(reversed(slt_res))
        return 1 if self.slt_true(self.last_result) else 0

    def slt_true(self, number: List[int]):
        return any(map(lambda n: n == 1, number))

    def subtract(self):
        sub_res = []
        carry_in = 1
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out, _ = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=1,
                less=0,
                carry_in=carry_in,
                ula_op=[1, 0],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            sub_res.append(result)
        self.last_result = list(reversed(sub_res))
        return self.last_result

    def do_nor(self):
        nor_res = []
        carry_in = 0
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out, _ = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=1,
                b_invert=1,
                less=0,
                carry_in=carry_in,
                ula_op=[0, 0],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            nor_res.append(result)
        self.last_result = list(reversed(nor_res))
        return self.last_result

    def do_and(self):
        and_res = []
        carry_in = 0
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out, _ = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=0,
                less=0,
                carry_in=carry_in,
                ula_op=[0, 0],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            and_res.append(result)
        self.last_result = list(reversed(and_res))
        return self.last_result

    def do_or(self):
        or_res = []
        carry_in = 0
        for i in range(len(self.n1) - 1, -1, -1):
            result, carry_out, _ = self.process_entries(
                self.n1[i],
                self.n2[i],
                a_invert=0,
                b_invert=0,
                less=0,
                carry_in=carry_in,
                ula_op=[0, 1],
                is_the_most_significant_valid_bit=True if i == 1 else False,
            )
            carry_in = carry_out
            or_res.append(result)
        self.last_result = list(reversed(or_res))
        return self.last_result

    def process_entries(
        self,
        a: int,
        b: int,
        a_invert: int,
        b_invert: int,
        less: int,
        carry_in: int,
        ula_op: List[int],
        is_the_most_significant_valid_bit: bool,
    ):
        a = mux(a, int(not a), a_invert)
        b = mux(b, int(not b), b_invert)

        result_and = a and b
        result_or = a or b
        result_adder, carry_out = full_adder(a, b, carry_in)

        if is_the_most_significant_valid_bit and carry_out == carry_in:
            self.last_calculation_was_overflow = 1

        if ula_op == [0, 0]:
            return result_and, carry_out, less
        if ula_op == [0, 1]:
            return result_or, carry_out, less
        if ula_op == [1, 0]:
            return result_adder, carry_out, less
        if ula_op == [1, 1]:
            return result_adder, carry_out, less
        else:
            raise Exception('Invalid ula_op')

    def overflow(self):
        return self.last_calculation_was_overflow

    def the_last_result_was_zero(self):
        return not reduce(lambda n1, n2: n1 or n2, self.last_result)


def main():
    pass


if __name__ == "__main__":
    main()
