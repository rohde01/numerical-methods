# Numerical Methods

University of Copenhagen · BSc Computer Science and Economics · Autumn 2023, block 1 · 7.5 ECTS  
Course code NDAB22009U · [Course description](https://kurser.ku.dk/course/ndab22009u)

Numerical methods for scientific computing, covering linear systems, eigenvalue estimation, interpolation, nonlinear equations and optimisation. The repo has my hand-ins as LaTeX source and my Python solutions to the CodeJudge tasks.

## Contents

| Folder | Contents |
| --- | --- |
| `assignments/aflevering-<n>/` | Tasks 1–6. Report in `sample-authordraft.tex` and `.pdf`, code in one folder per CodeJudge task |
| `assignments/aflevering-1/draft/` | An earlier version of task 1. `task1carl-emilrohde.pdf` has no source |
| `assignments/aflevering-4t/` | A draft of task 2 |
| `materials/` | Course-provided material. gitignored |

## Topics

- Gershgorin discs and eigenvalues
- The Hungarian algorithm

## Tools

Python, LaTeX

## Build

Each LaTeX source sits next to its PDF. Rebuild a PDF from its folder with:

```bash
tectonic -Z continue-on-errors sample-authordraft.tex
```

## Notes

Each report uses the ACM `acmart` template, so its folder also holds the template's files. `auto_test_tools.py` in each task folder is the course's test harness.
