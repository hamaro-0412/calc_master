import pytest
import random
from math_workbook.cmd_line_args import CmdLineArgs

class TestCmdLineArgs :
    
    @classmethod
    def setup_class(cls) :
        cls.inst = CmdLineArgs()

    def test__generate_answer__excluding_0(self, monkeypatch) :
        monkeypatch.setattr(random, 'randint', lambda a, b: 7)
        assert self.inst.generate_answer() == 7

