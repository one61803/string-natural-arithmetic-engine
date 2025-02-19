
global debug_1, debug_2
debug_1 = False
debug_2 = False

def succ(digit_CH):
    "Successor function."
    if (digit_CH == ""):
        print("L6. ERROR")
    else:
        match digit_CH:
            case "0":
                return "1"
            case "1":
                return "2"
            case "2":
                return "3"
            case "3":
                return "4"
            case "4":
                return "5"
            case "5":
                return "6"
            case "6":
                return "7"
            case "7":
                return "8"
            case "8":
                return "9"
            case "9":
                return "10"
            case _:
                s = succ(digit_CH[-1])
                if (len(s) == 1):
                    return digit_CH[0:-1] + s
                else:
                    return succ(digit_CH[0:-1]) + s[1:2]

def pred(digit_CH):
    "Predecessor function."
    match digit_CH:
        case "0":
            return "0"
        case "1":
            return "0"
        case "2":
            return "1"
        case "3":
            return "2"
        case "4":
            return "3"
        case "5":
            return "4"
        case "6":
            return "5"
        case "7":
            return "6"
        case "8":
            return "7"
        case "9":
            return "8"
        case _:
            p = pred(digit_CH[-1])
            if not (p == digit_CH[-1]):
                return digit_CH[0:-1] + p
            else:
                return simplify(pred(digit_CH[0:-1]) + "9")

def simplify(number_ST):
    "Removes preceding zeroes."
    if (number_ST == ""):
        return "0"
    elif (len(number_ST) == 1):
        return number_ST
    elif number_ST[0] == "0":
        return simplify(number_ST[1:])
    else:
        return number_ST

def digit_plus_digit(digit1_CH, digit2_CH):
    "Adds two digits."
    match digit2_CH:
        case "0":
            return digit1_CH
        case "1":
            return succ(digit1_CH)
        case "2":
            return succ(succ(digit1_CH))
        case "3":
            return succ(succ(succ(digit1_CH)))
        case "4":
            return succ(succ(succ(succ(digit1_CH))))
        case "5":
            return succ(succ(succ(succ(succ(digit1_CH)))))
        case "6":
            return succ(succ(succ(succ(succ(succ(digit1_CH))))))
        case "7":
            return succ(succ(succ(succ(succ(succ(succ(digit1_CH)))))))
        case "8":
            return succ(succ(succ(succ(succ(succ(succ(succ(digit1_CH))))))))
        case "9":
            return succ(succ(succ(succ(succ(succ(succ(succ(succ(digit1_CH)))))))))

def number_plus_digit(number_ST, digit_CH):
    "Adds a natural number and a digit."
    if (len(number_ST) == 1):
        return digit_plus_digit(number_ST, digit_CH)
    else:
        last_CH = digit_plus_digit(number_ST[-1], digit_CH)
        if (len(last_CH) > 1):
            bulk = number_ST[0:-1]
            new_bulk = digit_plus_digit(bulk, last_CH[0:1])
            last_CH = last_CH[1:2]
            return new_bulk + last_CH
        elif (len(last_CH) == 1):
            return number_ST[0:-1] + last_CH

def number_plus_number(number1_ST, number2_ST):
    "Adds two natural numbers."
    if (len(number2_ST) > len(number1_ST)):
        return number_plus_number(number2_ST, number1_ST)
    elif (len(number2_ST) == 1):
        return number_plus_digit(number1_ST, number2_ST)
    elif (len(number2_ST) == 0):
        return number1_ST
    elif (len(number2_ST) == 1):
        return number_plus_digit(number1_ST, number2_ST)
    elif (len(number2_ST) > 1):
        number2_last_CH = number2_ST[-1]
        new_number1_ST = number_plus_digit(number1_ST, number2_last_CH)
        last_CH = new_number1_ST[-1]          # return
        bulk1_ST = new_number1_ST[0:-1]
        bulk2_ST = number2_ST[0:-1]
        new_bulk_ST = number_plus_number(bulk1_ST, bulk2_ST)
        return new_bulk_ST + last_CH
        

