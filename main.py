import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
import openai


def main():
    load_dotenv()
    print("Hello from langchain Ollama!")
 

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
        print("Response from the model:", response.generations[0][0].text)
    except openai.RateLimitError as ex:
        print(
            "Ollama API rate limit exceeded. Please try again later. Error details:",
            ex,
        )
        print("Fallback summary:", _fallback_summary(information))

if __name__ == "__main__":
    main()
