Implement a UI user story end-to-end by orchestrating three agents in sequence: UX design → coding → UI verification.

## User Story

$ARGUMENTS

## Pipeline

Execute the three phases below in strict order. Do not begin the next phase until the previous one is complete.

---

### Phase 1 — UX Design (ux-design-planner agent)

Invoke the `ux-design-planner` agent with the user story above.

The agent will produce:
- Written UI layout
- Component list
- Interaction flow
- Coding checklist (ending with "Ready for coding.")

Wait for the agent to return its full design spec before continuing.

---

### Phase 2 — Implementation (coding)

Using the coding checklist from Phase 1 as your implementation guide:

1. Implement all template, route, model, and style changes required by the spec.
2. Add unit tests for every new behaviour (`tests/test_app.py`).
3. Run the full test suite (`python -m unittest discover -s tests`) and confirm all tests pass before continuing.

Do not proceed to Phase 3 until tests are green.

---

### Phase 3 — UI Verification (playwright-feature-verifier agent)

Invoke the `playwright-feature-verifier` agent to visually verify the implemented feature.

The agent will:
1. Ensure the Flask app is running at `http://127.0.0.1:5000`.
2. Navigate to every URL affected by the feature.
3. Interact with the feature (click, type, submit as appropriate).
4. Take a full-page screenshot of the working feature.
5. Save the screenshot to `test-output/` using the naming convention `feature-name-verification-YYYY-MM-DD.png`.
6. Report a ✅/❌ status for each verification step.

---

## Completion Criteria

The command is complete when all of the following are true:
- [ ] Phase 1 design spec produced and ends with "Ready for coding."
- [ ] All code changes implemented per the checklist
- [ ] All unit tests pass
- [ ] Screenshot saved to `test-output/` confirming the feature works visually
