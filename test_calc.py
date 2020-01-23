from calc import get_expression, parse_args, evaluate_expression

def test_parses_arguments_simple():
  expr = "2 2"
  arg1, arg2 = parse_args(expr)
  assert (arg1, arg2) == ("2", "2")

def test_gets_first_argument():
  expr = "(add 2 (multiply 4 5)) 43"
  assert get_expression(expr) == "(add 2 (multiply 4 5))"

def test_gets_first_argument_complex():
  expr = "(add 2 (multiply 4 5)) (multiply 9 (add 4 5))"
  assert get_expression(expr) == "(add 2 (multiply 4 5))"

def test_returns_expression_unmodified():
  expr = "(add 2 (multiply 4 5))"
  assert get_expression(expr) == "(add 2 (multiply 4 5))"

def test_returns_single_simple():
  expr = "8989"
  assert get_expression(expr) == "8989"

def test_returns_single_value_argument():
  expr = "8989 (add 2 (multiply 4 5))"
  assert get_expression(expr) == "8989"

def test_parses_arguments_complex():
  expected_arg1 = "(add 2 (multiply 4 5))"
  expected_arg2 = "(multiply 9 (add 4 5))"

  expr = "{} {}".format(expected_arg1, expected_arg2)
  arg1, arg2 = parse_args(expr)

  assert (arg1, arg2) == (expected_arg1, expected_arg2)

def test_evaluates_single_value():
  expr = "123"
  assert evaluate_expression(expr) == 123

def test_evaluates_simple_expression():
  expr = "(add 2 4)"
  assert evaluate_expression(expr) == 6

def test_evaluates_nested_expression():
  expr = "(add 1 (multiply (add 2 1) 3))"
  assert evaluate_expression(expr) == 10
    
def test_evaluates_complex_expression():
  expr = "(multiply 3 (multiply (multiply 3 3) 3))"
  assert evaluate_expression(expr) == 81

def test_evaluates_complex2_expression():
  expr = "(multiply (add 5 5) (add 5 5))"
  assert evaluate_expression(expr) == 100

def test_evaluates_exponentation():
  expr = "(exponent 2 (add 2 3))"
  assert evaluate_expression(expr) == 32