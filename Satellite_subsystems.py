import time

class CPU_simulator:
    def __init__(self):
        self.pc           = 0   # Program Counter
        self.memory       = {}  # Simple memory model for registers
        self.memory_limit = 8   # Limit for the number of variables
        self.stack        = []  # Simple memory model for a stack # TODO: Implement using append(), pop()
        self.program      = []  # List of instructions currently loaded
        self.labels       = {}  # List of labels for current programs branch logic

        self.syscall_list = []  # Simple list in order to ensure a time-slot of delay for syscalls

        # Initialize subsystems
        power_management  = Power_management()
        coms_system       = Communication_system()
        navigation_system = Navigation_system()
        data_collection   = Data_collection()
        thermal_control   = Thermal_control()
        mag_coil_storage  = Mag_coil_storage()
        self.subsytem   = {
            0: power_management,
            1: coms_system,
            2: navigation_system,
            3: data_collection,
            4: thermal_control,
            5: mag_coil_storage,
            #6: 
        }
        self.subsytem_power = {
            0: True,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            #6:
        }
        self.amount_of_subsystems = len(self.subsytem)

    def load_main(self):
        self.program = self.subsytem[5].programs["main.asm"]

    def load_program(self, program):
        """Load the program into the CPU."""
        self.program = program
        self.pc = 0  # Reset program counter

    def parse_instruction(self, instruction):
        """Parse the instruction into operation and operands."""

        # Check for a label definition
        if instruction.endswith(':'):
            label = instruction[:-1]
            return ('LABEL', label)

        parts = instruction.split()
        operation = parts[0]
        operands = parts[1:]
        if len(operands) > 2:
            operation = "NOP"
            print(f"PC : {self.pc} | Instruction overflow error, running NOP ")
        return operation, operands
    
    def parse_program(self, program_lines):
        labels = {}
        instructions = []
        
        for line_number, line in enumerate(program_lines, start=0):
            result = self.parse_instruction(line)
            if result is None:
                #print(result) # TODO: DEBUG
                continue  # Skip empty or comment-only lines
            
            operation = result[0]
            operand  = result[1] 
            #time.sleep(1) # TODO: DEBUG
            if operation == 'LABEL':
                #print("SETTING LINE NUMBER:", line_number) # TODO: DEBUG
                #time.sleep(1) # TODO: DEBUG
                labels[operand] = line_number  # Store label with its line number
            else:
                instructions.append(line)
        #print("LABELS: ",labels) # TODO: DEBUG
        #time.sleep(5) # TODO: DEBUG
        return instructions, labels

    def set_memory(self, key, value):
        """Set a value in memory, respecting the memory limit."""
        if key in self.memory or len(self.memory) < self.memory_limit:
            self.memory[key] = value
        else:
            print(f"Memory limit reached. Cannot allocate '{key}'.")

    def syscall(self, value, subsystem_id):
        """Direct system calls to the appropriate subsystem based on the ID."""
        # Placeholder for subsystem interaction logic
        subsystem = self.subsytem.get(subsystem_id)
        #print(subsystem) #TODO: DEBUG
        if subsystem:
            
            # Power management
            if subsystem_id == 0:
                if value >= 0 and value <= self.amount_of_subsystems:
                    self.subsytem[0].toggle_subsystem_power(self, value)

            # Communication systems
            if subsystem_id == 1:  
                if value == 0:
                    if subsystem.read_data() != 1:
                        print(f"Error in subsystem{subsystem_id}")
                elif value == 1:
                    #print(subsystem.received_program) # TODO: DEBUG
                    self.program, self.labels = self.parse_program(subsystem.received_program)
                    self.pc = -1 # Set to -1 since pc will increment after returning.
                    # TODO: MAYBE SAVE WHERE YOU WERE USING THE STACK...
                else:
                    print(f"") # TODO: What?----

            # Magnetic coils storage
            elif subsystem_id == 5: # TODO: NOT TESTED
                if value >= 0 and value <= 9:
                    """Load program from Communications Systems into magnetic coil pos 0"""
                    self.subsytem[5].load_from_communication_system(value, self.subsytem[1])
                elif value <= 19:
                    """Load program from mag coil storage"""
                    self.program = self.subsytem[5].get_from_Mag_coil_storage(value)
                    self.pc = -1 # Set to -1 since pc will increment after returning.

            # Add handling for other subsystems...
        else:
            print(f"Subsystem {subsystem_id} not found.")

    def execute_program(self):
        """Execute the loaded program."""
        while self.pc < len(self.program):
            instruction = self.program[self.pc]
            operation, operands = self.parse_instruction(instruction)
            
            #print("PC ",self.pc) #TODO: DEBUG

            # Adjusted memory operations to use set_memory method
            if operation == "LOAD":
                self.set_memory(operands[0], int(operands[1]))
            elif operation == "SYSCALL":
                self.syscall_list.append(instruction)
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
            elif operation == "JMPZ":
                if self.memory.get(operands[0], 0) == 0:
                    #print("label name", operands[1], "LABEL ADRESS ", self.labels.get(operands[1], 0) - 1) # TODO: DEBUG
                    self.pc = self.labels.get(operands[1], 0) - 1
            elif operation == "LOG":
                print("PC :", self.pc, "| MEM :", operands[0], ":=", self.memory.get(operands[0], "Undefined"))
            elif operation == "NOP":
                pass

            # Handle any if all delayed syscalls
            if len(self.syscall_list) > 0:
                call = self.syscall_list.pop()
                call_operation, call_operands = self.parse_instruction(call) # call_operation is not needed.
                # Extract the value and subsystem_id from operands
                value = int(self.memory.get(call_operands[0], "Undefined"))
                subsystem_id = int(call_operands[1])
                print(f"Sending {value} to subsystem {subsystem_id}")
                self.syscall(value, subsystem_id)
            
            self.pc += 1  # Move to the next instruction unless JMP changes it

    def run(self):
        """Convenience method to execute the program."""
        if len(self.program) > 0:
            self.execute_program()
        else:
            self.load_main()
            self.execute_program()

