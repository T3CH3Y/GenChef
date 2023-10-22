from config import config

import os
import json
import openai
import weaviate

from langchain.chat_models import ChatOpenAI

from llama_index import (
    OpenAIEmbedding,
    PromptHelper,
    QuestionAnswerPrompt,
    RefinePrompt,
    ServiceContext,
    VectorStoreIndex,
)

from llama_index.llm_predictor import LLMPredictor
from llama_index.vector_stores import WeaviateVectorStore
from llama_index.callbacks import CallbackManager, LlamaDebugHandler

def callchef(text_query):
    client = weaviate.Client(
    url = "https://gen-chef-grbe0axw.weaviate.network/",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="rF9pAPONKDg6HyxoP7f0Q4iC3A5MRdIiLaZW"),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": "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"  # Replace with your inference API key
    }
    )

    openai.api_key = config["OPENAI_KEY"]
    
    weaviate_api_key = "rF9pAPONKDg6HyxoP7f0Q4iC3A5MRdIiLaZW"
    weaviate_url = "https://gen-chef-grbe0axw.weaviate.network/"
    tgi_endpoint_url = os.getenv("OPENAI_MODEL")

    if not weaviate_api_key or not weaviate_url or not tgi_endpoint_url:
        exit(
            "Make sure you've set WEAVIATE_API_TOKEN, WEAVIATE_URL, and TGI_ENDPOINT_URL environment variables"
        )

    auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)

    client = weaviate.Client(
        url=weaviate_url,
        auth_client_secret=auth_config,
    )

    embed_model = OpenAIEmbedding(embed_batch_size=10)

    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(temperature=0, 
                       model=config["OPENAI_MODEL"], 
                       openai_api_key=config["OPENAI_KEY"], 
                       streaming=True,
                       max_tokens = 1000
                       )
        # llm=HuggingFaceTextGenInference(
        #     inference_server_url=tgi_endpoint_url,
        #     max_new_tokens=512,
        #     streaming=True,
        # ),
    )

    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager([llama_debug])

    service_context = ServiceContext.from_defaults(
        embed_model=embed_model,
        llm_predictor=llm_predictor,
        prompt_helper=PromptHelper(context_window=1024),
        callback_manager=callback_manager,
    )
    
    vector_store = WeaviateVectorStore(
        weaviate_client=client, index_name="Recipe"
    )
    
    print("flag")
    print(vector_store)
    print("flag")
    
    index = VectorStoreIndex.from_vector_store(
        vector_store, service_context=service_context
    )

    text_qa_template = QuestionAnswerPrompt(
        """<s>[INST] <<SYS>>
    We have provided context information below. 

    {context_str}

    Given this information, please answer the question.
    <</SYS>>

    {query_str} [/INST]"""
        )

    refine_template = RefinePrompt(
            """<s>[INST] <<SYS>>
    The original query is as follows: 

    {query_str}

    We have provided an existing answer:

    {existing_answer}

    We have the opportunity to refine the existing answer (only if needed) with some more context below.

    {context_msg}
    <</SYS>>

    Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer. [/INST]"""
        )

    query_engine = index.as_query_engine(
        text_qa_template=text_qa_template,
        refine_template=refine_template,
        service_context=service_context,
        streaming=True,
        similiarity_top_k = 1
    )
    print(query_engine)
    
    response = query_engine.query(text_query)
    return str(response)

    #response = client.query.get("Recipe", ["name", "keywords", "ingredients"]).with_near_text({"concepts": ["arab cuisine"]}).with_limit(10).do()
    #print(dir(response))
    # print(response)
    # print(f"\n\nSources:\n\n{response.get_formatted_sources()}")
    # print(json.dumps(response, indent=4))