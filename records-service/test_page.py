"""CI Test: Validates templates/records.html has the expected structural elements."""
import sys

HTML_FILE = "templates/records.html"
REQUIRED_SNIPPETS = ['id="search"', 'id="records-table"']


def run_tests():
    print("=== CI Records Page Validation Test ===")
    with open(HTML_FILE, "r") as f:
        html_content = f.read()

    failures = []
    for snippet in REQUIRED_SNIPPETS:
        if snippet in html_content:
            print(f"  PASS: found {snippet}")
        else:
            failures.append(f"FAIL: missing {snippet}")

    if failures:
        print("=== CI FAILED ===")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        print("=== CI PASSED ===")


if __name__ == "__main__":
    run_tests()
