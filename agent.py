from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground, serve_playground_app

from dotenv import load_dotenv
load_dotenv()

copywriter = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="copywriter",
    add_history_to_messages=True,
    num_history_runs=3,
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/storage.db"),
    tools=[TavilyTools()],
    show_tool_calls=True,
    instructions=open("prompts/copywriter.md").read(),
)

playground = Playground(agents=[copywriter])

if __name__ == "__main__":
    serve_playground_app(playground, port=8000)