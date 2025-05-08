%{
#include <stdio.h>
#include <string.h>

char longest[1024] = "";
%}

%%

[a-zA-Z]+ {
    if (strlen(yytext) > strlen(longest)) {
        strcpy(longest, yytext);
    }
}

.|\n     { /* Ignore non-word characters */ }

%%

int main(int argc, char **argv) {
    yylex();
    printf("Longest word: %s\n", longest);
    return 0;
}

int yywrap() {
    return 1;
}
