from typing import List, Literal, Union


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
        self.n1 = a
        self.n2 = b
    
    def do_sum(self):
        sum_res = []
        carry_in = 0
        for i in range(len(self.n1)-1, -1, -1):
            result, carry_out = self.process_entries(
                                    self.n1[i], 
                                    self.n2[i], 
                                    a_invert=0, 
                                    b_invert=0, 
                                    carry_in=carry_in,
                                    is_the_last_bit=True if i == 0 else False,
                                )
            carry_in = carry_out
            sum_res.append(result)
        return list(reversed(sum_res))
    
    def subtract(self):
        sub_res = []
        carry_in = 1
        for i in range(len(self.n1)-1, -1, -1):
            result, carry_out = self.process_entries(
                                    self.n1[i], 
                                    self.n2[i], 
                                    a_invert=0, 
                                    b_invert=1, 
                                    carry_in=carry_in,
                                    is_the_last_bit=True if i == 0 else False,
                                )
            carry_in = carry_out
            sub_res.append(result)
        return list(reversed(sub_res))
    
    def process_entries(self, a: int, b: int, a_invert: int, b_invert: int, carry_in: int, is_the_last_bit: bool = False):
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
