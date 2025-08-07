import asyncio
from dotenv import load_dotenv
from fpdf import FPDF
import os

load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatGoogle

# Unicode PDF class using built-in DejaVu font
class UnicodePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_font("DejaVu", "", os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf"), uni=True)
        self.set_font("DejaVu", size=12)

    def add_text(self, text):
        for line in text.split("\n"):
            self.multi_cell(0, 10, line)

async def main():
    agent = Agent(
        task="Analyse the recent Arxiv AI papers and summarize the key findings. Arxiv:https://arxiv.org/",
        task="Give me current data about the AI industry",
        llm=ChatGoogle(model="gemini-2.0-flash", temperature=0.1),
        verbose=True,
        headless=False,
    )

    result = await agent.run()
    final_text = result.extracted_content()[-1]

    print("\n" + "=" * 60)
    print("FINAL RESPONSE:")
    print("=" * 60)
    print(final_text)
    print("=" * 60)

    # Generate PDF
    pdf = UnicodePDF()
    pdf.add_text(final_text)
    pdf.output("arxiv_ai_summary.pdf")  # saved in current directory

asyncio.run(main())
