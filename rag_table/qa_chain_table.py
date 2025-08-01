"""
qa_chain.py
Responsible for constructing and managing the question-answering chain.
"""
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank
from typing import Any, Dict

def setup_qa_chain(llm: Any, vectordb: Any) -> Any:
    """
    Sets up the QA chain.

    Args:
        llm (Any): An instance of the language model.
        vectordb (Any): An instance of the vector database.
    Returns:
        Any: An instance of the RetrievalQA chain.
    """
    # Configure the compressor and retriever
    compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2")
    retriever = vectordb.as_retriever(search_kwargs={"k": 30})
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )
    
    # Create the Prompt Template
    template = """
    You are an intelligent assistant for a cooling tower company, specializing in answering questions about GXT series cooling tower specifications.
    Please answer the user's question based on the following context information.
    If the context does not contain the answer, please state that the data is not available, do not try to make up an answer.
    Answer in Markdown format.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

    # Configure and create the QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=compression_retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    
    return qa_chain

def query(qa_chain: Any, question: str) -> Dict[str, Any]:
    """
    Executes a query using the QA chain.

    Args:
        qa_chain (Any): An instance of the RetrievalQA chain.
        question (str): The user's question.
    Returns:
        Dict[str, Any]: The result of the query.
    """
    result = qa_chain.invoke({"query": question})
    return result
