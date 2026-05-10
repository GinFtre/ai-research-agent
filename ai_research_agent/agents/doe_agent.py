import pandas as pd


class DOEAgent:

    def generate_experiments(self):

        factors = {
            "temperature": [40, 50, 60],
            "flow_rate": [0.1, 0.3, 0.5],
            "molar_ratio": [1, 3, 5],
            "enzyme_loading": [5, 10, 15]
        }

        experiments = []

        for t in factors["temperature"]:
            for f in factors["flow_rate"]:
                for m in factors["molar_ratio"]:
                    for e in factors["enzyme_loading"]:

                        experiments.append({
                            "temperature": t,
                            "flow_rate": f,
                            "molar_ratio": m,
                            "enzyme_loading": e
                        })

        df = pd.DataFrame(experiments)

        return df.sample(9)
