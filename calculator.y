%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);

%}

%token NUMBER
%token ADD SUB MUL DIV
%token LPAREN RPAREN

%%

/* Grammar rules for arithmetic expressions */

expression:
    expression ADD term          { $$ = $1 + $3; }
    | expression SUB term        { $$ = $1 - $3; }
    | term                       { $$ = $1; }
    ;

term:
    term MUL factor              { $$ = $1 * $3; }
    | term DIV factor            { if ($3 == 0) { yyerror("Division by zero!"); YYABORT; } $$ = $1 / $3; }
    | factor                     { $$ = $1; }
    ;

factor:
    NUMBER                       { $$ = $1; }
    | LPAREN expression RPAREN   { $$ = $2; }
    ;

/* Lexical rules */
%%

int main() {
    printf("Enter an expression:\n");
    yyparse();
    return 0;
}

int yylex() {
    char c;
    
    /* Skip spaces */
    while ((c = getchar()) == ' ' || c == '\t');
    
    if (c == EOF) {
        return 0;
    }

    if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        int num;
        scanf("%d", &num);
        yylval = num;
        return NUMBER;
    }

    switch (c) {
        case '+': return ADD;
        case '-': return SUB;
        case '*': return MUL;
        case '/': return DIV;
        case '(': return LPAREN;
        case ')': return RPAREN;
        default: return 0;
    }
}

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}
