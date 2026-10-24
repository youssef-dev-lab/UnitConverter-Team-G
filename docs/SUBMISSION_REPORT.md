# Software Engineering Assignment 2 — Submission Audit

Audit date: 2026-10-24 (Africa/Casablanca)

## Brief and checklist

The assignment brief/rubric was not present anywhere in the repository at audit time. The checklist below records the technical work requested in the task prompt; compare it with the instructor's actual brief before submission.

- [x] Python length conversion: m, km, mi, ft.
- [x] Python temperature conversion: C, F, K; invalid values and below-absolute-zero input rejected.
- [x] Python weight conversion: kg, g, lb.
- [x] Shared validation for non-numeric values, booleans, NaN/infinity, and non-finite results.
- [x] Responsive interactive website with three categories, selectors, swap, result, and error feedback.
- [x] README, dependency declaration, ignore rules, and project layout reviewed.
- [x] GitHub Actions workflow reviewed; PR and post-merge tests passed.
- [x] Existing collaboration evidence reviewed without fabricating contributions, reviews, or approvals.
- [ ] Instructor brief/rubric compliance: needs the assignment document.
- [x] Live updated app: the Pages URL loaded the deployed converter. The three category tabs changed unit selectors/results; swap and empty-input error behavior were verified in-browser.
- [ ] Screenshot evidence: no screenshot files were available in the repository or checkout. Save genuine screenshots only if the instructor's rubric requests them.

## Changes

- `converter.py`: consistent numeric/finite validation across conversions, plus absolute-zero and overflow-result checks.
- `tests/test_length_temperature.py`: added invalid input and absolute-zero cases.
- `index.html`: responsive client-side converter. Remote repository history confirmed this root-level file is the Pages entry point; the legacy files in `docs/` are empty.
- `README.md`: documented app behavior, setup, project layout, and deployment.
- `docs/SUBMISSION_REPORT.md`: audit checklist and evidence.

## Verification and repository evidence

- Local: `.venv/bin/python -m pytest -v` — 30 passed (Python 3.14.7).
- Inline JavaScript: parsed successfully with `node --check` (Node.js 22.20.0).
- `git diff --check` passed.
- GitHub Actions PR run `40131441946` passed; post-merge `main` run `40131485620` passed for commit `7dd38af`.
- GitHub Pages post-merge deployment run `40131485628` completed successfully for `main` commit `7dd38af`; the deployed UI was then loaded and interactively verified.
- Repository: https://github.com/youssef-dev-lab/UnitConverter-Team-G
- Pages: https://youssef-dev-lab.github.io/UnitConverter-Team-G/
- PR #8, [feat: finish Assignment 2 unit converter](https://github.com/youssef-dev-lab/UnitConverter-Team-G/pull/8), was squash-merged to `main` as `7dd38af7c5a2e62918c0bfe34b500943ea1bc7d8` after its CI passed.
- Branch protection: GitHub's branch listing marked all listed branches, including `main`, as unprotected. Reading detailed protection settings returned 403 through the connected integration, so no settings were changed.
- Collaboration: history includes a real contribution by Ali El Addouli (`e77ed35`, weight validation) and Ali-authored PRs #2 and #5, both merged. Other reviewed changes are attributed to Youssef. No new collaboration event was fabricated.
- Local Git limitation: `.git` is read-only in this checkout and `git fetch` could not write `.git/FETCH_HEAD`. The code was published and merged through GitHub tools; the local branch itself remains behind remote `main`.
- Screenshots: none supplied or found.

## Before submission

1. Provide the instructor's assignment brief/rubric and compare its exact criteria with this task-prompt checklist.
2. Save genuine screenshots if the instructor requires visual evidence.
