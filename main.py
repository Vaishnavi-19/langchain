import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langsmith.client import Client
from langsmith.schemas import RunTypeEnum
import openai


def main():
    load_dotenv()
    print("Hello from langchain Ollama!")

    # LangSmith tracing configuration (optional but required to see the project in LangSmith)
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    langsmith_project = os.getenv("LANGSMITH_PROJECT", "default")

    if langsmith_api_key:
        try:
            client = Client(api_key=langsmith_api_key)
            client.create_project(langsmith_project, upsert=True)
            print(f"LangSmith project configured: {langsmith_project}")
        except Exception as e:
            print("Unable to configure LangSmith project:", e)

    information = "Raghavendra Tirtha (Rāghavēndra Tīrtha) (c.1595 – c.1671) was a Vaishnava scholar, theologian, and saint. He was also known as Sudha Parimalacharya (Sudhā Parimaḷācārya). His diverse oeuvre include commentaries on the works of Madhva, Jayatirtha, and Vyasatirtha, interpretation of the Principal Upanishads from the standpoint of Dvaita and a treatise on Purva Mimamsa. He served as the pontiff of the matha at Kumbakonam from 1621 to 1671.[1] Raghavendra Tirtha was also an accomplished player of the veena and he composed several songs under the name of Venu Gopala.[2] His memorial at Mantralayam attracts lakhs (hundreds of thousands) of visitors every year."
    prompt = PromptTemplate.from_template(
        "What is the summary of the following information: {information}"
        "1.Interestig points in the information\n"
        "2.Important entities mentioned in the information\n"
        "3.Overall summary of the information"
    )
    llm =ChatOllama(model="gemma3:4b", temperature=0)
    prompt_text = prompt.format(information=information)

    def _fallback_summary(text: str, max_sentences: int = 2) -> str:
        """Create a quick local summary if the API call fails."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        return ". ".join(sentences[:max_sentences]) + ("." if len(sentences) >= max_sentences else "")

    try:
        response = llm.generate([[HumanMessage(content=prompt_text)]])
        summary_text = response.generations[0][0].text
        print("Response from the model:", summary_text)

        if langsmith_api_key:
            try:
                client.create_run(
                    name="Ollama summarization",
                    inputs={"information": information, "prompt": prompt_text},
                    outputs={"summary": summary_text},
                    run_type=RunTypeEnum.llm,
                    project_name=langsmith_project,
                )
                print(f"Logged run to LangSmith project: {langsmith_project}")
            except Exception as e:
                print("Failed to log run to LangSmith:", e)
    except openai.RateLimitError as ex:
        print(
            "Ollama API rate limit exceeded. Please try again later. Error details:",
            ex,
        )
        print("Fallback summary:", _fallback_summary(information))

if __name__ == "__main__":
    main()
