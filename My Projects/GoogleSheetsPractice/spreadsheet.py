import gspread pprint
from oath2client.service_account import ServiceAcccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAcccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Python test data - cleaning').sheet1

results = sheet.get_all_records()

print(results)
