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
        args = ' '.join(ctx.argList().accept(self))
        block = ctx.block().accept(self)
        return f"{name} {args} = {block}"

    def visitArgList(self, ctx: CaskellParser.ArgListContext):
        return [str(c) for c in ctx.Identifier()]

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

    def visitCall(self, ctx: CaskellParser.CallContext):
        return self.visitChildren(ctx)

    def visitNumber(self, ctx: CaskellParser.NumberContext):
        return ctx.getText()

    def visitTuple(self, ctx: CaskellParser.TupleContext):
        children = [c.accept(self) for c in ctx.expr()]
        return f"({','.join(children)})"

    def visitParens(self, ctx: CaskellParser.ParensContext):
        return self.visitChildren(ctx)

    def visitIf(self, ctx: CaskellParser.IfContext):
        return self.visitChildren(ctx)

    def visitOperation(self, ctx: CaskellParser.OperationContext):
        return self.visitChildren(ctx)

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
    return result.stdout or result.stderr


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
