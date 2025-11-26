# main.py
import os
import json
import random
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# IMPORT YOUR DATA AND TEMPLATES
from email_templates import PROMPT_LIST
from variables import TITLES, INDUSTRIES, PAINS, VALUES, COMPANY_PREFIXES, COMPANY_SUFFIXES

load_dotenv()

# CONFIGURATION
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash-thinking-exp-01-21"
OUTPUT_FILE = "final_training_dataset.jsonl"
MAX_RETRIES = 3  # How many times to try if API fails

def generate_company_name():
    return f"{random.choice(COMPANY_PREFIXES)}{random.choice(COMPANY_SUFFIXES)}"

def get_gemini_response(client, prompt):
    """
    Wraps the API call in a retry loop to handle rate limits or server errors.
    """
    for attempt in range(MAX_RETRIES):
        try:
            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)],
                ),
            ]
            
            generate_content_config = types.GenerateContentConfig(
                temperature=0.7,
                # STRICT SYSTEM INSTRUCTION TO REMOVE FLUFF
                system_instruction=[
                    types.Part.from_text(text="""
                    You are a Senior Sales Copywriter. 
                    Output Rules:
                    1. Output strictly the email draft only. 
                    2. Do not include 'Subject:' labels inside the body if the prompt asks for a specific subject line format, just write the subject line as the first line.
                    3. Do not include conversational filler like 'Here is the email'.
                    4. Do not use markdown blocks (```).
                    """)
                ],
            )

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=contents,
                config=generate_content_config,
            )
            return response.text.strip() # Clean up whitespace

        except Exception as e:
            wait_time = 2 ** attempt # Exponential Backoff (2s, 4s, 8s)
            print(f"⚠️ API Error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    
    return None # Failed after 3 attempts

def generate_synthetic_data(num_emails):
    if not API_KEY:
        print("❌ Error: GEMINI_API_KEY not found in environment variables.")
        return

    client = genai.Client(api_key=API_KEY)
    
    print(f"🚀 Starting generation of {num_emails} emails...")
    
    successful_generations = 0

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        for i in range(num_emails):
            
            # A. PREPARE DATA
            selected_template = random.choice(PROMPT_LIST)
            
            variables = {
                "title": random.choice(TITLES),
                "company": generate_company_name(),
                "pain": random.choice(PAINS),
                "value": random.choice(VALUES),
                "industry": random.choice(INDUSTRIES)
            }

            # B. INJECT VARIABLES (Safeguard against missing keys)
            try:
                formatted_prompt = selected_template["text"].format(**variables)
            except KeyError as e:
                # If your template has {Decision_Maker} but variables.py doesn't, this catches it.
                print(f"❌ Template {selected_template['id']} Error: Missing variable {e}")
                continue

            # C. CALL API
            email_body = get_gemini_response(client, formatted_prompt)

            if email_body:
                # D. SAVE TO JSONL (Chat format for Fine-Tuning)
                entry = {
                    "messages": [
                        {"role": "system", "content": "You are a Senior Sales Copywriter."},
                        # We reconstruct the user prompt to be generic for the training data
                        {"role": "user", "content": f"Write a {selected_template['style']} email to a {variables['title']}."},
                        {"role": "assistant", "content": email_body}
                    ]
                }
                
                f.write(json.dumps(entry) + "\n")
                successful_generations += 1
                
                # Small visual progress bar
                if successful_generations % 10 == 0:
                    print(f"✅ Generated {successful_generations} emails...")
            else:
                print(f"❌ Failed to generate email {i+1} after retries.")

    print(f"\n🎉 Job Complete. Saved {successful_generations} emails to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Start small to test, then change to 100000
    generate_synthetic_data(1)
