%{
#include <stdio.h>
#include <stdlib.h>
%}

// Define the possible tokens
digit   [0-9]
num     {digit}+            // Integer literal

%%

// Match any number
{num}   { printf("Number: %s\n", yytext); }

"+"     { printf("Operator: +\n"); }
"-"     { printf("Operator: -\n"); }
"*"     { printf("Operator: *\n"); }
"/"     { printf("Operator: /\n"); }

"("     { printf("Left Parenthesis: (\n"); }
")"     { printf("Right Parenthesis: )\n"); }

[ \t\n] { /* Ignore spaces, tabs, and newlines */ }

.       { printf("Invalid character: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    printf("Enter an arithmetic expression:\n");
    yylex();  // Start the lexer
    return 0;
}

int yywrap() {
    return 1;
}
