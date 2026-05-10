class AnalysisAgent:

    def analyze(self, df):

        summary = {}

        summary["max_conversion"] = df["conversion"].max()
        summary["mean_conversion"] = df["conversion"].mean()

        best_row = df.loc[df["conversion"].idxmax()]

        summary["best_conditions"] = best_row.to_dict()

        return summary
