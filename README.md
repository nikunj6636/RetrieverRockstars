## Tracking Runs
https://langsmith.com
Project: GraphIndex Creator

## Running LLMs
- To run ollama model with GPU
    ```
    CUDA_VISIBLE_DEVICES=0 ollama run gemma2:2b
    ```

- To run AzureOpenAI model (make a .env file)
    ```
    AZURE_OPENAI_API_KEY=
    AZURE_OPENAI_ENDPOINT=https://divi-azure-openai.openai.azure.com
    ```

## Implementations:

### Networkx Graph and Graph Index Creator:

Making KG using Graph Index Creator and stores in Networkx Entity Graph: \
https://www.kaggle.com/code/aritrase/bulding-graphqa-chain-using-langchain

- Exteacts Triplets from Graph which are insufficient sources of knowledge and hence GrapgRAG
not able to perform.


### Local to Global Text Summarization:

Implementation of GraphRAG with community level summaries: \
https://github.com/ApexIQ/End-to-End-Graphrag-implementation


### Neo4J Limitations encountered: (running and analysing the code)

Neo4j documentation with langchain:
https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/

GraphRAG with Langchain and Neo4J (implementation): Fails over Cypher Generation Chain because of lack of proper schema \
https://medium.com/@jinglemind.dev/mastering-advanced-rag-methods-graphrag-with-neo4j-implementation-with-langchain-42b8f1d05246

Generates custom knowledge Graph:
https://github.com/harrisonsrp/Knowledge-Graph-for-RAG-using-Neo4j/tree/master

__NOTE__: Unavailability of well defined schema in advance in case of unstructured data becomes a limitation of using Graph database like Neo4J. Becuase of this LLMs fails to generate valid cypher queries