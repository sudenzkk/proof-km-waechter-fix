# KM-Wächter | AI-Assisted Python Code Modernization

### IBM SkillsBuild Bobathon 2026 · ProoV Guided Project

A hands-on software engineering project focused on debugging,
modernizing, testing, and analyzing a legacy Python-based
vehicle maintenance monitoring system.

**Project Status:** Completed  
**Acceptance Checks:** 11/11 Passed  
**Technologies:** Python, Pandas, Git, GitHub, VS Code, AI-Assisted Development

## Project Overview

KM-Wächter is a fictional fleet maintenance monitoring system
developed as part of the IBM Bobathon 2026 challenge,
"The Legacy Fix", delivered through ProoV.

The application monitors a fictional fleet of 6,000 vehicles
and determines when maintenance warnings should be issued.

The original codebase contained calculation errors,
missing-data handling problems, insufficient regression tests,
and an incomplete data analysis component.

The objective was to identify and resolve these issues
while preserving the existing maintenance rules.

## The Problem

The original application used integer floor division
to calculate vehicle maintenance wear:

```python
ratio = km_since_service // interval
return ratio * 100
```

This caused incorrect results for vehicles approaching
their maintenance interval.

For example:

- Maintenance interval: 15,000 km
- Distance since last service: 14,900 km
- Incorrect result: 0%
- Correct result: approximately 99.33%

Because the warning threshold was set to 80%,
affected vehicles were not flagged when they should have been.

The defect could silently prevent maintenance warnings
from being generated.

## Implemented Improvements

### 1. Corrected Maintenance Calculations

Replaced floor division with accurate division to
calculate maintenance wear percentages.

Preserved the original business requirements:

- Maintenance interval: 15,000 km
- Warning threshold: 80%

### 2. Improved Missing-Data Handling

Updated maintenance checks to handle missing
last-service readings without incorrectly treating
them as zero.

Improved fleet reporting to prevent crashes
caused by missing maintenance data.

### 3. Fixed Reporting and Utility Calculations

- Corrected average maintenance wear calculations.
- Fixed kilometres-to-miles conversion.
- Improved reliability of the nightly fleet report.

### 4. Expanded Regression Testing

Added regression tests covering:

- Vehicles approaching their maintenance interval.
- Accurate fractional wear calculations.
- Missing maintenance readings.
- Fleet report behavior and edge cases.

### 5. Conducted Breakdown-Risk Data Analysis

Used Python and Pandas to analyze a dataset of
120 vehicles, including 26 recorded breakdowns.

Compared vehicle characteristics between vehicles
with and without recorded breakdowns.

The analysis found larger differences in:

- Kilometres since last service.
- Average daily driving distance.
- Vehicle load factor.

Total odometer readings and vehicle age showed
relatively small differences between the groups.

These findings represent descriptive associations
within the provided dataset, not evidence of causation
or a validated predictive model.

## Testing and Verification

The project includes automated tests and an
independent acceptance verification script.

Run the acceptance checks with:

```bash
python verify.py
```

**Final verification result:**

```text
KM-Waechter acceptance check
============================
11 of 11 checks pass.
Done. Push it and hand in the link.
```

The successful checks confirm that the identified
maintenance defects were corrected, the required
business rules were preserved, the missing regression
test was added, and the data analysis was completed.

## AI-Assisted Development Workflow

This project was completed using an AI-assisted
development workflow.

My responsibilities included:

1. Examining the legacy codebase and identifying defects.
2. Defining specific tasks and acceptance criteria.
3. Directing an AI coding agent to implement targeted changes.
4. Reviewing generated code for correctness.
5. Identifying unintended modifications.
6. Validating changes through tests and acceptance checks.
7. Documenting the technical decisions and findings.

During the guided code-review exercise, I identified
an incorrect use of floor division, an unauthorized
change to the maintenance warning threshold,
and missing regression test coverage.

This experience reinforced the importance of
reviewing AI-generated code rather than accepting
changes without verification.

## Repository Structure

| File | Purpose |
|------|---------|
| `km_wachter.py` | Core maintenance calculations |
| `fleet_report.py` | Fleet reporting functionality |
| `fleet_utils.py` | Utility functions and unit conversions |
| `config_loader.py` | Configuration handling |
| `settings.cfg` | Maintenance configuration |
| `test_km_wachter.py` | Maintenance regression tests |
| `test_fleet_report.py` | Fleet reporting tests |
| `analyze.py` | Breakdown-risk data analysis |
| `fleet_history.csv` | Dataset containing 120 vehicles |
| `verify.py` | Acceptance verification script |
| `NOTES.md` | Review observations and project reflections |
| `TASK.md` | Original project requirements |

## Getting Started

Clone the repository:

```bash
git clone https://github.com/sudenzkk/proof-km-waechter-fix.git
cd proof-km-waechter-fix
```

Install the required dependencies:

```bash
python -m pip install pytest pandas
```

Run the tests:

```bash
python -m pytest
```

Run the acceptance verification:

```bash
python verify.py
```

Run the data analysis:

```bash
python analyze.py
```

## Certification

**IBM SkillsBuild — IBM Bobathon: The Legacy Fix**

[View IBM SkillsBuild Completion Certificate](https://skills.yourlearning.ibm.com/certificate/share/ac3ce9b670ewogICJvYmplY3RJZCIgOiAiVVJMLTM4Q0FFRTZENjZFMiIsCiAgIm9iamVjdFR5cGUiIDogIkFDVElWSVRZIiwKICAibGVhcm5lckNOVU0iIDogIjkyNzM1OThSRUciCn08970d726ea-10)

## Project Context

This repository was created as part of
**The Legacy Fix**, a ProoV Guided Project
powered by IBM Bob.

The fictional company Vossberg Mobility and
the KM-Wächter application were created for
educational purposes.

The project demonstrates practical experience
in Python debugging, regression testing,
data analysis, GitHub workflows, and
AI-assisted software development.

**Original challenge:**
[The Legacy Fix — ProoV](https://projectstudy.in/explore/experience-legacy-fix)
