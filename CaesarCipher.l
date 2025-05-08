%{
#include <stdio.h>

char shift_char(char c, int shift) {
    if (c >= 'a' && c <= 'z')
        return ((c - 'a' + shift) % 26) + 'a';
    else if (c >= 'A' && c <= 'Z')
        return ((c - 'A' + shift) % 26) + 'A';
    else
        return c;
}
%}

%%

[a-zA-Z]    { putchar(shift_char(yytext[0], 3)); }
.|\n        { putchar(yytext[0]); }

%%

int main(int argc, char **argv) {
    yylex();  // Start tokenizing
    return 0;
}

int yywrap() {
    return 1;
}
