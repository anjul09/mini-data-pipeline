# Project

Lightweight Python data pipeline for validating and processing event records.

No external dependencies beyond pytest. Keep it simple.

## Key Files
- `src/validator.py` — handles record validation rules
- `src/processor.py` — core transformation logic
- `src/main.py` — entrypoint for manual runs
- `tests/` — unit tests


## Conventions
- Keep validation and processing strictly separate
- `processor.py` should assume validation is handled via `validator.py`
- Functions should be small and composable (no large monolithic logic)
- Prefer explicit logic over clever shortcuts


## Workflow
- Run tests after making changes: `pytest`
- Prefer running a single test file while iterating
- Do not assume behavior — verify with tests
- Run `ruff check .` before finalizing changes


## Do Not
- Do not add new dependencies without asking
- Do not mix validation logic into processing
- Do not introduce global state
- Do not silently drop invalid data without making that behavior explicit


## Tests
- Add tests for any new logic or edge cases
- Keep tests simple and readable
- Focus on behavior, not implementation details