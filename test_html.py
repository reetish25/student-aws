"""CI Test: Validates templates/index.html form field name attributes."""
import sys
from html.parser import HTMLParser

HTML_FILE = "templates/index.html"
REQUIRED_FIELDS = {"name": "name", "usn": "usn", "dept": "dept"}


class FormFieldParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            self.inputs.append(dict(attrs))


def run_tests():
    print("=== CI HTML Form Validation Test ===")
    with open(HTML_FILE, "r") as f:
        html_content = f.read()

    parser = FormFieldParser()
    parser.feed(html_content)

    found = {
        i.get("name", ""): i.get("id", "")
        for i in parser.inputs
        if i.get("type", "text") != "submit"
    }
    print(f"Found fields: {found}")

    failures = []
    for req_name, req_id in REQUIRED_FIELDS.items():
        if req_name not in found:
            failures.append(f'FAIL: Missing name="{req_name}"')
        elif found[req_name] != req_id:
            failures.append(
                f'FAIL: name="{req_name}" has wrong id="{found[req_name]}"'
            )
        else:
            print(f'  PASS: name="{req_name}" id="{req_id}"')

    if failures:
        print("=== CI FAILED ===")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        print("=== CI PASSED ===")


if __name__ == "__main__":
    run_tests()
