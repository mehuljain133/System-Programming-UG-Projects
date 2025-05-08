%{
#include <stdio.h>
#include <string.h>

// List of keywords in a simple C-like language
const char* keywords[] = {
    "int", "float", "if", "else", "for", "while", "return", "void"
};
int is_keyword(const char *str) {
    for (int i = 0; i < sizeof(keywords)/sizeof(keywords[0]); i++) {
        if (strcmp(str, keywords[i]) == 0) return 1;
    }
    return 0;
}
%}

%%

"//".*                        { printf("Comment: %s\n", yytext); }

"/*"([^*]|\*+[^*/])*\*+"/"    { printf("Comment: %s\n", yytext); }

[0-9]+\.[0-9]+                { printf("Float: %s\n", yytext); }

[0-9]+                        { printf("Integer: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*        {
                                if (is_keyword(yytext))
                                    printf("Keyword: %s\n", yytext);
                                else
                                    printf("Identifier: %s\n", yytext);
                              }

[+\-*/=<>!&|]+                { printf("Operator: %s\n", yytext); }

[ \t\n]+                     { /* Skip whitespace */ }

.                            { printf("Unknown: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    yylex();  // Start scanning
    return 0;
}

int yywrap() {
    return 1;
}
