import requests

contactDetails = {
        "name": 'b3l914n',
        "lastname": 'b3l9',
        "email": 'sarcartist@gmail.com',
        "message": 'Hello from Belgium'
        }

r = requests.post('https://lambdaschool.com/contact-form', json=contactDetails)

print (r.text)
