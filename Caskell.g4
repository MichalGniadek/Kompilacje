grammar Caskell;

/*
 * Parser Rules
 */

prog: (include | func)* EOF;

include: From includePath Include Identifier ';';

includePath: Identifier ('.' Identifier)*;

func: Func Identifier '(' argList ')' ('->' type)? block;

argList: (Identifier (':' type)? (',' Identifier (':' type)?)*)?;

block: '{' (let | do)* expr '}';

let: Let Identifier '=' expr ';';
do: Do (Identifier Arrow)? expr ';';

expr:
	expr Operator expr											# operation
	| (Number)													# number
	| (Identifier)												# identifier
	| ('(' expr ')')											# parens
	| (FuncIdentifier '(' ')')									# call
	| (FuncIdentifier '(' (Identifier (',' Identifier)*)? ')')	# call
	| '(' expr (',' expr)+ ')'									# tuple
	| (If expr block Else block)								# if;

struct:
	Identifier (
		'<' Identifier (':' Identifier)? (
			',' Identifier (':' Identifier)?
		)* '>'
	)? typeDef;

typeDef:
	Identifier
	| Identifier '(' type (',' type)* ')'
	| Identifier '{' Identifier ':' type (
		',' Identifier ':' type
	)* '}';

type:
	Identifier
	| type ('|' type)+
	| '(' type (',' type)+ ')'
	| type '<' type (',' type)* '>';

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

FuncIdentifier: Identifier | ('(' Operator ')');

Operator: [*<>+$=-]+ | ('`' Identifier '`');

Number: [0-9]+;
Whitespace: [ \t\r\n]+ -> skip;

LeftParen: '(';
RightParen: ')';
LeftBrace: '{';
RightBrace: '}';
LeftBracket: '[';
RightBracket: ']';
