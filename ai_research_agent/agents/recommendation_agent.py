class RecommendationAgent:

    def recommend_next_round(self, best_conditions):

        next_conditions = {
            "temperature": [
                best_conditions["temperature"] - 5,
                best_conditions["temperature"],
                best_conditions["temperature"] + 5
            ],

            "flow_rate": [
                round(best_conditions["flow_rate"] * 0.8, 2),
                best_conditions["flow_rate"],
                round(best_conditions["flow_rate"] * 1.2, 2)
            ]
        }

        return next_conditions
