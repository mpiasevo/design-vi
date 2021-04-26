import json
import sys
import time
import datetime
import gspread
import subprocess
import Apartmentparser
from oauth2client.service_account import ServiceAccountCredentials
GDOCS_OAUTH_JSON       = 'JSON-KEY-FILE'
GDOCS_SPREADSHEET_NAME = 'GOOGLE-SHEET-NAME'
#FREQUENCY_SECONDS      = 10
def login_open_sheet(oauth_key_file, spreadsheet):
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, 
                      scopes = ['https://spreadsheets.google.com/feeds',
                                'https://www.googleapis.com/auth/drive'])
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet. Check OAuth credentials, spreadsheet name, and')
        print('make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
print('Auto Apartments.com Parser, if apartment link includes multiple units, may not work...')
print('Press Ctrl-C to quit.')
worksheet = None
while True:
    url = input('Input URL from Apartments.com: ')
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
    dat = datetime.datetime.now()
    rent = Apartmentparser.rentInfo(url)[0]
    bed = Apartmentparser.rentInfo(url)[1]
    bath = Apartmentparser.rentInfo(url)[2]
    sqft = Apartmentparser.rentInfo(url)[3]
    add = Apartmentparser.rentInfo(url)[4]
    link = Apartmentparser.rentInfo(url)[5]

    try:
        worksheet.append_row((str(dat), rent, bed, bath, sqft, add, link))

    except:
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))