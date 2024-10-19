from openai import OpenAI

client = OpenAI(
    api_key = "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",
)
command = ''' '''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named soumyajit who speaks hindi as well as english. He is from india and is a coder. You have to analyze chat history and rspond like soumyajit"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)