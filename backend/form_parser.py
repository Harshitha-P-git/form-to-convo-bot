import requests
from bs4 import BeautifulSoup

def fetch_html_from_url(url):
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL. Status code: {response.status_code}")
    return response.text

def parse_form(html_content):
    soup = BeautifulSoup(html_content, 'lxml')

    # 🧩 Find the <form> tag
    form = soup.find('form')
    if not form:
        print("❌ No <form> tag found in the HTML.")
        return []

    # 🔍 Collect all relevant input elements
    inputs = form.find_all(['input', 'select', 'textarea'])
    print(f"✅ Found {len(inputs)} input elements")

    fields = []

    for tag in inputs:
        name = tag.get('name')
        if not name:
            print(f"⚠️ Skipping unnamed field: {tag}")
            continue

        field = {
            'tag': tag.name,
            'type': tag.get('type', 'text') if tag.name == 'input' else tag.name,
            'name': name,
            'id': tag.get('id'),
            'placeholder': tag.get('placeholder'),
            'required': tag.has_attr('required'),
            'label': None,
            'options': None,
            'validation': {}
        }

        # 🔗 Try to find label for the input
        if field["id"]:
            label_tag = soup.find('label', attrs={'for': field["id"]})
            if label_tag:
                field["label"] = label_tag.text.strip()

        if not field["label"]:
            parent = tag.find_parent('label')
            if parent:
                field["label"] = parent.text.strip()

        # 📋 Extract options from <select>
        if tag.name == 'select':
            options = tag.find_all('option')
            field['options'] = [opt.text.strip() for opt in options if opt.text.strip()]

        # 🛡️ Validation rules
        for attr in ['min', 'max', 'pattern']:
            if tag.has_attr(attr):
                field['validation'][attr] = tag[attr]

        fields.append(field)

    print(f"✅ Parsed {len(fields)} valid fields from <form>.")
    return fields
