# from enum import Enum

class ParameterMode():
    POSITION = 0
    IMMEDIATE = 1


class Operations:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    TERMINATE = 99

    # @staticmethod
    # def add(program, index):


NUM_PARAMS = {
    Operations.ADD: 3,
    Operations.MULTIPLY: 3,
    Operations.INPUT: 1,
    Operations.OUTPUT: 1,
    Operations.TERMINATE: 0,
}

# p = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,5,19,23,2,9,23,27,1,27,5,31,2,31,13,35,1,35,9,39,1,39,10,43,2,43,9,47,1,47,5,51,2,13,51,55,1,9,55,59,1,5,59,63,2,6,63,67,1,5,67,71,1,6,71,75,2,9,75,79,1,79,13,83,1,83,13,87,1,87,5,91,1,6,91,95,2,95,13,99,2,13,99,103,1,5,103,107,1,107,10,111,1,111,13,115,1,10,115,119,1,9,119,123,2,6,123,127,1,5,127,131,2,6,131,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
p = [
    3,225,
    1,225,6,6,
    1100,1,238,225,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]


def parameter(program: list, val: int, mode: int):
    # print("parameter", val, mode)
    if mode == ParameterMode.POSITION:
        # print("pos")
        val = program[val]
    # else:
        # print("no pos")
    return val

# def prepare_params(program: list, index):


def parse_instruction(program: list, inst_index: int):
    raw_inst = program[inst_index]
    opcode = raw_inst % 100
    num_params = NUM_PARAMS[opcode]
    param_modes = [ParameterMode.POSITION for _ in range(0, num_params)]
    raw_param_modes = raw_inst // 100
    for i in range(num_params):
        param_mode = raw_param_modes % 10
        param_modes[i] = param_mode
        raw_param_modes = raw_param_modes // 10

    params = [(program[inst_index + 1 + i], mode) for i, mode in enumerate(param_modes)]
    return opcode, params

def run_program(program, index_=0, input_=None, output_=None,):

    # print(program[:50])
    # print('start', index_)
    # if index_ == 6:
    #     import pdb; pdb.set_trace()
    # print('instruction', program[index_])
    opcode, params = parse_instruction(program, index_)
    # print('opcode', opcode)
    # print('params', params)
    if opcode == 99:
        return
    elif opcode in (1,2):
        new_index = index_ +  4
        (operand_1, operand_1_mode) , (operand_2, operand_2_mode) , (result_pos, result_pos_mode)  = params
        if result_pos_mode != 0:
            raise Exception(result_pos_mode)
        if opcode == 1:
            program[result_pos] = parameter(program, operand_1, operand_1_mode) + parameter(program, operand_2, operand_2_mode)
        else:
            program[result_pos] = parameter(program, operand_1, operand_1_mode) * parameter(program, operand_2, operand_2_mode)
    elif opcode in (3,4):
        new_index = index_ +  2
        operand_1, operand_1_mode = params[0]
        if opcode == 3:
            if operand_1_mode != 0:
                raise Exception(result_pos_mode)
            program[operand_1] = input_()
        elif opcode == 4:
            output_(parameter(program, operand_1, operand_1_mode))
    elif opcode in (5, 6):
        new_index = index_ +  2
        (operand_1, operand_1_mode) , (operand_2, operand_2_mode) = params
        if parameter(program, operand_1, operand_1_mode):
            
    run_program(program, new_index, input_, output_)


def run(base_program, input_, output_):
    p_ = list(base_program)  # clone p
    # p_[1:3] = [12, 2]
    # p_[1:3] = [noun, verb]
    run_program(p_, 0, input_, output_)
    return p_[0]


def main():
    inputs = [1]
    outputs = []
    def input_():
        return inputs.pop(0)
    def output_(val):
        outputs.append(val)

    run(p, input_, output_)
    print(outputs)
    # for noun in range(100):
    #     for verb in range(100):
    #         if run(p, noun, verb) == 19690720:
    #             print(noun*100 + verb)
    #             return
main()