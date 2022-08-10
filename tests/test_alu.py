from ..main import Alu


def test_ula_sum():
    """Somando 4 mais 1"""
    alu = Alu(a=[0, 1, 0, 0], b=[0, 0, 0, 1])
    sum_res = alu.do_sum()
    five = [0, 1, 0, 1]
    assert sum_res == five


def test_ula_sum_2():
    """Somando -4 mais 2"""
    alu = Alu(a=[1, 1, 0, 0], b=[0, 0, 1, 0])
    sum_res = alu.do_sum()
    minus_two = [1, 1, 1, 0]
    assert sum_res == minus_two


def test_ula_sub():
    """Subtraindo 4 menos 1"""
    sub_res = []
    alu = Alu(a=[0, 1, 0, 0], b=[0, 0, 0, 1])
    sub_res = alu.subtract()
    three = [0, 0, 1, 1]
    assert sub_res == three


def test_ula_sub_2():
    """Somando -4 menos 2"""
    alu = Alu(a=[1, 1, 0, 0], b=[0, 0, 1, 0])
    sub_res = alu.subtract()
    minus_six = [1, 0, 1, 0]
    assert sub_res == minus_six


def test_ula_should_overflow():
    """Somando 7 mais 1 deve dar overflow"""
    alu = Alu(a=[0, 1, 1, 1], b=[0, 0, 0, 1])
    alu.do_sum()
    assert alu.overflow() == 1


def test_ula_should_overflow_2():
    """Subtraindo -1 de -8 deve dar overflow"""
    alu = Alu(a=[1, 0, 0, 0], b=[1, 1, 1, 1])
    alu.subtract()
    assert alu.overflow() == 1


def test_ula_should_not_overflow():
    """Somando 2 mais 2 NÃO deve dar overflow"""
    alu = Alu(a=[0, 0, 1, 0], b=[0, 0, 1, 0])
    alu.do_sum()
    assert alu.overflow() == 0


def test_ula_zero_result_when_sum():
    """Retorna se o resultado é zero"""
    alu = Alu(a=[0, 0, 0, 0], b=[0, 0, 0, 0])
    alu.do_sum()
    assert alu.the_last_result_was_zero() == 1


def test_ula_should_not_be_zero_when_sum():
    """Retorna se o resultado é zero"""
    alu = Alu(a=[0, 0, 1, 0], b=[0, 0, 1, 0])
    alu.do_sum()
    assert alu.the_last_result_was_zero() == 0


def test_ula_zero_result_when_subtract():
    """Retorna se o resultado é zero"""
    alu = Alu(a=[0, 0, 0, 0], b=[0, 0, 0, 0])
    alu.subtract()
    assert alu.the_last_result_was_zero() == 1


def test_ula_should_not_be_zero_when_subtract():
    """Retorna se o resultado é zero"""
    alu = Alu(a=[0, 1, 0, 0], b=[0, 0, 1, 0])
    alu.subtract()
    assert alu.the_last_result_was_zero() == 0
