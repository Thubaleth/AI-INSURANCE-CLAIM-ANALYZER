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

def classify(message):
    
  response = client.responses.parse(
     model="gpt-4o-mini",
    
     input=f"""
  You are an insurance customer support analyzer.

  your job is to classify the following categories:

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
  customer message:
  "My car was hit by another vehichle."

  category:
  CAR_ACCIDENT

  Example 2:
  customer message:
  "Someone stole my laptop from my house."

  Category:
  THEFT


  Example 3:
  " My roof was damaged during a heavy storm."

  Category:
  HOME_DAMAGE


  Example 4:
  "I need to claim for my hospital treatment."

   Category:
  MEDICAL_CLAIM


  Example 5:
  "When will my insurance claim be processed?"

   Category:
  CLAIM_STATUS

   Now classify this new customer message:

  Customer message:
  {message}

  Return the category and a short explanation for why the message belongs to that category.

   
  """,
 text_format=ClassificationResult
  
  )
  
  return response.output_parsed

result = classify(
  "Another driver crashed into my Toyota yesterday"
)






print("category: ",result.category)
print("reason: ",result.reason)


