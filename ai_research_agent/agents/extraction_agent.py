import json


class ExtractionAgent:

    def extract_parameters(self, llm_output):

        try:
            data = json.loads(llm_output)
            return data

        except Exception as e:
            print("JSON parsing failed:", e)
            return None
