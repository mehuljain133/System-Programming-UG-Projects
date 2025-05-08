%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
%}

%token A B

%%

/* Grammar rules for the language a^n b, n >= 10 */

start:
    A A A A A A A A A A B    { printf("Valid input\n"); }
    | A A A A A A A A A A start B  { printf("Valid input\n"); }
    ;

%%

int main() {
    printf("Enter a string (a^n b, n>=10):\n");
    yyparse();
    return 0;
}

int yylex() {
    char c = getchar();
    
    /* Ignore spaces and newlines */
    while (c == ' ' || c == '\n') {
        c = getchar();
    }

    if (c == EOF) {
        return 0;  // End of input
    }

    if (c == 'a') {
        return A;
    }

    if (c == 'b') {
        return B;
    }

    return 0;  // Invalid character
}

void yyerror(const char *s) {
    printf("Invalid input\n");
}
