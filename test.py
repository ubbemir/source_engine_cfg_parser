from lark import Lark, Transformer, v_args


with open("source_cfg.lark", "r") as file:
    cfg_grammar = file.read()

cfg_parser = Lark(cfg_grammar, parser='earley')


with open("input.cfg", "r") as file:
    cfg_input = file.read()


print(cfg_parser.parse(cfg_input).pretty())