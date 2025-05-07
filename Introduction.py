# Introduction: Overview of compilation, Phases of a compiler.

class Compiler:
    def __init__(self):
        self.symbol_table = {}
        self.intermediate_code = []
        self.optimized_code = []

    # Phase 1: Lexical Analysis (Scanner)
    def lexical_analysis(self, source_code):
        """
        Breaks the source code into tokens.
        """
        tokens = source_code.split()
        return tokens

    # Phase 2: Syntax Analysis (Parser)
    def syntax_analysis(self, tokens):
        """
        Parses the tokens into a simple syntax tree.
        Here, we assume a very basic syntax structure for simplicity.
        """
        syntax_tree = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                syntax_tree.append(f"Operator: {token}")
            elif token.isdigit():
                syntax_tree.append(f"Operand: {token}")
            else:
                syntax_tree.append(f"Identifier: {token}")
        return syntax_tree

    # Phase 3: Semantic Analysis
    def semantic_analysis(self, syntax_tree):
        """
        Check for semantic errors like undeclared variables and mismatched types.
        """
        for node in syntax_tree:
            if "Identifier" in node and node.split(": ")[1] not in self.symbol_table:
                print(f"Semantic Error: {node.split(': ')[1]} is undeclared!")
                return False
        return True

    # Phase 4: Intermediate Code Generation
    def intermediate_code_generation(self, syntax_tree):
        """
        Generate an intermediate code representation (IR).
        """
        intermediate = []
        for node in syntax_tree:
            if "Operator" in node:
                intermediate.append(f"OP {node.split(': ')[1]}")
            elif "Operand" in node:
                intermediate.append(f"LOAD {node.split(': ')[1]}")
            elif "Identifier" in node:
                intermediate.append(f"STORE {node.split(': ')[1]}")
        return intermediate

    # Phase 5: Optimization
    def optimize(self, intermediate_code):
        """
        Simple optimization step: Remove redundant load/store operations.
        """
        optimized = []
        previous = None
        for instruction in intermediate_code:
            if previous and instruction == previous:
                continue
            optimized.append(instruction)
            previous = instruction
        return optimized

    def compile(self, source_code):
        # Phase 1: Lexical Analysis
        print("Phase 1: Lexical Analysis")
        tokens = self.lexical_analysis(source_code)
        print("Tokens:", tokens)
        
        # Phase 2: Syntax Analysis
        print("\nPhase 2: Syntax Analysis")
        syntax_tree = self.syntax_analysis(tokens)
        print("Syntax Tree:", syntax_tree)

        # Phase 3: Semantic Analysis
        print("\nPhase 3: Semantic Analysis")
        if not self.semantic_analysis(syntax_tree):
            print("Compilation aborted due to semantic errors.")
            return
        
        # Phase 4: Intermediate Code Generation
        print("\nPhase 4: Intermediate Code Generation")
        self.intermediate_code = self.intermediate_code_generation(syntax_tree)
        print("Intermediate Code:", self.intermediate_code)

        # Phase 5: Optimization
        print("\nPhase 5: Optimization")
        self.optimized_code = self.optimize(self.intermediate_code)
        print("Optimized Code:", self.optimized_code)


# Example usage
compiler = Compiler()

# Example source code
source_code = "a + 5 * b"

# Simulate declaring variables
compiler.symbol_table = {'a': 10, 'b': 20}

# Compile the source code
compiler.compile(source_code)
