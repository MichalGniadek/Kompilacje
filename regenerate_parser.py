import os
os.system(
    "antlr4 -o myparser -Dlanguage=Python3 -no-listener -visitor -Werror Caskell.g4")
