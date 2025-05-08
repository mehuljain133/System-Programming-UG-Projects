%{
#include <stdio.h>
#include <string.h>

int identifier_count = 0;

// C language keywords
const char* keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "inline", "int", "long", "register", "restrict", "return",
    "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
    "union", "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof",
    "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn",
    "_Static_assert", "_Thread_local"
};

int is_keyword(const char* word) {
    int i;
    for (i = 0; i < sizeof(keywords)/sizeof(keywords[0]); ++i) {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }
    return 0;
}
%}

%%

[a-zA-Z_][a-zA-Z0-9_]* {
    if (!is_keyword(yytext)) {
        identifier_count++;
    }
}

.|\n { /* Ignore everything else */ }

%%

int main(int argc, char **argv) {
    yylex();
    printf("Total identifiers: %d\n", identifier_count);
    return 0;
}

int yywrap() {
    return 1;
}
