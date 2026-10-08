"""Score process steps for AI readiness and recommend who does the work.

    python ai-readiness/scorer.py ai-readiness/sample_steps.csv

Each step is rated 1-5 on six factors. The output is a recommendation per step:
AUTOMATE (agent acts), AUGMENT (agent prepares, person decides) or HUMAN-LED
(person owns it, AI only retrieves). Judgment or regulatory risk of 4+ caps a
step at AUGMENT; 5 makes it HUMAN-LED whatever the automation potential.
"""
import csv
import sys

WEIGHTS = {"volume": 0.25, "rule_clarity": 0.25, "data_availability": 0.2,
           "exception_rate": 0.15, "error_cost": 0.15}
FACTORS = ["volume", "rule_clarity", "data_availability", "exception_rate", "error_cost", "judgment_risk"]


def potential(row):
    """0-100. High volume, clear rules and good data raise it; exceptions and error cost lower it."""
    raw = (WEIGHTS["volume"] * row["volume"] + WEIGHTS["rule_clarity"] * row["rule_clarity"] +
           WEIGHTS["data_availability"] * row["data_availability"] +
           WEIGHTS["exception_rate"] * (6 - row["exception_rate"]) +
           WEIGHTS["error_cost"] * (6 - row["error_cost"]))
    return round((raw - 1) / 4 * 100)


def recommend(row):
    p = potential(row)
    risk = row["judgment_risk"]
    if risk >= 5:
        return p, "HUMAN-LED"
    if p >= 70 and risk <= 2:
        return p, "AUTOMATE"
    if p >= 45:
        return p, "AUGMENT"
    return p, "HUMAN-LED"


def score_file(path):
    out = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            vals = dict((f, int(row[f])) for f in FACTORS)
            for f, v in vals.items():
                if not 1 <= v <= 5:
                    raise ValueError("%s: %s must be 1-5" % (row["step"], f))
            p, rec = recommend(vals)
            out.append({"family": row["family"], "step": row["step"], "potential": p, "recommendation": rec})
    return out


if __name__ == "__main__":
    rows = score_file(sys.argv[1] if len(sys.argv) > 1 else "ai-readiness/sample_steps.csv")
    print("%-5s %-44s %9s  %s" % ("Fam", "Step", "Potential", "Recommendation"))
    for r in rows:
        print("%-5s %-44s %9d  %s" % (r["family"], r["step"], r["potential"], r["recommendation"]))
