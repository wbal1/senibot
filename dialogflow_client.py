from google.cloud import dialogflow
from google.oauth2 import service_account
import os
import json
import uuid  # UUID를 생성하기 위한 모듈

# 세션 ID 생성 함수
def generate_session_id():
    return str(uuid.uuid4())

# 사용 예시
u_session_id = generate_session_id()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
credentials_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
credentials = service_account.Credentials.from_service_account_info(credentials_info)

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path('suh-3-429200', u_session_id)
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code='ko')
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
