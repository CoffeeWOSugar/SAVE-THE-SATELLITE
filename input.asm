# TEST FILE
LOAD A 10
LOAD B 5
ADD A B         # A = A + B -> A = 10 + 5
ADDI A 3        # A = A + 3 -> A = 15 + 3
SUB A B         # A = A - B -> A = 18 - 5
LOAD C 2
LSHIFT A 1      # A = A << 1 -> A = 13 << 1
RSHIFT C 1      # C = C >> 1 -> C = 2 >> 1
LOG A           # Should log 26
LOG C           # Should log 1
ADD A A A       # Should log an error
LOAD D 0
JMPZ D skip
NOP
LOG A A A       # SHOULD BE SKIPPED AND GETS SKIPPED !!! 
skip:
LOG A