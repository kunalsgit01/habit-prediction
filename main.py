
import pandas as pd


item_similarity_df = pd.read_csv("data.csv", index_col=0)
item_similarity_df = item_similarity_df.pivot_table(
    index="Name", columns="Habit", values="Rating")
item_similarity_df.fillna(0, inplace=True)
item_similarity_df = item_similarity_df.corr(method="pearson")
print(item_similarity_df)

def make_rec():
        data = request.json
        habit_category = data["habit"]
        try:
            similar_score = item_similarity_df[habit_category]
            similar_category = similar_score.sort_values(ascending=False)[1:50]
            api_recommendations = [*set(similar_category.index.to_list())]
        except:
            api_recommendations = ["Dance", "Stay-Fit-with-Exercises", "Exercise-Time", "Call-My-Parents", "Eat-Fruits",
                                   "Go-Climbing", "Practice-for-Baseball", "Watch-Your-Diet", "Appreciate-Others", "Count-Your-Steps"]
        return {"rec_habit": api_recommendations}

if __name__ == "__main__":
    make_rec()

