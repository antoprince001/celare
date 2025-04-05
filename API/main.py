from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig


class Text(BaseModel):
    content: str


analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Celare API is running!"}


@app.post("/v1/anonymize")
async def anonymize_text(text: Text):
    try:
        if not text or not text.content or text.content.strip() == "":
            return {"error": "No valid text provided"}
        if not (10 <= len(text.content) <= 500):
            return {"error": "Text length must be between 10 and 500 characters"}

        analyzer_results = analyzer.analyze(text=text.content, entities=[], language='en')
        anonymized_content = anonymizer.anonymize(
            text=text.content,
            analyzer_results=analyzer_results,
            operators={
                "DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"}),
                "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "<PHONE_NUMBER>"}),
                "TITLE": OperatorConfig("replace", {"new_value": "<TITLE>"}),
                "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "<EMAIL>"}),
                "PERSON": OperatorConfig("replace", {"new_value": "<PERSON>"})
            }
        )
        if anonymized_content is None:
            return {"error": "An error occurred during anonymization"}
        if anonymized_content.text == text.content:
            return {"error": "No sensitive information found to anonymize"}

        anonymized_text = anonymized_content.text
        return {"anonymized_text": anonymized_text}
    except Exception as e:
        return {"error": str(e)}
