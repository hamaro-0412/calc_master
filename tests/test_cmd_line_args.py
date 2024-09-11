import pytest
import random
from math_workbook.cmd_line_args import CmdLineArgs

class TestCmdLineArgs :
    
    @classmethod
    def setup_class(cls) :
        cls.cmd_line_args = CmdLineArgs()

    # 足し算の答えが一桁になるかどうかのテスト 0を除く
    def test__generate_answer__excluding_0(self, monkeypatch) :
        monkeypatch.setattr(random, 'randint', lambda a, b: 7)
        assert self.cmd_line_args.generate_answer() == 7
    
    # 足し算の答えが一桁になるかどうかのテスト 0を含む
    def test__generate_answer__including_0(self) :
        pass

