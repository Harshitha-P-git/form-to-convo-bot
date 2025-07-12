from form_filler import fill_form

form_url = "http://localhost:8000/form_wizard.html"  # make sure this matches your local server
responses = {
    "fname": "Harsh",
    "lname": "Mishra",
    "user_email": "harsh@example.com",
    "aadhaar_number": "123412341234",
    "gender": "Male",
    "lang_pref": "en"
}

fill_form(form_url, responses)
