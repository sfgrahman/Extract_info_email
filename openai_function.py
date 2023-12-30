import os
from dotenv import load_dotenv
from openai import OpenAI
from schema import *
#from input_email import *

load_dotenv()

def openai_function_response(email):
    client = OpenAI()

    prompt = f"Please extract key information from this email: {email} "
    message = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        functions = function_descriptions,
        function_call="auto"
        
    )

    #print(response.choices[0].message.function_call.arguments)
    arguments = response.choices[0].message.function_call.arguments
    companyName = eval(arguments).get("companyName")
    priority = eval(arguments).get("priority")
    product = eval(arguments).get("product")
    amount = eval(arguments).get("amount")
    category = eval(arguments).get("category")
    nextStep = eval(arguments).get("nextStep")

    return {
        "companyName": companyName,
        "product": product,
        "amount": amount,
        "priority": priority,
        "category": category,
        "nextStep": nextStep
    }