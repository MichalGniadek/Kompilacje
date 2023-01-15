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


    # Visit a parse tree produced by CaskellParser#if.
    def visitIf(self, ctx:CaskellParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#operation.
    def visitOperation(self, ctx:CaskellParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#struct.
    def visitStruct(self, ctx:CaskellParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#typeDef.
    def visitTypeDef(self, ctx:CaskellParser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaskellParser#type.
    def visitType(self, ctx:CaskellParser.TypeContext):
        return self.visitChildren(ctx)



del CaskellParser