import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel



load_dotenv()
Api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=Api_key)

#clasification results must have a category and reason
class ClassificationResult(BaseModel):
  category:str
  reason:str
  location:str
  vehicle:str
  incident_date:str
  sentiment:str



def classify(message):
    
  response = client.responses.parse(
     model="gpt-4o-mini",
    
     input=f"""
  You are an insurance customer support analyzer.

  Your job is to classify the customer's message into exactly ONE
  of the following categories:

  CAR_ACCIDENT
  THEFT
  HOME_DAMAGE
  MEDICAL_CLAIM
  TRAVEL_CLAIM
  POLICY_QUESTION
  CLAIM_STATUS
  PAYMENT
  OTHER


  Example 1:

  Customer message:
  "My car was hit by another vehicle."

  Category:
  CAR_ACCIDENT


  Example 2:

  Customer message:
 "Someone stole my laptop from my house."

  Category:
  THEFT


  Example 3:

  Customer message:
  "My roof was damaged during a heavy storm."

  Category:
  HOME_DAMAGE

  your job is also to extract the following from the cutomer message:

  Location:
  The city or place where the incident occurred.

  vehicle:
  The vehicle involved in the incident.

  incident_date:
  The date or relative data of the incident.

  Analyze the sentiment of the customer's message.

  The sentiment must be exactly one of:

  POSITIVE
  NEUTRAL
  NEGATIVE

  POSITIVE means the customer expresses satisfaction,
  happiness, gratitude, or a positive experience.

  NEUTRAL means the customer is simply asking for information
  without expressing a strong emotion.

  NEGATIVE means the customer expresses frustration,
  anger, disappointment, sadness, or dissatisfaction

    Return:
  - category
  - reason
  - location
  - vehicle
  - incident date
  - sentiment

  If information is not provided, return "unknown"


   Now classify this new customer message:

  Customer message:
  {message}

  Return the category and a short explanation for why the message belongs to that category.

   
  """,
 text_format=ClassificationResult
  
  )
  
  return response.output_parsed

result = classify(
   "I am very happy with how quickly my claim was processed."
)

print("category : ",result.category)
print("reason : ",result.reason)
print("location : ",result.location)
print("vehichle : ",result.vehicle)
print("incident date : ",result.incident_date)
print("sentiment : ",result.sentiment)
