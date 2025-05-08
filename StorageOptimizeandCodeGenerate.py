# Storage organization & Code generation: Activation records, stack allocation, Object code generation

class ActivationRecord:
    def __init__(self, name, return_address):
        self.name = name
        self.return_address = return_address
        self.locals = {}
        self.stack_offset = 0  # for local variable offsets
        print(f"\n[Enter] Function: {self.name}")

    def allocate_local(self, var_name):
        self.locals[var_name] = self.stack_offset
        self.stack_offset += 4  # 4 bytes for each local variable

    def get_offset(self, var_name):
        return self.locals.get(var_name, None)

    def __str__(self):
        return f"ActivationRecord({self.name}): Locals -> {self.locals}"

# Simulate a call stack
call_stack = []

# Object code instructions
object_code = []

def emit(instruction):
    object_code.append(instruction)

def call_function(func_name, args):
    # Push activation record
    ar = ActivationRecord(func_name, return_address="ret_main")
    call_stack.append(ar)

    # Allocate locals for this function
    for arg in args:
        ar.allocate_local(arg)

    # Simulate body
    if func_name == "main":
        # main() has 2 local variables
        ar.allocate_local("x")
        ar.allocate_local("y")

        emit("MOV R1, 5")
        emit("STORE R1, [BP - {}]".format(ar.get_offset("x")))

        emit("MOV R2, 10")
        emit("STORE R2, [BP - {}]".format(ar.get_offset("y")))

        emit("ADD R3, R1, R2")
        emit("STORE R3, [BP - {}]".format(ar.get_offset("x")))

    elif func_name == "sum":
        # sum(a, b): return a + b
        emit("LOAD R1, [BP - {}]".format(ar.get_offset("a")))
        emit("LOAD R2, [BP - {}]".format(ar.get_offset("b")))
        emit("ADD R3, R1, R2")
        emit("RET R3")

    # Pop activation record
    print(ar)
    print(f"[Exit] Function: {ar.name}\n")
    call_stack.pop()

# Simulate program execution
call_function("main", [])

# Simulate calling another function
call_function("sum", ["a", "b"])

# Print object code
print("Generated Object Code:\n")
for line in object_code:
    print(line)
