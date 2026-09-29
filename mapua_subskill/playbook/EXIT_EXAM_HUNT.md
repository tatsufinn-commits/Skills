# Exit-exam / off-ICS assessment hunt

## Why this exists

Blackboard **Share Calendar / ICS often omits** exit exams and many assessments.  
Empty ICS ≠ no exam.

## Procedure

1. Parse Commander query: course code, term, exam type (exit / midterm / finals / other).  
2. Search official hosts + query variants:  
   `{CODE} exit exam Mapua`, `{CODE} departmental exam`, program name + exit assessment.  
3. Check Brain/courses and External_Sources for admitted material.  
4. Secondary: Reddit/web — extract **claims with URLs**, grade secondary.  
5. Optional: merge calendar brief events if any match (bonus only).  
6. Package MAPUA_PACK.  
7. If empty: NOT_FOUND_PUBLIC + next_acquisition (LMS, faculty, college office — human paths listed as residual, not fetched if auth-walled).

## Hypothesis policy

If nothing solid: propose **where else to look** (hypotheses UNVERIFIED).  
Do **not** emit a fake date row under `claims`.