class Power_management:
    def __init__(self):
        self.power_level = 100  # Initial power level
        self.max_power_level = 100
        self.min_power_level = 20
        self.power_saving_mode = False

    def adjust_power(self, adjustment):
        new__power_level = self.power_level + adjustment
        if new__power_level < self.max_power_level and new__power_level > self.min_power_level:
            self.power_level = new__power_level
            return 1
        else:
            return 0

    def toggle_subsystem_power(self, computer, arg):
        computer.subsystem_power[arg] = not computer.subsystem.power[arg] # TODO: Maybe save the power state as a dict in the main class.
        sucess = 0
        if computer.subsystem_power:
            sucess = self.adjust_power(20)
        else:
            sucess = self.adjust_power(-20)
        return sucess

    def toggle_power_saving(self):
        self.power_saving_mode = not self.power_saving_mode

class Communication_system:
    def __init__(self):
        # Initialize any necessary variables
        self.received_program = []

    def read_data(self, filepath='input.asm'):
        """Reads a program from a file, strips comments, and stores it for execution."""
        try:
            with open(filepath, 'r') as file:
                # Read and strip out comments
                program_with_comments = file.readlines()
                program_clean = [self.strip_comments(line) for line in program_with_comments]
                
                # Store cleaned and non-empty lines in received_program
                self.received_program = [line for line in program_clean if line.strip()]
            print("Program loaded successfully.")
        except FileNotFoundError:
            print(f"File {filepath} not found.")
            return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
        return 1
    
    def strip_comments(self, line):
        """Removes comments and trailing spaces from a line."""
        comment_index = line.find('#')
        if comment_index != -1:
            return line[:comment_index].strip()
        return line.strip()
    
class Navigation_system:
    def __init__(self):
        pass

class Data_collection:
    def __init__(self):
        pass

class Thermal_control:
    def __init__(self):
        pass

class Mag_coil_storage:
    def __init__(self):
        self.programs = {
            "main.asm" : ["LOAD A 0","SYSCALL A 1", "LOAD A 1", "SYSCALL A 1"],
            "0" : []
        }
    
    def load_from_communication_system(self, arg, com_sys):
        self.programs[str(arg)] = com_sys.program()

    def get_from_Mag_coil_storage(self, arg):
        return self.programs.get(str(arg))

if __name__ == "__main__":
    cpu = CPU_simulator()
    cpu.run()