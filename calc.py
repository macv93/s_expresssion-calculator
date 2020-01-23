#!/usr/bin/python

'''
    File name: calc.py
    Author: Manuel Canarte
    Date created: 1/17/2020
    Date last modified: 1/21/2020
    Python Version: 2.7
'''

from sys import argv

def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

def exponent(a, b):
  return a ** b

##############################################################
# def get_operation(op_string):
# compares and returns the corresponding operation function based on the op_string
# inputs: op_string, operation string
# returns: the actual function that performs the corresponding operation 

def get_operation(op_string):
  if op_string == 'add':
    return add
  elif op_string == 'multiply':
    return multiply
  elif op_string == 'exponent':
    return exponent

##############################################################
# get_expression(arg_string)
# gets the first valid expression in a string of space delimited expressions
# inputs: arg_string, passed through command line arguments
# returns: a string expression

def get_expression(arg_string):

  open_bracket_count = 0
  closed_bracket_count = 0

  if arg_string[0].isdigit():
    first_space_idx = arg_string.find(" ")

    # space found, find() returns -1 if not found - return first half up to space
    if first_space_idx > 0:
      return arg_string[:first_space_idx]
    
    return arg_string

  # if it's not a digit, then it's an expression

  #full expression check by balanced brackets
  for idx, val in enumerate(arg_string):
    if val == "(":
      open_bracket_count += 1

    elif val == ")":
      closed_bracket_count += 1

    
    if open_bracket_count == closed_bracket_count:
      #index of closing bracket + space
      return arg_string[:idx + 1]


##############################################################
# def parse_args(arg_string):
# splits the LHS and RHS based on space delimiter 
# inputs: arg_string, string of operands
# returns: LHS and RHS expressions/operands

def parse_args(arg_string):
  arg1 = get_expression(arg_string)
  arg2 = arg_string.replace(arg1, " ", 1).strip()
  
  return arg1, arg2

##############################################################
# def parse_expression(expression_string):
# removes brackets from expression and parses through op_str and calls parse_args(arg_string) to parse LHS and RHS
# inputs: expression_string, passed from CLI
# returns: operation string, left and right operands

def parse_expression(expression_string):
  without_brackets = ''.join(expression_string.rsplit(')', 1)).replace("(", "", 1)
  space_idx = without_brackets.find(" ")

  op_str = without_brackets[0:space_idx]
  
  arg_string = without_brackets[space_idx+1:]
  arg1, arg2 = parse_args(arg_string)

  return op_str, arg1, arg2

##############################################################
# def evaluate_expression(expr_str):
# 'implicit' recursive binary expression tree - if either argument is an expression, 
# decomposition is required until result of LHS and RHS can be returned 
# inputs: exptr_str passed through CLI
# returns: 'base case' int(expr_str) - operation + LHS + RHS -  operation + expression + RHS - operation + LHS + expression - operation + expression + expression

def evaluate_expression(expr_str):

  # base case - single value
  if expr_str.isdigit():
    return int(expr_str)
  else:
    op_string, arg1, arg2 = parse_expression(expr_str)

    operation = get_operation(op_string)

    if arg1.isdigit() and arg2.isdigit():
      arg1_int = int(arg1)
      arg2_int = int(arg2)

      return operation(arg1_int, arg2_int)

    if not arg1.isdigit() and arg2.isdigit():
      return operation(evaluate_expression(arg1), int(arg2))

    if arg1.isdigit() and not arg2.isdigit():
      return operation(int(arg1), evaluate_expression(arg2))

    else:
      return operation(evaluate_expression(arg1), evaluate_expression(arg2))

def main():
  expression = argv[1]
  result = evaluate_expression(expression)
  print(result)

if __name__ == "__main__":
    main()
