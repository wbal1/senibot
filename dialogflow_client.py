from google.cloud import dialogflow
import os
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
credentials_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
credentials = service_account.Credentials.from_service_account_info(credentials_info)

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
