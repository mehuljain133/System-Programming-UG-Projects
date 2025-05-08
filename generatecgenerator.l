%{
#include <stdio.h>
%}

%%
generate {
    printf("#include <stdio.h>\n");
    printf("#include <string.h>\n");
    printf("#include <stdbool.h>\n");
    printf("#include <stdlib.h>\n\n");

    printf("void swap(char *x, char *y) {\n");
    printf("    char temp = *x; *x = *y; *y = temp;\n");
    printf("}\n\n");

    printf("void permute(char *str, int l, int r) {\n");
    printf("    if (l == r) printf(\"%%s\\n\", str);\n");
    printf("    else {\n");
    printf("        for (int i = l; i <= r; i++) {\n");
    printf("            swap((str + l), (str + i));\n");
    printf("            permute(str, l + 1, r);\n");
    printf("            swap((str + l), (str + i)); // backtrack\n");
    printf("        }\n");
    printf("    }\n");
    printf("}\n\n");

    printf("void substrings(const char* str) {\n");
    printf("    int len = strlen(str);\n");
    printf("    for (int i = 0; i < len; i++) {\n");
    printf("        for (int j = i; j < len; j++) {\n");
    printf("            for (int k = i; k <= j; k++) putchar(str[k]);\n");
    printf("            putchar('\\n');\n");
    printf("        }\n");
    printf("    }\n");
    printf("}\n\n");

    printf("int main() {\n");
    printf("    char str[100];\n");
    printf("    printf(\"Enter a string: \");\n");
    printf("    scanf(\"%%s\", str);\n");
    printf("\n    printf(\"\\nAll substrings:\\n\");\n");
    printf("    substrings(str);\n");
    printf("\n    printf(\"\\nAll permutations:\\n\");\n");
    printf("    permute(str, 0, strlen(str) - 1);\n");
    printf("    return 0;\n");
    printf("}\n");
}
.|\n    ;
%%

int main() {
    yylex();
    return 0;
}
