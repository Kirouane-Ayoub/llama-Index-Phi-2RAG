# Phi-2 RAG Project

## Overview

**Phi-2 RAG** is a project that combines the power of the RAG (Retrieval-Augmented Generation) technique with the capabilities of the Phi-2 language model. This synergy enables the generation of highly accurate and contextually rich responses by harnessing external knowledge through RAG and leveraging the language generation capabilities of Phi-2.

### RAG

![image3](https://github.com/Kirouane-Ayoub/llama-Index-Phi-2RAG/assets/99510125/48fc95ce-4704-4dd9-b203-e673da63f98b)



*RAG* is a revolutionary technique in Natural Language Processing (NLP) designed to address the limitations of large language models (LLMs). The process involves Retrieval, Augmentation, and Generation:

1. **Retrieval:** Searches external databases or documents for relevant information.
2. **Augmentation:** Augments the retrieved information with the original input.
3. **Generation:** Utilizes the augmented context for precise and informative response generation.

#### Advantages of RAG:

- **Improved Factuality:** Generates more accurate and reliable responses.
- **Reduced Hallucination:** Minimizes the risk of false or misleading content.
- **Domain-Specific Knowledge:** Adaptable to specific domains for enhanced expertise.
- **Transparency:** Provides users with insight into the reasoning behind generated text by revealing retrieved information sources.

### Phi-2

*Phi-2* is a small language model (SLM) developed by Microsoft Research. With 2.7 billion parameters, Phi-2 is a Transformer-based model trained on diverse datasets for various tasks:

- **Generating Text:** Capable of creating diverse content formats, such as poems, code, scripts, music, emails, and more.
- **Language Translation:** Supports translation between over 100 languages.
- **Question Answering:** Provides comprehensive and informative answers, even for open-ended or challenging questions.
- **Creative Content Generation:** Can generate different types of creative content based on user requirements.

Phi-2, though still under development, shows potential as a powerful tool for tasks requiring common sense and logical reasoning.


![Screenshot from 2024-01-16 14-14-41](https://github.com/Kirouane-Ayoub/llama-Index-Phi-2RAG/assets/99510125/da4ffdbc-29a0-4406-a6df-0ff957983e27)



+ Source : **https://huggingface.co/microsoft/phi-2**

### LLAMA Index 🦙

![6462ca68c52fdda3d86e90d9_Frame 33-p-1600](https://github.com/Kirouane-Ayoub/llama-Index-Phi-2RAG/assets/99510125/748f19b8-d1aa-47b9-b495-0621086bcbd4)


*LLAMA Index* is a data framework designed to complement RAG systems. It acts as a toolkit for building applications powered by both large language models and customized data.

#### Main Components:

1. **Data Ingestion:** Connects various data sources (APIs, PDFs, documents, SQL databases) to make data accessible for LLMs.
2. **Data Indexing:** Structures and indexes data for efficient retrieval during queries.
3. **Query Interface:** Allows crafting queries in natural language for relevant information retrieval.
4. **Retrieval Engines:** Identify the most relevant information for LLM consideration.
5. **Augmentation Process:** Combines retrieved information with the original query, providing richer context.
6. **LLM Integration:** Seamlessly integrates with various LLMs, enhancing language generation capabilities.
7. **Output Channels:** Delivers responses through different channels based on the application's needs (e.g., text-based responses, chatbots).

#### Benefits of Using LLAMA Index:

- **Improved Accuracy and Factuality:** Grounds LLM responses in specific data, ensuring higher accuracy.
- **Enhanced Domain Expertise:** Tailors applications to specific domains for more informed responses.
- **Transparent Reasoning:** Reveals data sources used for retrieval, providing transparency into the LLM's reasoning.
- **Flexibility and Scalability:** Modular design allows easy scaling and adaptation to different use cases.

+ Source : **https://docs.llamaindex.ai/en/stable**

## Usage : 
```
pip install -q -U git+https://github.com/huggingface/transformers.git
pip install -r requirement.txt 
python3 app.py
```

![Screenshot from 2024-01-16 14-06-05](https://github.com/Kirouane-Ayoub/llama-Index-Phi-2RAG/assets/99510125/fce405f6-c4a9-435f-a521-079d89ea8f88)
