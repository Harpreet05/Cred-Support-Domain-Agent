# Task 3 - Chunking, embeddings, and vector collections

Command: `.\.venv\Scripts\python.exe -m rag.evaluate`

The project creates fixed-size chunks with overlap and sentence-based chunks,
embeds the chunks locally, and keeps each chunk strategy in its own ChromaDB
collection. Persistent collection inspection returned:

```text
knowledge_base_sentence: 47
knowledge_base_fixed: 112
```
