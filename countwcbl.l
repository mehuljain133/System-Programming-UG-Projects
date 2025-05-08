%{
#include <stdio.h>
#include <ctype.h>

int word_count = 0;
int char_count = 0;
int space_count = 0;
int line_count = 0;
%}

%%

[a-zA-Z0-9_]+    { word_count++; char_count += yyleng; }

[ \t]+           { space_count += yyleng; char_count += yyleng; }

\n               { line_count++; char_count++; }

.                { char_count++; }

%%

int main(int argc, char **argv) {
    yylex();  // Start tokenizing

    printf("Total characters: %d\n", char_count);
    printf("Total words: %d\n", word_count);
    printf("Total blank spaces: %d\n", space_count);
    printf("Total lines: %d\n", line_count);

    return 0;
}

int yywrap() {
    return 1;
}
