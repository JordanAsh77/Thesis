import pandas as pd
import crowdtruth

from crowdtruth.configuration import DefaultConfig
import dateparser


df = pd.read_csv("/Users/jordangijsbertha/Desktop/Programming/CrowdTruth/tutorial/data/Answers.csv")

print(df)


class TestConfig(DefaultConfig):
    
    inputColumns = ["videolocation"]
    outputColumns = ["picture_displayed"]
    customPlatformColumns = ["judgmentId", "unitId", "workerId", "startedAt", "submittedAt"]
    open_ended_task = False
    annotation_vector = ["protest", "revolt", "insurrection", "strike"]
    
    def processJudgments(self, judgments):
        # pre-process output to match the values in annotation_vector
        for col in self.outputColumns:
            # transform to lowercase
            judgments[col] = judgments[col].apply(lambda x: str(x).lower())
            # remove square brackets from annotations
        return judgments


data, config = crowdtruth.load(
    file = "/Users/jordangijsbertha/Desktop/Programming/CrowdTruth/tutorial/data/Answers.csv",
    config = TestConfig()
    
)

# print(data['judgments'].head())

results = crowdtruth.run(data, config)

print(results["units"].head())




 





