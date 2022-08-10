from ..main import Alu

def test_ula_sum():
    # Somando 10 mais 1
    alu = Alu(a=[1, 0, 1, 0], b=[0, 0, 0, 1])
    sum_res = alu.do_sum()
    eleven = [1, 0, 1, 1]
    assert sum_res == eleven


def test_ula_sub():
    # Subtraindo 10 menos 1
    sub_res = []
    alu = Alu(a=[1, 0, 1, 0], b=[0, 0, 0, 1])
    sub_res = alu.subtract()
    nine = [1, 0, 0, 1]
    assert sub_res == nine


def test_ula_should_overflow():
    """Somando 8 mais 8 deve dar overflow"""
    alu = Alu(a=[1, 0, 0, 0], b=[1, 0, 0, 0])
    alu.do_sum()
    assert alu.overflow() == 1


def test_ula_should_not_overflow():
    """Somando 2 mais 2 NÃO deve dar overflow"""
    alu = Alu(a=[0, 0, 1, 0], b=[0, 0, 1, 0])
    alu.do_sum()
    assert alu.overflow() == 0
