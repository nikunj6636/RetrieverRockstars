## Successfully executed!

from langchain_community.llms import Ollama
llm = Ollama(model="gemma2:2b")
print(llm.invoke("what is Gemma?"))