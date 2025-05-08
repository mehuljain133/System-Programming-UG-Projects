%{
int line_count = 0;
int char_count = 0;
%}

%%

\n         { line_count++; char_count++; }
.          { char_count++; }

%%

int main(int argc, char **argv) {
    yylex();  // Start scanning
    printf("Total characters: %d\n", char_count);
    printf("Total lines: %d\n", line_count);
    return 0;
}

int yywrap() {
    return 1;
}
