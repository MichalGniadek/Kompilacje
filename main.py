import argparse
import subprocess
import sys
from antlr4 import *
from myparser.CaskellLexer import CaskellLexer
from myparser.CaskellParser import CaskellParser
from myparser.CaskellVisitor import CaskellVisitor


class Visitor(CaskellVisitor):
    def visitProg(self, ctx: CaskellParser.ProgContext):
        return ("\n".join(c.accept(self) for c in ctx.include()) +
                "\n" +
                "\n".join(c.accept(self) for c in ctx.func()))

    def visitInclude(self, ctx: CaskellParser.IncludeContext):
        return f"import {ctx.includePath().accept(self)} ({ctx.Identifier()})"

    def visitIncludePath(self, ctx: CaskellParser.IncludePathContext):
        return ".".join([str(i) for i in ctx.Identifier()])

    def visitFunc(self, ctx: CaskellParser.FuncContext):
        name = str(ctx.Identifier())

        argList = ctx.argList().accept(self)
        if argList is not None:
            types, args = argList[0], argList[1]
        types = '->'.join(types)
        args = ' '.join(args)

        type_ = ctx.type_()
        return_type = f"-> {type_.accept(self)}" if type_ is not None else ''

        block = ctx.block().accept(self)

        type_line = ""
        if len(types) == len(args) and return_type:
            type_line = f"{name} :: {types} {return_type} \n"
        elif return_type == '' and len(types) != 0:
            print(f"error at {ctx.getSourceInterval()}, function {name}:\n" + 
                "\tyou can't provide parameter types without specyfing the return type", file=sys.stderr)
        elif return_type != '' and len(types) == 0 and len(args) != 0:
            print(f"error at {ctx.getSourceInterval()}, function {name}:\n" +
                "\tyou can't return type without specyfing the parameter type", file=sys.stderr)

        return f"{type_line}{name} {args} = {block}"

    def visitArgList(self, ctx: CaskellParser.ArgListContext):
        return ([c.accept(self) for c in ctx.type_()], [c.accept(self) for c in ctx.pattern()])

    def visitTypeIdentifier(self, ctx: CaskellParser.IdentifierContext):
        return ctx.getText()

    def visitTypeParens(self, ctx: CaskellParser.ParensContext):
        return f"( {ctx.type_().accept(self)} )"

    def visitTypeTuple(self, ctx: CaskellParser.TupleContext):
        children = [c.accept(self) for c in ctx.type_()]
        return f"({','.join(children)})"

    def visitTypeCall(self, ctx: CaskellParser.CallContext):
        [func, *args] = [e.accept(self) for e in ctx.type_()]
        return f"({func} ({' '.join(args)}))"

    def visiTypeArray(self, ctx: CaskellParser.CallContext):
        return f"[ {ctx.type_().accept(self)} ]"

    def visitTypeArrow(self, ctx: CaskellParser.CallContext):
        children = [c.accept(self) for c in ctx.type_()]
        return f"({'->'.join(children)})"

    def visitBlock(self, ctx: CaskellParser.BlockContext):
        children = [c.accept(self) for c in ctx.getChildren()][1:-1]
        return "".join(children)

    def visitLet(self, ctx: CaskellParser.LetContext):
        return f"let {ctx.Identifier()} = {ctx.expr().accept(self)} in "

    def visitDo(self, ctx: CaskellParser.DoContext):
        var = ''
        if ctx.Identifier() is not None:
            var = f"{ctx.Identifier()} <-"
        return f"do {var} {ctx.expr().accept(self)}; "

    def visitIdentifier(self, ctx: CaskellParser.IdentifierContext):
        return ctx.getText()

    def visitCall(self, ctx: CaskellParser.CallContext):
        [func, *args] = [e.accept(self) for e in ctx.expr()]
        return f"({func} ({' '.join(args)}))"

    def visitNumber(self, ctx: CaskellParser.NumberContext):
        return ctx.getText()

    def visitTuple(self, ctx: CaskellParser.TupleContext):
        children = [c.accept(self) for c in ctx.expr()]
        return f"({','.join(children)})"

    def visitParens(self, ctx: CaskellParser.ParensContext):
        return f"( {ctx.expr().accept(self)} )"

    def visitIf(self, ctx: CaskellParser.IfContext):
        cond = ctx.expr().accept(self)
        [ifTrue, ifFalse] = [c.accept(self) for c in ctx.block()]
        return f"if {cond} then {ifTrue} else {ifFalse}"

    def visitOperation(self, ctx: CaskellParser.OperationContext):
        [left, right] = [c.accept(self) for c in ctx.expr()]
        return f"{left} {ctx.Operator()} {right}"

    def visitSwitch(self, ctx: CaskellParser.SwitchContext):
        [_, expr, _, *rest, _] = [c.accept(self) for c in ctx.getChildren()]
        cases = [rest[i+1:i + 3] for i in range(0, len(rest), 3)]
        cases = [f"{pattern} -> {expr}" for pattern, expr in cases]
        return f"case {expr} of {';'.join(cases)};"

    def visitParensPattern(self, ctx: CaskellParser.ParensPatternContext):
        return f"( {ctx.pattern().accept(self)} )"

    def visitTuplePattern(self, ctx: CaskellParser.TuplePatternContext):
        children = [c.accept(self) for c in ctx.pattern()]
        return f"({','.join(children)})"

    def visitCallPattern(self, ctx: CaskellParser.CallPatternContext):
        args = [e.accept(self) for e in ctx.pattern()]
        return f"({ctx.Identifier().accept(self)} ({' '.join(args)}))"

    def visitOperationPattern(self, ctx: CaskellParser.OperationPatternContext):
        [left, right] = [c.accept(self) for c in ctx.pattern()]
        return f"{left} {ctx.Operator()} {right}"

    def visitTerminal(self, node):
        return str(node)


def run_command(command: str, stdin: str) -> str:
    def run(command):
        return subprocess.run(command, shell=True,
                              input=stdin, text=True,
                              encoding="utf8", capture_output=True)
    result = run(command)
    if result.returncode == 0:
        return result.stdout

    result = run(f"wsl bash -i -c '{command}'")
    return result.stdout


def format(text: str) -> str:
    return run_command("hfmt -", text) or text


def run(text: str) -> str:
    return run_command("runghc", text) or "Couldn't run :("


def transpile(text: str) -> str:
    lexer = CaskellLexer(text)
    stream = CommonTokenStream(lexer)
    parser = CaskellParser(stream)
    tree = parser.prog()
    visitor = Visitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output-file")
    parser.add_argument("--no-formatting", action="store_true")
    parser.add_argument("-r", "--run", action="store_true")
    args = parser.parse_args()

    text = FileStream(args.input_file)
    result = transpile(text)

    if not args.no_formatting:
        result = format(result)

    if args.output_file is not None:
        with open(args.output_file, 'w', encoding='utf8') as f:
            f.write(result)

    if args.run:
        print(run(result))

    if not args.run and args.output_file is None:
        print(result)
