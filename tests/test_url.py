# test_url.py
from form_parser import fetch_html_from_url, parse_form
from pprint import pprint

url = "https://www.w3schools.com/html/html_forms.asp"  # sample test URL
html = fetch_html_from_url(url)
form_fields = parse_form(html)

print("Extracted Form Fields:\n")
pprint(form_fields)
