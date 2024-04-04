class CPU_simulator:
    def __init__(self):
        self.pc = 0  # Program Counter
        self.memory = {}  # Simple memory model for registers
        self.memory_limit = 8  # Limit for the number of variables
        # Initialize subsystems as needed, for example:
        self.subsystems = {i: None for i in range(10)}  # Dummy subsystems 0-9

    def load_program(self, program):
        """Load the program into the CPU."""
        self.program = program
        self.pc = 0  # Reset program counter

    def parse_instruction(self, instruction):
        """Parse the instruction into operation and operands."""
        parts = instruction.split()
        operation = parts[0]
        operands = parts[1:]
        if len(operands) > 2:
            operation = "NOP"
            print(f"PC : {self.pc} | Instruction overflow error, running NOP ")
        return operation, operands

    def set_memory(self, key, value):
        """Set a value in memory, respecting the memory limit."""
        if key in self.memory or len(self.memory) < self.memory_limit:
            self.memory[key] = value
        else:
            print(f"Memory limit reached. Cannot allocate '{key}'.")

    def syscall(self, value, subsystem_id):
        """Handle a system call to a designated subsystem."""
        # Placeholder for subsystem interaction logic
        print(f"Sending {value} to subsystem {subsystem_id}")
        # Here, you'd include logic for interacting with the specific subsystem
        # For example, adjusting power levels, sending communications, etc.

    def execute_program(self):
        """Execute the loaded program."""
        while self.pc < len(self.program):
            instruction = self.program[self.pc]
            operation, operands = self.parse_instruction(instruction)
            
            # Adjusted memory operations to use set_memory method
            if operation == "LOAD":
                self.set_memory(operands[0], int(operands[1]))
            elif operation == "SYSCALL":
                # Extract the value and subsystem_id from operands
                value = self.memory.get(operands[0], "Undefined")
                subsystem_id = int(operands[1])
                self.syscall(value, subsystem_id)
            elif operation == "ADD":
                self.set_memory(operands[0], self.memory.get(operands[0], 0) + self.memory.get(operands[1], 0))
            elif operation == "ADDI":
                self.set_memory(operands[0], self.memory.get(operands[0], 0) + int(operands[1]))
            elif operation == "SUB":
                self.set_memory(operands[0], self.memory.get(operands[0], 0) - self.memory.get(operands[1], 0))
            elif operation == "LSHIFT":
                self.set_memory(operands[0], self.memory.get(operands[0], 0) << int(operands[1]))
            elif operation == "RSHIFT":
                self.set_memory(operands[0], self.memory.get(operands[0], 0) >> int(operands[1]))
            elif operation == "JMP":
                self.pc = int(operands[0]) - 1  # Jump to instruction at index
            elif operation == "LOG":
                print("PC :", self.pc, "| MEM :", operands[0], ":=", self.memory.get(operands[0], "Undefined"))
            elif operation == "NOP":
                pass
            
            self.pc += 1  # Move to the next instruction unless JMP changes it

    def run(self):
        """Convenience method to execute the program."""
        self.execute_program()

class Power_management:
    def __init__(self):
        self.power_level = 100  # Initial power level
        self.power_saving_mode = False

    def adjust_power(self, adjustment):
        self.power_level += adjustment
        self.power_level = min(max(self.power_level, 0), 100)  # Keep within 0-100

    def toggle_power_saving(self):
        self.power_saving_mode = not self.power_saving_mode

class Communication_systems:
    pass