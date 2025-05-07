# Lexical Analysis: Role of a Lexical analyzer, Specification and recognition of tokens, Symboltable, lexical Analyzer Generator.

import re

class LexicalAnalyzer:
    def __init__(self):
        # Define token specifications using regular expressions (regex)
        self.token_specs = [
            ('KEYWORD', r'\b(if|else|while|for)\b'),         # Keywords like if, else, while, for
            ('IDENTIFIER', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),  # Identifiers: variable names or function names
            ('NUMBER', r'\b\d+\b'),                          # Numbers (integers)
            ('OPERATOR', r'[+\-*/=]'),                       # Operators: +, -, *, /, =
            ('PUNCTUATION', r'[;,\(\)\{\}]'),                # Punctuation: semicolons, commas, parentheses, curly braces
            ('WHITESPACE', r'[ \t\n]+'),                     # Whitespace (spaces, tabs, newlines)
            ('COMMENT', r'//[^\n]*'),                        # Comments (single-line)
            ('UNKNOWN', r'.'),                               # Any other character (unknown tokens)
        ]
        
        # Create a compiled regex for each token type
        self.regexes = [(name, re.compile(pattern)) for name, pattern in self.token_specs]

        # Symbol table to store identifiers
        self.symbol_table = {}

    def tokenize(self, source_code):
        """
        Tokenizes the source code into a list of tokens.
        """
        tokens = []
        position = 0

        while position < len(source_code):
            match = None
            for token_name, regex in self.regexes:
                match = regex.match(source_code, position)
                if match:
                    lexeme = match.group(0)
                    if token_name == 'IDENTIFIER' and lexeme not in self.symbol_table:
                        # Add identifiers to the symbol table
                        self.symbol_table[lexeme] = len(self.symbol_table) + 1
                    if token_name != 'WHITESPACE' and token_name != 'COMMENT':  # Ignore whitespaces and comments
                        tokens.append((token_name, lexeme))
                    position = match.end()  # Move the position forward
                    break
            if not match:
                raise ValueError(f"Invalid token at position {position}")
        
        return tokens

    def print_tokens(self, tokens):
        """
        Print out the tokenized source code.
        """
        for token_type, lexeme in tokens:
            print(f"{token_type}: {lexeme}")

    def print_symbol_table(self):
        """
        Print the symbol table (all identifiers encountered).
        """
        print("\nSymbol Table:")
        for identifier, address in self.symbol_table.items():
            print(f"{identifier}: {address}")

# Example usage:

source_code = """
if (x == 10) {
    y = 20;
    // This is a comment
    while (y > x) {
        x = x + 1;
    }
} else {
    z = 30;
}
"""

# Instantiate the lexical analyzer
lexical_analyzer = LexicalAnalyzer()

# Tokenize the source code
tokens = lexical_analyzer.tokenize(source_code)

# Print the tokens
print("Tokens:")
lexical_analyzer.print_tokens(tokens)

# Print the symbol table
lexical_analyzer.print_symbol_table()