def digit_times_digit(digit1_CH, digit2_CH):
    "Multiplies two digits."
    accum_ST = "0"
    while not (digit1_CH == "0"):
        DEBUG(126, debug_1, f"digit1_CH = {digit1_CH}")
        DEBUG(127, debug_1, f"accum_ST = {accum_ST}")
        accum_ST = number_plus_digit(accum_ST, digit2_CH)
        digit1_CH = pred(digit1_CH)
    return accum_ST

def DEBUG(line_NT, flag_BL, msg_ST):
    "For debugging: line_NT should be the line number. msg_ST might typically have the form \
     f'variablename = {variablename}'. flag_BL might typically be fed a Boolean parameter debug_# \
     which would be set to True when debugging operation number # is going on. (Different debugging operations \
     could target/focus_on different parts of the code."
    if flag_BL:
        print(f"L{line_NT}. " + msg_ST)

def number_times_digit(number_ST, digit_CH):
    "Product of a natural number times a digit."
    if (len(number_ST) == 1):
        return digit_times_digit(number_ST, digit_CH)
    else:
        bulk_ST = number_ST[0:-1]
        last_CH = number_ST[-1]
        prod_ST = digit_times_digit(digit_CH, last_CH)
        new_last_CH = prod_ST[-1]     # return
        carry_CH = prod_ST[0:-1]
        if (carry_CH == ""):
            carry_CH = "0"
        new_bulk_ST = number_plus_digit(number_times_digit(bulk_ST, digit_CH), carry_CH)
        return new_bulk_ST + new_last_CH

def number_times_number(number1_ST, number2_ST):
    "Product of two natural numbers."
    if (len(number2_ST) == 1):
        return number_times_digit(number1_ST, number2_ST)
    elif (len(number1_ST) == 1):
        return number_times_digit(number2_ST, number1_ST)
    else:
        accum_ST = "0"
        for i in range(len(number2_ST)):
            DEBUG(167, debug_2, f"i = {i}")
            digit_CH = number2_ST[-(i + 1)]
            DEBUG(169, debug_2, f"digit_CH = {digit_CH}")
            zeroes_ST = "0"*i
            DEBUG(171, debug_2, f"zeroes_ST = {zeroes_ST}")
            shift_ST = number_times_digit(number1_ST, digit_CH)
            DEBUG(173, debug_2, f"shift_ST = {shift_ST}")
            addend_ST = shift_ST + zeroes_ST
            DEBUG(175, debug_2, f"addend_ST = {addend_ST}")
            accum_ST = number_plus_number(accum_ST, addend_ST)
            DEBUG(177, debug_2, f"accum_ST = {accum_ST}")
        return accum_ST

def digit_versus_digit(digit1_CH, digit2_CH):
    "Compares two digits."
    if (digit1_CH == digit2_CH):
        return "="
    elif (digit1_CH == "0"):
        return "<"
    elif (digit2_CH == "0"):
        return ">"
    else:
        return digit_versus_digit(pred(digit1_CH), pred(digit2_CH))

def number_versus_number(number1_ST, number2_ST):
    "Compares two natural numbers."
    number1_ST = simplify(number1_ST)
    number2_ST = simplify(number2_ST)
    if (len(number1_ST) > len(number2_ST)):
        return ">"
    elif (len(number1_ST) < len(number2_ST)):
        return "<"
    elif (len(number1_ST) == 1) and (len(number2_ST) == 1):
        return digit_versus_digit(number1_ST, number2_ST)
    elif (number1_ST[0] == number2_ST[0]):
        return number_versus_number(number1_ST[1:], number2_ST[1:])
    else:
        return digit_versus_digit(number1_ST[0], number2_ST[0])

