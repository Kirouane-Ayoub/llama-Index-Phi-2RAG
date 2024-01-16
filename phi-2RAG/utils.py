from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import HuggingFaceLLM
import torch
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.prompts.prompts import SimpleInputPrompt

documents = SimpleDirectoryReader("Data").load_data()
system_prompt = "As a Q&A assistant, your primary objective is to respond to inquiries with the utmost precision, concentrating on delivering accurate answers in alignment with the given instructions and context."

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")


model_name = "microsoft/phi-2"
device_map = "cuda"
llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=250,
    generate_kwargs={"temperature": 0.5, 
                     "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name=model_name,
    model_name=model_name,
    device_map=device_map,
    model_kwargs={"torch_dtype": torch.bfloat16}
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

service_context = ServiceContext.from_defaults(
    chunk_size=256,
    llm=llm,
    embed_model=embed_model
)

index = VectorStoreIndex.from_documents(documents, 
                                        service_context=service_context)

query_engine = index.as_query_engine()

def predict(input, history):
  response = query_engine.query(input)
  return str(response)
