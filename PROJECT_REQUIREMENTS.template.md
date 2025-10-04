# Project Requirements Template

Copy this template to `PROJECT_REQUIREMENTS.md` and fill in your project details. The autonomous agent will read this and implement everything.

---

## Project Name
[Your project name]

## Overview
[Brief description of what this project does]

## Requirements

### Functional Requirements

#### Requirement 1: [Feature Name]
- **Description**: [What should it do?]
- **Input**: [What inputs does it take?]
- **Output**: [What should it return?]
- **Example**:
  ```
  Input: [example]
  Output: [example]
  ```

#### Requirement 2: [Feature Name]
- **Description**: [What should it do?]
- **Input**: [What inputs does it take?]
- **Output**: [What should it return?]
- **Example**:
  ```
  Input: [example]
  Output: [example]
  ```

### Non-Functional Requirements
- **Performance**: [e.g., "should handle 1000 requests/second"]
- **Error Handling**: [e.g., "should raise ValueError for invalid input"]
- **Code Quality**: [e.g., "follow PEP 8 standards"]

## Technical Specifications

### Project Structure
```
src/
  ├── [module_name].py
  └── ...
tests/
  ├── test_[module_name].py
  └── ...
```

### Dependencies
- [List any required libraries]

### API/Interface Design

#### Function 1: `function_name(param1, param2)`
- **Purpose**: [What it does]
- **Parameters**:
  - `param1` (type): [description]
  - `param2` (type): [description]
- **Returns**: [return type and description]
- **Raises**: [any exceptions]

#### Function 2: `another_function(param)`
- **Purpose**: [What it does]
- **Parameters**:
  - `param` (type): [description]
- **Returns**: [return type and description]

## Test Cases

### Test Case 1: [Scenario]
- **Input**: [specific input]
- **Expected Output**: [specific output]
- **Edge Cases**: [list edge cases to test]

### Test Case 2: [Scenario]
- **Input**: [specific input]
- **Expected Output**: [specific output]
- **Edge Cases**: [list edge cases to test]

## Success Criteria

The project is complete when:
- [ ] All functional requirements are implemented
- [ ] All test cases pass
- [ ] Code coverage > 80%
- [ ] No linting errors
- [ ] Documentation is complete

## Example Usage

```python
from src.module_name import function_name

# Example 1
result = function_name(input1, input2)
print(result)  # Expected: [output]

# Example 2
result = another_function(input)
print(result)  # Expected: [output]
```

---

## Notes for Autonomous Agent

- Implement tests FIRST (in tests/ folder)
- Tests should ONLY import from src/ and verify behavior
- DO NOT hardcode logic in test files
- Debug and fix issues automatically
- Iterate until all tests pass
