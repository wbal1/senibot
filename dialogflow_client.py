import os
import json
from google.oauth2 import service_account
from google.cloud import dialogflow_v2 as dialogflow

# 환경 변수에서 자격 증명을 로드
credentials_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
credentials = service_account.Credentials.from_service_account_info(credentials_info)

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text
