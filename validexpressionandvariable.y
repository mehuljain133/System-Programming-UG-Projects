%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER
%token VAR
%token ADD SUB MUL DIV
%token LPAREN RPAREN

%%

/* Grammar rules for arithmetic expressions */

expression:
    expression ADD term          { printf("Valid Expression: %s + %s\n", $1, $3); }
    | expression SUB term        { printf("Valid Expression: %s - %s\n", $1, $3); }
    | term                       { $$ = $1; }
    ;

term:
    term MUL factor              { printf("Valid Expression: %s * %s\n", $1, $3); }
    | term DIV factor            { printf("Valid Expression: %s / %s\n", $1, $3); }
    | factor                     { $$ = $1; }
    ;

factor:
    NUMBER                       { $$ = $1; }
    | VAR                        { $$ = $1; }
    | LPAREN expression RPAREN   { $$ = $2; }
    ;

/* Grammar rule for recognizing a variable: starts with a lowercase letter, followed by a digit */
VAR: [a-z][0-9] { printf("Valid variable: %s\n", yytext); }

%%

int main() {
    printf("Enter an expression:\n");
    yyparse();
    return 0;
}

int yylex() {
    char c;
    
    /* Skip spaces and newlines */
    while ((c = getchar()) == ' ' || c == '\n');
    
    if (c == EOF) {
        return 0;
    }
    
    if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    }
    
    if (c >= 'a' && c <= 'z') {
        ungetc(c, stdin);
        char str[10];
        scanf("%s", str);
        yylval = strdup(str); // Store the string in yylval
        return VAR;
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
