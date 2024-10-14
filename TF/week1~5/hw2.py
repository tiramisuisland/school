import pandas as pd

data = {
    "Name" : ["Jacky", "Peter", "John", "Joe"],
    "Engligh" : [90, 73, 78, 89],
    "Chinese" : [67, 70, 55, 45]
    }
StudentDF = pd.DataFrame(data)
#自訂索引值
StudentDF.columns = ["Student Name", "English Sorce", "Chinese Sorce"]
StudentDF.index = ["NO 1", "NO 2", "NO 3", "NO 4"]
print(StudentDF)