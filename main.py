import os
import sys
from antlr4.tree.Trees import Trees
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

    # def visitTerminal(self, node):
    #     if node.symbol.type == Token.EOF:
    #         return None
    #     return str(node)


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CaskellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CaskellParser(stream)
    tree = parser.prog()
    visitor = Visitor()
    result = visitor.visit(tree)
    if len(argv) > 2:
        with open(argv[2], 'w', encoding='utf8') as f:
            f.write(result)
    else:
        print(result)


if __name__ == '__main__':
    main(sys.argv)
