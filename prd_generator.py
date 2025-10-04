#!/usr/bin/env python3
"""
Intelligent PRD Generator

Takes a one-line brief, asks clarifying questions, and generates a detailed PRD.
Designed to work autonomously with minimal user input.
"""

import sys
import json
from pathlib import Path


class PRDGenerator:
    """Generate detailed Product Requirements Document from brief"""

    def __init__(self):
        self.brief = ""
        self.answers = {}
        self.prd = {}

    def analyze_brief(self, brief):
        """Analyze the brief and identify what questions to ask"""
        self.brief = brief.strip()

        print(f"\n{'='*80}")
        print("INTELLIGENT PRD GENERATOR")
        print(f"{'='*80}\n")
        print(f"📝 Brief: {self.brief}\n")

        # Determine project type and complexity
        questions = self._generate_questions()

        return questions

    def _generate_questions(self):
        """Generate intelligent questions based on the brief"""

        # Standard questions for any project
        questions = [
            {
                "id": "scope",
                "question": "What are the core features/functions needed? (comma-separated)",
                "required": True,
                "type": "list"
            },
            {
                "id": "inputs",
                "question": "What inputs will the system accept? (describe format/type)",
                "required": True,
                "type": "text"
            },
            {
                "id": "outputs",
                "question": "What outputs should it produce? (describe format)",
                "required": True,
                "type": "text"
            },
            {
                "id": "edge_cases",
                "question": "Any specific edge cases or error conditions to handle? (or 'auto' for standard)",
                "required": False,
                "type": "text",
                "default": "auto"
            },
            {
                "id": "constraints",
                "question": "Any performance/technical constraints? (or 'none')",
                "required": False,
                "type": "text",
                "default": "none"
            }
        ]

        # Add domain-specific questions based on keywords
        brief_lower = self.brief.lower()

        if any(word in brief_lower for word in ['api', 'web', 'http', 'rest']):
            questions.append({
                "id": "api_details",
                "question": "API endpoints needed? (list them or 'auto')",
                "required": False,
                "type": "text",
                "default": "auto"
            })

        if any(word in brief_lower for word in ['database', 'data', 'storage', 'persist']):
            questions.append({
                "id": "data_model",
                "question": "Data structure/schema? (describe or 'auto')",
                "required": False,
                "type": "text",
                "default": "auto"
            })

        if any(word in brief_lower for word in ['ml', 'ai', 'model', 'predict', 'train']):
            questions.append({
                "id": "ml_details",
                "question": "Model type and training data? (describe or 'auto')",
                "required": False,
                "type": "text",
                "default": "auto"
            })

        return questions

    def ask_questions(self, questions):
        """Interactively ask questions to user"""

        print("📋 Please answer the following questions for detailed PRD:\n")

        for q in questions:
            if q["required"]:
                prompt = f"✓ {q['question']}: "
            else:
                default = q.get('default', '')
                prompt = f"  {q['question']} [{default}]: "

            answer = input(prompt).strip()

            if not answer and not q["required"]:
                answer = q.get('default', '')

            if q["type"] == "list":
                self.answers[q["id"]] = [item.strip() for item in answer.split(",")]
            else:
                self.answers[q["id"]] = answer

        print(f"\n{'='*80}\n")

    def generate_prd(self):
        """Generate detailed PRD from brief and answers"""

        # Parse core features
        features = self.answers.get("scope", [])

        # Generate comprehensive PRD structure
        prd = {
            "project_name": self._extract_project_name(),
            "overview": self.brief,
            "functional_requirements": self._generate_functional_requirements(features),
            "technical_specs": self._generate_technical_specs(),
            "test_cases": self._generate_test_cases(features),
            "success_criteria": self._generate_success_criteria(features)
        }

        return prd

    def _extract_project_name(self):
        """Extract project name from brief"""
        # Simple extraction - take first few words
        words = self.brief.split()[:4]
        return " ".join(words).title()

    def _generate_functional_requirements(self, features):
        """Generate functional requirements for each feature"""

        requirements = []

        for i, feature in enumerate(features, 1):
            req = {
                "id": i,
                "name": feature.strip().title(),
                "description": f"Implement {feature.strip()}",
                "inputs": self.answers.get("inputs", ""),
                "outputs": self.answers.get("outputs", ""),
                "example": f"Input: [example] → Output: [expected result]"
            }
            requirements.append(req)

        return requirements

    def _generate_technical_specs(self):
        """Generate technical specifications"""

        specs = {
            "project_structure": {
                "src": "Implementation code",
                "tests": "Test files (imports only, no hardcoding)"
            },
            "dependencies": ["pytest", "pytest-cov"],
            "constraints": self.answers.get("constraints", "none")
        }

        # Add API specs if relevant
        if self.answers.get("api_details"):
            specs["api"] = self.answers["api_details"]

        # Add data model if relevant
        if self.answers.get("data_model"):
            specs["data_model"] = self.answers["data_model"]

        return specs

    def _generate_test_cases(self, features):
        """Generate test case templates"""

        test_cases = []

        for feature in features:
            # Basic test case
            test_cases.append({
                "feature": feature.strip(),
                "test_name": f"test_{feature.lower().replace(' ', '_')}",
                "scenarios": [
                    "Basic functionality",
                    "Edge cases",
                    "Error handling",
                    "Type validation"
                ]
            })

        # Add edge case handling
        edge_cases = self.answers.get("edge_cases", "auto")
        if edge_cases != "auto":
            test_cases.append({
                "feature": "Edge Cases",
                "test_name": "test_edge_cases",
                "scenarios": edge_cases.split(",")
            })

        return test_cases

    def _generate_success_criteria(self, features):
        """Generate success criteria"""

        return [
            f"All {len(features)} features implemented",
            "All tests pass (100%)",
            "Code coverage > 90%",
            "Tests import from codebase (no hardcoding)",
            "Proper error handling",
            "Clean, documented code"
        ]

    def save_prd(self, filename="PROJECT_REQUIREMENTS.md"):
        """Save PRD in markdown format"""

        prd = self.generate_prd()

        content = f"""# {prd['project_name']}

## Overview
{prd['overview']}

## Functional Requirements

"""

        # Add functional requirements
        for req in prd['functional_requirements']:
            content += f"""### Requirement {req['id']}: {req['name']}
- **Description**: {req['description']}
- **Input**: {req['inputs']}
- **Output**: {req['outputs']}
- **Example**: {req['example']}

"""

        # Add technical specifications
        content += f"""## Technical Specifications

### Project Structure
```
{json.dumps(prd['technical_specs']['project_structure'], indent=2)}
```

### Dependencies
{', '.join(prd['technical_specs']['dependencies'])}

### Constraints
{prd['technical_specs'].get('constraints', 'None')}

"""

        # Add test cases
        content += """## Test Cases

"""
        for tc in prd['test_cases']:
            content += f"""### {tc['feature']}
- Test function: `{tc['test_name']}`
- Scenarios to test:
"""
            for scenario in tc['scenarios']:
                content += f"  - {scenario}\n"
            content += "\n"

        # Add success criteria
        content += """## Success Criteria

"""
        for criterion in prd['success_criteria']:
            content += f"- [ ] {criterion}\n"

        # Add testing guidelines
        content += """
## Testing Guidelines

**CRITICAL RULES:**
1. Tests must ONLY import from src/ - NO hardcoding logic
2. Tests are wrappers that verify behavior, not implement it
3. All edge cases must be covered
4. Type validation must be tested
5. Error handling must be verified

Example test structure:
```python
from src.module import function

def test_function():
    result = function(input)  # Import and test
    assert result == expected  # Verify behavior
```

**NOT THIS:**
```python
def test_function():
    result = input + 1  # WRONG: Logic in test
    assert result == expected
```
"""

        # Save to file
        with open(filename, 'w') as f:
            f.write(content)

        print(f"✅ PRD saved to {filename}\n")
        return filename


def main():
    """Main entry point"""

    if len(sys.argv) < 2:
        print("Usage: python prd_generator.py 'one line brief'")
        print("Example: python prd_generator.py 'Build a calculator that adds, subtracts, multiplies, divides'")
        sys.exit(1)

    brief = " ".join(sys.argv[1:])

    generator = PRDGenerator()
    questions = generator.analyze_brief(brief)
    generator.ask_questions(questions)
    generator.save_prd()

    print("📄 PRD Generation Complete!")
    print("\nNext steps:")
    print("1. Review PROJECT_REQUIREMENTS.md")
    print("2. Run: ./run_autonomous.sh")
    print("3. Agent will build the project autonomously")
    print("4. Verify via: pytest tests/ -v\n")


if __name__ == "__main__":
    main()
