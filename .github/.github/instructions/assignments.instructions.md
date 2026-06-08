---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/README.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
-- The assignment must be created as a `README.md` file placed in a folder under `assignments/` (for example: `assignments/python-basics/README.md`).
-- Do not remove or skip required sections from the template. If you add optional sections, mark them clearly as **Optional**.

## 2. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name
   - In the Description, clearly state what the student must do.
   - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
   - Provide example input/output in code blocks if helpful.

Do not include extra sections unless explicitly specified.

## 3. Examples and runnable guidance

- If the assignment provides starter code, reference the starter filename in the `📁 Starter files` section of the template.
- Add a short `▶️ How to run` snippet showing the exact command to run (for example `python3 starter-code.py`).
- If the task requires specific input or sample output, include minimal examples in fenced code blocks under the relevant task.

## 4. Review checklist (before committing)

- Title, Objective, Tasks, Requirements present and follow template icons/labels.
- `README.md` exists at the assignment folder root.
- Starter files referenced and present in the folder.
- Run instructions included and tested locally when possible.
- Keep language student-friendly and concise.

Use `templates/assignment-template.md` as the single source of truth for structure.