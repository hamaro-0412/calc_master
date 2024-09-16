import pytest

from random import randint
from calc_quiz.cmd_line_args import CmdLineArgs

class TestCmdLineArgs :
    
    @classmethod
    def setup_class(cls) :
        cls.inst = CmdLineArgs()

    def test__generate_answer__excluding_0(self, monkeypatch) :
        print(randint(1,9))
        #tmp = 'f"{random.uniform(100,999):.3f}"'
        #print(eval(tmp))
        #x=3
        #print(f'{x:+1d}')
        #monkeypatch.setattr(random, 'randint', lambda a, b: 7)
        #assert self.inst.generate_answer() == 7

