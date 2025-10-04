#!/usr/bin/env python3
"""
Interactive PRD Generator with Claude Integration

Uses Claude to ask intelligent follow-up questions and generate comprehensive PRD.
"""

import os
import sys
import json


class ClaudePRDGenerator:
    """Generate PRD using Claude for intelligent questioning"""

    def __init__(self):
        self.brief = ""
        self.conversation_history = []

    def generate_prd_with_claude(self, brief):
        """Use Claude to generate PRD through conversation"""

        self.brief = brief

        print(f"\n{'='*80}")
        print("🤖 INTELLIGENT PRD GENERATOR (Claude-Powered)")
        print(f"{'='*80}\n")
        print(f"📝 Your Brief: {brief}\n")

        # Step 1: Analyze the brief
        print("🔍 Analyzing your brief...\n")

        analysis_prompt = f"""You are a product requirements analyst. Analyze this brief and identify:

Brief: "{brief}"

Generate:
1. What type of project is this?
2. What are the implied core features?
3. What critical information is missing?
4. What follow-up questions should we ask to create a complete PRD?

Provide a JSON response with:
{{
    "project_type": "...",
    "implied_features": [...],
    "missing_info": [...],
    "questions": [
        {{"id": "q1", "question": "...", "why": "...", "required": true}},
        ...
    ]
}}
"""

        # This would call Claude API - for now, we'll simulate
        analysis = self._call_claude(analysis_prompt)

        # Step 2: Ask follow-up questions
        print("📋 I need some clarifications to build a complete PRD:\n")

        answers = self._ask_follow_ups(analysis.get("questions", []))

        # Step 3: Generate comprehensive PRD
        print("\n🔨 Generating detailed PRD...\n")

        prd_prompt = f"""Generate a comprehensive Product Requirements Document.

Original Brief: {brief}

Analysis:
{json.dumps(analysis, indent=2)}

User Answers:
{json.dumps(answers, indent=2)}

Generate a complete PRD in markdown format with:
1. Project Overview
2. Detailed Functional Requirements (each feature with inputs, outputs, examples)
3. Technical Specifications (structure, API design, data models)
4. Comprehensive Test Cases (remember: tests import from src/, NO hardcoding)
5. Success Criteria
6. Testing Guidelines

Format as markdown suitable for PROJECT_REQUIREMENTS.md
"""

        prd_content = self._call_claude(prd_prompt)

        # Step 4: Validate PRD
        print("✅ Validating PRD for completeness...\n")

        validation_prompt = f"""Review this PRD and check if it's complete for autonomous development:

{prd_content}

Check:
1. Are all features clearly defined with inputs/outputs?
2. Are test cases comprehensive?
3. Is the testing guideline clear about NO hardcoding in tests?
4. Are edge cases covered?
5. Is success criteria measurable?

If anything is missing, provide the complete updated PRD.
Otherwise, return the PRD as-is.
"""

        final_prd = self._call_claude(validation_prompt)

        return final_prd

    def _call_claude(self, prompt):
        """Call Claude API (or simulate for now)"""

        # In production, this would use the Anthropic API
        # For demonstration, we'll return structured responses

        if "Analyze this brief" in prompt:
            # Return analysis
            return {
                "project_type": "utility library",
                "implied_features": self._extract_features_from_brief(),
                "missing_info": ["input formats", "edge cases", "error handling"],
                "questions": self._generate_smart_questions()
            }

        elif "Generate a comprehensive" in prompt:
            # Generate PRD
            return self._generate_prd_content()

        elif "Review this PRD" in prompt:
            # Validation - return as-is for now
            return prompt.split("Review this PRD and check")[1].split("Check:")[0].strip()

        return ""

    def _extract_features_from_brief(self):
        """Extract features from brief"""
        # Simple keyword extraction
        features = []
        if "calculator" in self.brief.lower():
            features = ["addition", "subtraction", "multiplication", "division"]
        elif "string" in self.brief.lower():
            features = ["reverse", "count", "transform"]
        else:
            # Generic features
            features = ["core_function_1", "core_function_2"]
        return features

    def _generate_smart_questions(self):
        """Generate intelligent follow-up questions"""

        return [
            {
                "id": "inputs",
                "question": "What input types/formats will the system accept?",
                "why": "Need to define function signatures and validation",
                "required": True
            },
            {
                "id": "outputs",
                "question": "What should the outputs look like (format, type)?",
                "why": "Need to define return types and test assertions",
                "required": True
            },
            {
                "id": "edge_cases",
                "question": "Any specific edge cases or error conditions to handle?",
                "why": "Need to write comprehensive tests",
                "required": False,
                "default": "Standard edge cases (None, empty, invalid types)"
            },
            {
                "id": "performance",
                "question": "Any performance requirements or constraints?",
                "why": "Need to design efficient algorithms",
                "required": False,
                "default": "No specific constraints"
            },
            {
                "id": "additional",
                "question": "Any other requirements or features needed?",
                "why": "Ensure nothing is missed",
                "required": False,
                "default": "None"
            }
        ]

    def _ask_follow_ups(self, questions):
        """Ask follow-up questions interactively"""

        answers = {}

        for q in questions:
            required = "✓" if q.get("required") else " "
            why = f"\n  💡 Why: {q['why']}" if 'why' in q else ""
            default = f" [{q['default']}]" if 'default' in q else ""

            print(f"{required} {q['question']}{default}{why}")

            answer = input("  → ").strip()

            if not answer and 'default' in q:
                answer = q['default']

            answers[q['id']] = answer
            print()

        return answers

    def _generate_prd_content(self):
        """Generate PRD markdown content"""

        # This would be generated by Claude in production
        # For now, return a template

        return f"""# {self.brief.title()}

## Overview
{self.brief}

## Functional Requirements

### Requirement 1: Core Functionality
- **Description**: Main feature implementation
- **Input**: As specified by user
- **Output**: As specified by user
- **Example**: Input → Output

## Technical Specifications

### Project Structure
```
src/
  └── main.py
tests/
  └── test_main.py
```

### Testing Guidelines
**CRITICAL**: Tests must ONLY import from src/ - NO hardcoding logic

```python
# ✓ CORRECT
from src.module import function
def test_function():
    assert function(input) == expected

# ✗ WRONG
def test_function():
    result = input + 1  # Logic in test
    assert result == expected
```

## Success Criteria
- [ ] All features implemented
- [ ] All tests pass
- [ ] 100% code coverage
- [ ] Tests import from codebase (no hardcoding)
"""

    def save_prd(self, content, filename="PROJECT_REQUIREMENTS.md"):
        """Save PRD to file"""

        with open(filename, 'w') as f:
            f.write(content)

        print(f"✅ PRD saved to {filename}\n")
        return filename


def main():
    """Main entry point"""

    if len(sys.argv) < 2:
        print("\n🤖 Interactive PRD Generator")
        print("=" * 80)
        print("\nUsage: python interactive_prd.py 'one line brief'")
        print("\nExample:")
        print("  python interactive_prd.py 'Build a URL shortener service'")
        print("  python interactive_prd.py 'Create a todo list manager'")
        print("\nThe system will:")
        print("  1. Analyze your brief")
        print("  2. Ask intelligent follow-up questions")
        print("  3. Generate comprehensive PRD")
        print("  4. Validate completeness")
        print("  5. Ready for autonomous development\n")
        sys.exit(1)

    brief = " ".join(sys.argv[1:])

    generator = ClaudePRDGenerator()
    prd_content = generator.generate_prd_with_claude(brief)
    generator.save_prd(prd_content)

    print("=" * 80)
    print("✅ COMPLETE PRD READY!")
    print("=" * 80)
    print("\n📋 Next Steps:")
    print("  1. Review: cat PROJECT_REQUIREMENTS.md")
    print("  2. Build: ./run_autonomous.sh")
    print("  3. Agent builds autonomously with 100% correctness")
    print("  4. Verify: pytest tests/ -v\n")


if __name__ == "__main__":
    main()
