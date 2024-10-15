import pytest

from random import randint
from calc_quiz.cmd_line_args import CmdLineArgs

class TestCmdLineArgs :
    
    @classmethod
    def setup_class(cls) :
        cls.inst = CmdLineArgs()

    def test__purse__randint(self) :
        arg = 'randint(1,9)+randint(1,9)'
    
    def test__purse__randint_num_option_cond_option(self, monkeypatch) :
        arg = 'randint(1,9)+randint(1,9) --num=10 --cond=1<ans<10'
        

