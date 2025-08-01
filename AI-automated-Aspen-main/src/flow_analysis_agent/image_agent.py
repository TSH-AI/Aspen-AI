import os
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

from src.flow_analysis_agent.prompt import IMAGE_TO_MERMAID_FLOW_PROMPT

def get_image_file_name(url):
    # https://github.com/zhouxiaochi/AI-automated-Aspen/blob/main/example_flow_figures/energies-17-02381-fig-1.PNG?raw=true
    return url.split("/")[-1].replace("?raw=true", "")

url = "https://github.com/zhouxiaochi/AI-automated-Aspen/blob/main/example_flow_figures/energies-17-02381-fig-1.PNG?raw=true"
file_name = get_image_file_name(url)
load_dotenv()
chat = ChatOpenAI(
    model="gpt-4-vision-preview",
    max_tokens=256,
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
output = chat.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": IMAGE_TO_MERMAID_FLOW_PROMPT},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url,
                        "detail": "auto",
                    },
                },
            ]
        )
    ]
)
print(output.content)

with open(f"example_flow_figures/outputs/{file_name}.md", "w") as f:
    f.write(output.content)

