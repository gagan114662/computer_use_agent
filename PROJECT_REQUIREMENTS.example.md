# Example Project: Simple Calculator

## Project Name
Simple Calculator

## Overview
A Python calculator that performs basic arithmetic operations with proper error handling.

## Requirements

### Functional Requirements

#### Requirement 1: Addition
- **Description**: Add two numbers together
- **Input**: Two numbers (int or float)
- **Output**: Sum of the two numbers
- **Example**:
  ```
  Input: 5, 3
  Output: 8
  ```

#### Requirement 2: Subtraction
- **Description**: Subtract second number from first
- **Input**: Two numbers (int or float)
- **Output**: Difference of the two numbers
- **Example**:
  ```
  Input: 10, 4
  Output: 6
  ```

#### Requirement 3: Multiplication
- **Description**: Multiply two numbers
- **Input**: Two numbers (int or float)
- **Output**: Product of the two numbers
- **Example**:
  ```
  Input: 6, 7
  Output: 42
  ```

#### Requirement 4: Division
- **Description**: Divide first number by second
- **Input**: Two numbers (int or float)
- **Output**: Quotient of the two numbers
- **Example**:
  ```
  Input: 20, 4
  Output: 5.0
  ```
- **Error Handling**: Raise `ZeroDivisionError` when dividing by zero

### Non-Functional Requirements
- **Error Handling**: Properly handle division by zero
- **Type Support**: Support both integers and floats
- **Code Quality**: Follow PEP 8 standards

## Technical Specifications

### Project Structure
```
src/
  └── calculator.py
tests/
  └── test_calculator.py
```

### Dependencies
- pytest (for testing)

### API/Interface Design

#### Function 1: `add(a, b)`
- **Purpose**: Add two numbers
- **Parameters**:
  - `a` (int/float): First number
  - `b` (int/float): Second number
- **Returns**: (int/float) Sum of a and b

#### Function 2: `subtract(a, b)`
- **Purpose**: Subtract b from a
- **Parameters**:
  - `a` (int/float): First number
  - `b` (int/float): Second number
- **Returns**: (int/float) Difference a - b

#### Function 3: `multiply(a, b)`
- **Purpose**: Multiply two numbers
- **Parameters**:
  - `a` (int/float): First number
  - `b` (int/float): Second number
- **Returns**: (int/float) Product of a and b

#### Function 4: `divide(a, b)`
- **Purpose**: Divide a by b
- **Parameters**:
  - `a` (int/float): Numerator
  - `b` (int/float): Denominator
- **Returns**: (float) Quotient a / b
- **Raises**: `ZeroDivisionError` if b is 0

## Test Cases

### Test Case 1: Basic Addition
- **Input**: 5, 3
- **Expected Output**: 8
- **Edge Cases**: negative numbers, floats, zero

### Test Case 2: Basic Subtraction
- **Input**: 10, 4
- **Expected Output**: 6
- **Edge Cases**: negative results, floats

### Test Case 3: Basic Multiplication
- **Input**: 6, 7
- **Expected Output**: 42
- **Edge Cases**: multiplication by zero, negative numbers

### Test Case 4: Basic Division
- **Input**: 20, 4
- **Expected Output**: 5.0
- **Edge Cases**: division by zero (should raise error)

### Test Case 5: Division by Zero
- **Input**: 10, 0
- **Expected Output**: Raises `ZeroDivisionError`

## Success Criteria

The project is complete when:
- [x] All four operations are implemented
- [x] All test cases pass
- [x] Division by zero raises proper exception
- [x] Code coverage > 80%
- [x] Clean, readable code

## Example Usage

```python
from src.calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)
print(result)  # Expected: 8

# Subtraction
result = subtract(10, 4)
print(result)  # Expected: 6

# Multiplication
result = multiply(6, 7)
print(result)  # Expected: 42

# Division
result = divide(20, 4)
print(result)  # Expected: 5.0

# Division by zero
try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
