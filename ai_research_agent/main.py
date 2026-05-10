from agents.literature_agent import LiteratureAgent
from agents.extraction_agent import ExtractionAgent
from agents.doe_agent import DOEAgent
from agents.analysis_agent import AnalysisAgent
from agents.recommendation_agent import RecommendationAgent


def main():

    # 1. Literature analysis
    literature_agent = LiteratureAgent()

    try:
        paper_result = literature_agent.analyze_paper(
            "data/papers/sample.pdf"
        )

        print("\n=== Literature Analysis ===")
        print(paper_result)

    except Exception as e:
        print("PDF analysis skipped:", e)
        paper_result = "{}"

    # 2. Parameter extraction
    extractor = ExtractionAgent()

    parameters = extractor.extract_parameters(paper_result)

    print("\n=== Structured Parameters ===")
    print(parameters)

    # 3. DOE experiment generation
    doe_agent = DOEAgent()

    experiments = doe_agent.generate_experiments()

    print("\n=== DOE Experiments ===")
    print(experiments)

    # 4. Simulated experimental results
    experiments["conversion"] = [
        65,
        72,
        81,
        79,
        88,
        91,
        85,
        76,
        82
    ]

    # 5. Analysis
    analysis_agent = AnalysisAgent()

    summary = analysis_agent.analyze(experiments)

    print("\n=== Analysis Summary ===")
    print(summary)

    # 6. Recommendation
    recommend_agent = RecommendationAgent()

    next_round = recommend_agent.recommend_next_round(
        summary["best_conditions"]
    )

    print("\n=== Next Round Recommendation ===")
    print(next_round)


if __name__ == "__main__":
    main()
