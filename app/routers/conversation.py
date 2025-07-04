from fastapi import APIRouter, Depends
from config import get_settings
from langchain_openai import ChatOpenAI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from ai.graph import AgentGraph
from langchain.schema import HumanMessage

router = APIRouter(prefix="/api", tags=["Conversation"])


class QuestionRequest(BaseModel):
    """
    Model for the question request.
    """
    question: str


@router.post("/question")
async def ask_question(request: QuestionRequest, settings=Depends(get_settings)):
    """
    Endpoint to ask a question to the graph.

    Args:
        question (str): The question to ask.
        settings: Application settings dependency.

    Returns:
        StreamingResponse: A streaming response that yields chunks of the answer.
    """
    model = ChatOpenAI(api_key=settings.OPENAI_API_KEY)
    graph = AgentGraph()
    compiled_graph = graph.compile()

    async def generate_answer():
        async for chunk in compiled_graph.astream({
            "messages": [HumanMessage(content=request.question)],
            "retries": 0,
            "max_retries": 3,
            "model": model,
        }, stream_mode="messages"):
            if chunk[0]:  # type: ignore
                msg = chunk[0]  # type: ignore
                print(msg.content, end="", flush=True)
                yield f"data: {msg.content}\n\n".encode('utf-8')

    return StreamingResponse(generate_answer(), media_type="text/event-stream")
