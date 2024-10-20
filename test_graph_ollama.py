from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_community.llms import Ollama
## Successfully executed!

llm = Ollama(model="gemma2:2b")

llm_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=['Category'],
    allowed_relationships=['Relation'],
    strict_mode=False
)

llm_transformer.convert_to_graph_documents([Document(page_content="A cat is an animal. It has a tail")])