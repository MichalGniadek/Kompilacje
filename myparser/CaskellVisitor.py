# Generated from Caskell.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CaskellParser import CaskellParser
else:
    from CaskellParser import CaskellParser

# This class defines a complete generic visitor for a parse tree produced by CaskellParser.

class CaskellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CaskellParser#prog.
    def visitProg(self, ctx:CaskellParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#include.
    def visitInclude(self, ctx:CaskellParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#includePath.
    def visitIncludePath(self, ctx:CaskellParser.IncludePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#func.
    def visitFunc(self, ctx:CaskellParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#argList.
    def visitArgList(self, ctx:CaskellParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeCall.
    def visitTypeCall(self, ctx:CaskellParser.TypeCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeArray.
    def visitTypeArray(self, ctx:CaskellParser.TypeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeArrow.
    def visitTypeArrow(self, ctx:CaskellParser.TypeArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeTuple.
    def visitTypeTuple(self, ctx:CaskellParser.TypeTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:CaskellParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeParens.
    def visitTypeParens(self, ctx:CaskellParser.TypeParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#block.
    def visitBlock(self, ctx:CaskellParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#let.
    def visitLet(self, ctx:CaskellParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#do.
    def visitDo(self, ctx:CaskellParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#call.
    def visitCall(self, ctx:CaskellParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#number.
    def visitNumber(self, ctx:CaskellParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#identifier.
    def visitIdentifier(self, ctx:CaskellParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#tuple.
    def visitTuple(self, ctx:CaskellParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#parens.
    def visitParens(self, ctx:CaskellParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#array.
    def visitArray(self, ctx:CaskellParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#if.
    def visitIf(self, ctx:CaskellParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#operation.
    def visitOperation(self, ctx:CaskellParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#switch.
    def visitSwitch(self, ctx:CaskellParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#identifierPattern.
    def visitIdentifierPattern(self, ctx:CaskellParser.IdentifierPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#parensPattern.
    def visitParensPattern(self, ctx:CaskellParser.ParensPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#numberPattern.
    def visitNumberPattern(self, ctx:CaskellParser.NumberPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#tuplePattern.
    def visitTuplePattern(self, ctx:CaskellParser.TuplePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#callPattern.
    def visitCallPattern(self, ctx:CaskellParser.CallPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#ignorePattern.
    def visitIgnorePattern(self, ctx:CaskellParser.IgnorePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#arrayPattern.
    def visitArrayPattern(self, ctx:CaskellParser.ArrayPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#operationPattern.
    def visitOperationPattern(self, ctx:CaskellParser.OperationPatternContext):
        return self.visitChildren(ctx)



del CaskellParser