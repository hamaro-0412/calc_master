import pytest
import random
from calc_master.addition_workbook import AdditionWorkbook

class TestAdditionWorkbook :
    
    @classmethod
    def setup_class(cls) :
        cls.inst = AdditionWorkbook()

    # 足し算の答えが一桁になるかどうかのテスト 0を含む
    def test__generate_answer__including_0(self) :
        pass

    # 一桁の答えから2つの変数を使った式を求める 0を除く
    # 答え: 4 -> 2 + 2, 3 + 1, etc
    def test__generate_fomula__single_digit_answer_and_two_value__excluding_0(self) :
        pass

    # 一桁の答えから2つの変数を求める 0を含む
    # 答え: 4 -> 4 + 0, 2 + 2, 3 + 1, etc
    def test__generate_fomula__single_digit_answer_and_two_value__including_0(self) :
        pass
