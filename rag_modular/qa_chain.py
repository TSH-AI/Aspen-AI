"""
qa_chain.py
Responsible for building question-answering chains and QA logic
"""

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank
from typing import Any, Dict

def setup_qa_chain(llm: Any, vectordb: Any) -> Any:
    """
    Set up question-answering chain

    Args:
        llm (Any): Large language model instance
        vectordb (Any): Vector database instance
    Returns:
        Any: Question-answering chain instance
    """
    # Configure compressor and retriever
    compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2")
    retriever = vectordb.as_retriever(search_kwargs={"k": 30})
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )

    # Define Prompt template
    prompt_template = """
    You are an assistant tasked with answering questions based on excerpts from multiple documents.
    The provided context below may contain text from different source files. Where possible, the source filename is included in the metadata associated with each piece of context.
    Please answer the user's question based *only* on the provided document content. Prioritize information that directly addresses the question keywords and seems to come from the most relevant source if discernible. If you don't know the answer or the context does not contain the answer, please say so directly and do not fabricate an answer.

    Reference Content:
    {context}

    User Question:
    {question}

    Response Requirements:
    1. If the question involves tables:
       - You must extract complete tables from the original document, maintaining structure and all data
       - Use Markdown format for tables, keeping column alignment
       - Include table titles and all column/row labels
       - Preserve all values, units, and special symbols
       - Do not omit any data from tables
       - If table content is scattered across multiple retrieval results, merge into one complete table
       - When the user queries specific tables (such as "Table 2.1" or "Table 2.13"), ensure the complete table content is provided

    2. Special table processing notes:
       - First, check if the retrieved content contains a complete table
       - If table content is split across parts, analyze and reconstruct the complete table
       - Ensure all columns and rows are fully displayed
       - Include table headers and footnotes (if any)
       - For cross-page tables, pay special attention to completeness and note any missing parts

    3. For material properties:
       - Highlight key values (e.g., flash points, corrosion grades)
       - Note measurement conditions (temperature/pressure)

    4. Safety considerations:
       - Mark any dangerous material combinations
       - Include handling precautions from the source

    5. Formatting requirements:
       - Use bullet points for multi-value properties
       - Maintain the original section title format
       - Ensure all table data is complete and accurate

    Most importantly, ensure that table answers accurately reflect the actual data from the original document. Do not omit any columns or rows. If a complete table cannot be found, clearly state this and provide the available partial information.
    """

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Build question-answering chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=compression_retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt, "verbose": False},
    )
    return qa_chain

async def query(qa_chain: Any, question: str) -> Dict[str, Any]:
    """
    Execute question-answering

    Args:
        qa_chain (Any): Question-answering chain instance
        question (str): User question
    Returns:
        Dict[str, Any]: Question-answering result
    """
    # Call the chain's async interface
    return await qa_chain.ainvoke(question)
