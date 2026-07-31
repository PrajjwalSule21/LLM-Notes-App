from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="My LLM Notebook")

templates = Jinja2Templates(directory="templates")

# add/remove entries here as you create more notes
NOTES = [
    {
        "title": "LLM API Basics",
        "url": "/notes/llm-api-basics",
        "description": "chat completions, system/user/assistant roles, temperature, max_tokens, streaming",
    },
    {
        "title": "Tokenization, Context Window, top_p, top_k",
        "url": "/notes/tokenization-context-topp-topk",
        "description": "how text becomes tokens, the context window limit, nucleus vs top-k sampling",
    },
    {
        "title": "Prompt Engineering Fundamentals",
        "url": "/notes/prompt-engineering-fundamentals",
        "description": "zero-shot, few-shot, and system prompt design",
    },
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"notes": NOTES})


@app.get("/notes/llm-api-basics", response_class=HTMLResponse)
async def llm_api_basics(request: Request):
    return templates.TemplateResponse(request, "notes/llm_api_basics.html", {})


@app.get("/notes/tokenization-context-topp-topk", response_class=HTMLResponse)
async def tokenization_context_topp_topk(request: Request):
    return templates.TemplateResponse(
        request, "notes/tokenization_context_topp_topk.html", {}
    )


@app.get("/notes/prompt-engineering-fundamentals", response_class=HTMLResponse)
async def prompt_engineering_fundamentals(request: Request):
    return templates.TemplateResponse(
        request, "notes/prompt_engineering_fundamentals.html", {}
    )
