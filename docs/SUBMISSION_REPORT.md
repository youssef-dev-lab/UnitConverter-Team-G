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
- [x] GitHub Actions workflow reviewed; latest remote tests run passed.
- [x] Existing collaboration evidence reviewed without creating false reviews or contributions.
- [ ] Instructor brief/rubric compliance: needs the assignment document.
- [ ] Live updated app: the live URL was opened successfully and currently shows the old informational page; the new app must be deployed and rechecked.
- [ ] Screenshot evidence: no existing screenshots were available in the repository or checkout.

## Changes in this submission

- `converter.py`: consistent numeric/finite validation for all conversions, plus absolute-zero and overflow-result checks.
- `tests/test_length_temperature.py`: added validation and absolute-zero cases.
- `index.html`: replaced the informational page with a responsive client-side converter. The remote `main` history showed this root-level file is the Pages entry point; the existing `docs/` HTML, JS, and CSS files are empty and are not the entry point.
- `README.md`: documented app behavior, setup, project layout, and deployment, and corrected stale status wording.
- `docs/SUBMISSION_REPORT.md`: this checklist and evidence record.

## Verification and external state

- Local test command: `.venv/bin/python -m pytest -v` — 30 passed after modifications (Python 3.14.7).
- Inline web JavaScript parsed successfully with `node --check` (Node.js 22.20.0).
- `git diff --check` passed.
- GitHub Actions: GitHub API reported the latest `Unit Converter Tests` run on `main` (commit `92d4427`) as completed/success on 2026-10-24. This predates the changes in this report.
- GitHub Pages: latest Pages build/deployment run on `main` (commit `92d4427`) completed/success on 2026-10-24. This predates the changes in this report. Browser verification of the live URL confirms it still serves the prior informational page.
- Repository: https://github.com/youssef-dev-lab/UnitConverter-Team-G
- Pages URL: https://youssef-dev-lab.github.io/UnitConverter-Team-G/
- Branch protection: GitHub's public branch listing marked all listed branches, including `main`, as unprotected. Reading the detailed protection endpoint was denied to the connected GitHub integration (403), so no settings were changed.
- Collaboration: history includes a real contribution by Ali El Addouli (`e77ed35`, weight validation) and Ali-authored pull requests #2 and #5, both merged. Other recorded changes are attributed to Youssef. No collaboration event was fabricated.
- Local Git limitation: the checkout's `.git` directory is read-only under the active filesystem permissions, and `git fetch` failed to write `.git/FETCH_HEAD`. The local worktree branch is behind remote `main`. Use the connected GitHub repository tools to publish the reviewed files on a new branch and PR; do not claim local commits in this checkout.
- Screenshots: none supplied or found. Do not claim screenshot evidence exists.

## Before submission

1. Add the assignment brief/rubric and reconcile its exact requirements with this inferred checklist.
2. Review the live Pages URL in a browser after the updated root `index.html` is deployed.
3. Save genuine browser screenshots if the rubric requests them.
4. Ensure the changes are merged to the Pages source branch, then verify the resulting CI, deployment, and live UI.
