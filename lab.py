import openai
engines = openai.Engine.list()
openai.api_key = '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'
print(engines)