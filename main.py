import openai

# Initialize the API key for OpenAI
openai.api_key = "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"

# Read the input file line by line
with open("input.txt", "r") as file:
    lines = file.readlines()

# Initialize the responses list
responses = []

# Loop through each line and get the response from ChatGPT
with open("output.txt", "w") as file:
    for line in lines:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=line,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text.strip()
        file.write(line + response + "\n")
        
        # responses.append(response)

# # Write the responses to the output file
# with open("output.txt", "w") as file:
#     for response in responses:
#         file.write(response + "\n")