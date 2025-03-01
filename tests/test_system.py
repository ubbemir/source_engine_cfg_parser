import unittest

import src.formatters as formatters

from lark import Lark

def get_parser():
    with open("source_cfg.lark", "r") as file:
        cfg_grammar = file.read()
    return Lark(cfg_grammar, parser="earley")

class TestFormatter(unittest.TestCase):
    def test_minify_1(self):
        test_input = """
            bot_kick
            sv_cheats 1
            mp_restartgame 1
        """
        minified = formatters.minify_cfg(get_parser().parse(test_input))
        self.assertEqual(minified, "bot_kick;sv_cheats 1;mp_restartgame 1")


if __name__ == "__main__":
    unittest.main()