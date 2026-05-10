from utils.pdf_reader import read_pdf
from utils.llm_client import ask_llm


class LiteratureAgent:

    def analyze_paper(self, pdf_path):

        text = read_pdf(pdf_path)

        prompt = f'''
You are an enzyme catalysis expert.

Extract the following information:

1. Enzyme name
2. Substrate
3. Temperature
4. Flow rate
5. Residence time
6. Molar ratio
7. Conversion
8. Solvent
9. Immobilization method

Return JSON only.

Paper content:
{text[:15000]}
'''

        result = ask_llm(prompt)

        return result
