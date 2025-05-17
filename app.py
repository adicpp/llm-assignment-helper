import openai
import os
from helper import extract_text_from_pdf
from prompts import SUMMARY_PROMPT, QUIZ_PROMPT

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt, content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    file_path = input("Enter path to academic PDF file: ").strip()
    content = extract_text_from_pdf(file_path)

    print("\n--- Summary ---\n")
    summary = generate_response(SUMMARY_PROMPT, content)
    print(summary)

    print("\n--- Quiz Questions ---\n")
    quiz = generate_response(QUIZ_PROMPT, content)
    print(quiz)