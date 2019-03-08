import os, sys
comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }


dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }


jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
    }

symbol_table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    }
for i in range(0,16):
	symbol = "R" + str(i)
	symbol_table[symbol] = i
variable_memory = 16

def parse(line):
	line = line.strip()
	line = line.replace(" ", "")
	if "//" in line:
		line = line.split("//")
		line = line[0]
	return line

def add_variable(variable):
	global variable_memory
	symbol_table[variable] = variable_memory
	variable_memory += 1
	return symbol_table[variable]  

def null(instruction):
	if ";" not in instruction:
		instruction = instruction + ";null"
	if "=" not in instruction:
		instruction = "null=" + instruction
	return instruction

def a_instruction(instruction):
	if instruction[1].isalpha():
		label = symbol_table.get(instruction[1:], "DNE")
		if label == "DNE":
			label = add_variable(instruction[1:])
			binary_instruction = bin(int(label))[2:].zfill(16)
		binary_instruction = bin(int(label))[2:].zfill(16)
	else:
		binary_instruction = bin(int(instruction[1:]))[2:].zfill(16)
	return binary_instruction

def c_instruction(instruction):
	instruction = null(instruction)
	instruction = instruction.split("=")
	dest_val = dest.get(instruction[0])
	temp = instruction[1].split(";")
	comp_val = comp.get(temp[0])
	jump_val = jump.get(temp[1])
	return comp_val, dest_val, jump_val

def a_or_c(instruction):
	if "@" in instruction:
		return a_instruction(instruction)
	elif "@" not in instruction:
		bits = c_instruction(instruction)
		return "111" + bits[0] + bits[1] + bits[2]

def first_pass():
	file = open(sys.argv[1] + ".asm")
	symbolless_file = open(sys.argv[1] + ".tmp", "w")
	file_lines = file.readlines()
	file.close()
	rom = 0

	for line in file_lines:
		parse_line = parse(line)
		line = line.replace("\n", "")
		if parse_line != "":
			if parse_line[0] == "(":
				symbol = parse_line[1:-1]
				symbol_table[symbol] = rom
				parse_line = ""
			else :
				rom += 1
				symbolless_file.write(parse_line + "\n")
	symbolless_file.close

def second_pass():
	symbolless_file = open(sys.argv[1] + ".tmp")
	symbolless = symbolless_file.readlines()
	symbolless_file.close
	binary_file = open(sys.argv[1] + ".hack", "w")

	for line in symbolless:
		line = line.replace("\n", "")
		binary_instruction = a_or_c(line)
		binary_file.write(binary_instruction + "\n")
	binary_file.close
	os.remove(sys.argv[1] +".tmp")

first_pass()
second_pass()
