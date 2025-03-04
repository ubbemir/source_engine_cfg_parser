import unittest
from os import listdir
from os.path import isfile, join

from lark import Lark

import src.formatters as formatters


def get_parser():
    with open("source_cfg.lark", "r") as file:
        cfg_grammar = file.read()
    return Lark(cfg_grammar, parser="earley")

class TestFormatter(unittest.TestCase):
    def test_minify_simple(self):
        test_input = """
            bot_kick
            sv_cheats 1
            mp_restartgame 1
        """
        minified = formatters.minify_cfg(get_parser().parse(test_input))
        self.assertEqual(minified, "bot_kick;sv_cheats 1;mp_restartgame 1")

    def test_minify_whitespaces(self):
        test_input = """


            
            bot_kick   

               
            sv_cheats 1
             
            
            mp_restartgame 1




        """
        minified = formatters.minify_cfg(get_parser().parse(test_input))
        self.assertEqual(minified, "bot_kick;sv_cheats 1;mp_restartgame 1")

    def test_minify_complex(self):
        test_input = """
            bind "mouse4" "+jump;+right";;
            sv_cheats 1; mp_restartgame 1 "apart of the previous" // comment not present;;;;;;;
            bot_kick;;
            bind "space" +jump
        """
        minified = formatters.minify_cfg(get_parser().parse(test_input))
        self.assertEqual(minified, """bind "mouse4" "+jump;+right";sv_cheats 1;mp_restartgame 1 "apart of the previous";bot_kick;bind "space" +jump""")

    def test_cfg_files(self):
        parser = get_parser()
        path = "tests/cfg"
        files = [f for f in listdir(path) if isfile(join(path, f))]

        for file_name in files:
            with open(join(path, file_name), "r") as file:
                content = file.read()

            # Just ensure it parses without failure
            try:
                parser.parse(content)
            except Exception:
                self.fail(f"Failure in file {file_name}")



if __name__ == "__main__":
    unittest.main()
