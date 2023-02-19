import requests
from bs4 import BeautifulSoup

# Set the API endpoint and parameters
url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
params = {
    "max_tokens": 1024,
    "n": 1,
    "stop": ".",
    "temperature": 0.5,
}

# Read the input questions from a file
with open("input.txt", "r") as input_file:
    questions = input_file.readlines()

# Open the output file in append mode
with open("output2.txt", "a") as output_file:
    # Loop over the questions and send each one as a separate request to the API endpoint
    for i, question in enumerate(questions):
        # Set the prompt parameter for this question
        prompt = f"{i+1}. {question.strip()}"

        # Set the prompt parameter in the API request
        params["prompt"] = prompt

        # Make the HTTP request and get the HTML response
        response = requests.post(url, json=params)
        html = response.content

        # Parse the HTML response and extract the text content
        soup = BeautifulSoup(html, "html.parser")
        response_text = soup.find("p").get_text() if soup.find("p") is not None else ""

        # Write the response text to the output file for this question
        output_file.write(f"{prompt}\n{response_text}\n\n")
