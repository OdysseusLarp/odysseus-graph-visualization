from functools import cache
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1_MgBZXhKJ-HT6rUY2TCXWP5FW2TBGtnNGMFpR7RnaM4"


def get_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


@cache
def get_organization_data(
    spreadsheet_id=SAMPLE_SPREADSHEET_ID,
    range="Taulukko1!A1:E449",  # TODO can the exact range be left unspecified?
):
    creds = get_credentials()
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()

    values = result["values"]
    header_row = values.pop(0)

    return [dict(zip(header_row, row)) for row in values]


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_organization_data())
