# Assemblers & Loaders, Linkers: One pass and two pass assembler, design of an assembler, Absolute loader, relocation and linking concepts, relocating loader and Dynamic Linking. 

# Define the Assembler class
class Assembler:
    def __init__(self):
        # Simplified opcode mapping
        self.opcodes = {
            'MOV': '0001', 'ADD': '0010', 'SUB': '0011', 'JMP': '0100'
        }
        self.symbol_table = {}

    def first_pass(self, assembly_code):
        """
        First pass: Process labels and generate basic machine code structure
        """
        machine_code = []
        address = 0
        for line in assembly_code:
            parts = line.split()
            if parts[0].isalpha():  # It's a label, add to symbol table
                self.symbol_table[parts[0]] = address
            else:
                machine_code.append(parts)
                address += 1
        return machine_code

    def second_pass(self, assembly_code, machine_code):
        """
        Second pass: Resolve addresses, generate final machine code
        """
        final_code = []
        for line in machine_code:
            if line[0] in self.symbol_table:  # Replace label with address
                address = self.symbol_table[line[0]]
                final_code.append(f"{self.opcodes[line[1]]} {address}")
            else:
                final_code.append(f"{self.opcodes[line[0]]} {line[1]}")
        return final_code


# Define the Loader class
class Loader:
    def __init__(self):
        self.memory = {}

    def load_program(self, program, start_address=0):
        """
        Load the program into memory from a given start address
        """
        memory_address = start_address
        for line in program:
            self.memory[memory_address] = line
            memory_address += 1
        return self.memory


# Define the Relocator class
class Relocator:
    def __init__(self):
        pass

    def relocate(self, program, relocation_factor):
        """
        Relocate the program by adding a relocation factor to each instruction's address.
        """
        relocated_program = []
        for line in program:
            parts = line.split()
            opcode = parts[0]
            address = int(parts[1]) + relocation_factor
            relocated_program.append(f"{opcode} {address}")
        return relocated_program


# Define the Linker class
class Linker:
    def __init__(self):
        self.external_symbols = {}

    def link(self, object_files):
        """
        Link multiple object files into one executable, resolving external references.
        """
        linked_code = []
        for file in object_files:
            for line in file:
                parts = line.split()
                if parts[1] in self.external_symbols:  # Resolve external symbols
                    linked_code.append(f"{parts[0]} {self.external_symbols[parts[1]]}")
                else:
                    linked_code.append(line)
        return linked_code

    def add_external_symbols(self, symbols):
        """
        Add external symbols for dynamic linking or inter-object linking.
        """
        self.external_symbols.update(symbols)


# Example usage

# Sample assembly code with labels
assembly_code_1 = [
    "START MOV R1, 0",  # Label: START
    "ADD R1, 5",  # No label
    "JMP END",  # Jump to END
    "END SUB R1, 1"  # Label: END
]

assembly_code_2 = [
    "START MOV R2, 10",  # Label: START
    "ADD R2, 2",  # No label
    "JMP FINISH",  # Jump to FINISH
    "FINISH SUB R2, 3"  # Label: FINISH
]

# Create assembler and process assembly code
assembler = Assembler()
machine_code_1 = assembler.first_pass(assembly_code_1)
machine_code_1 = assembler.second_pass(assembly_code_1, machine_code_1)

machine_code_2 = assembler.first_pass(assembly_code_2)
machine_code_2 = assembler.second_pass(assembly_code_2, machine_code_2)

print("Machine Code (Program 1):", machine_code_1)
print("Machine Code (Program 2):", machine_code_2)

# Simulate linking multiple object files
linker = Linker()
linker.add_external_symbols({'END': 100, 'FINISH': 200})  # Adding external symbols

linked_program = linker.link([machine_code_1, machine_code_2])
print("\nLinked Program:", linked_program)

# Relocate the program
relocator = Relocator()
relocated_program = relocator.relocate(linked_program, relocation_factor=500)
print("\nRelocated Program:", relocated_program)

# Load the program into memory
loader = Loader()
loaded_program = loader.load_program(relocated_program, start_address=1000)
print("\nLoaded Program into Memory:", loaded_program)
