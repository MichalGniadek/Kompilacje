grammar Caskell;

/*
 * Parser Rules
 */

prog: (include | func)* EOF;

include: From includePath Include Identifier ';';

includePath: Identifier ('.' Identifier)*;

func: Func Identifier '(' argList ')' block;

argList: (pattern (',' pattern)*)?;

block: '{' (let | do)* expr '}';

let: Let Identifier '=' expr ';';
do: Do (Identifier Arrow)? expr ';';

expr:
	expr Operator expr							# operation
	| (Number)									# number
	| expr '(' ')'								# call
	| expr '(' (expr (',' expr)*)? ')'			# call
	| (Identifier)								# identifier
	| ('(' Operator ')')						# identifier
	| ('(' expr ')')							# parens
	| '(' expr (',' expr)+ ')'					# tuple
	| (If expr block Else block)				# if
	| Switch expr '{' (Case pattern block)+ '}'	# switch;

pattern:
	pattern Operator pattern							# operationPattern
	| (Number)											# numberPattern
	| (Identifier)										# identifierPattern
	| ('(' pattern ')')									# parensPattern
	| (Identifier '(' (pattern (',' pattern)*)? ')')	# callPattern
	| '(' pattern (',' pattern)+ ')'					# tuplePattern
	| ('_')												# ignorePattern;

/*
 * Lexer Rules
 */

// Keywords
Func: 'func';
Do: 'do';
Let: 'let';
If: 'if';
Else: 'else';
Switch: 'switch';
Case: 'case';
Arrow: '<-';
From: 'from';
Include: 'include';

// Operators
fragment Letter: [a-zA-Z];
Identifier: (Letter | '_') (Letter | [0-9_] | '\'')*;

Operator: [:*<>+$=-]+ | ('`' Identifier '`');

Number: [0-9]+;
Whitespace: [ \t\r\n]+ -> skip;

LeftParen: '(';
RightParen: ')';
LeftBrace: '{';
RightBrace: '}';
LeftBracket: '[';
RightBracket: ']';
