import pandas as pd
import numpy as np
import subprocess as sp

df = pd.read_csv('./questions_with_LLM_answers.csv')
df1 = df.copy()
l1 = [f"not available" for i in range(df.shape[0])]

for index, row in df.iterrows():
    if "AAPL" not in row['Source Docs']:
        continue
    string = row['Question']
    command = f'''./graphragvenv/bin/python3 -m graphrag.query --root . --method local "{string}"'''
    print(string, command, index)
    result = sp.run(command, shell=True, capture_output=True, text=True)
    l1[index] = result.stdout
    
df1['Generated Answers'] = l1

l = ["" for i in range(df1.shape[0])]
for index, row in df1.iterrows():
    string = row['Generated Answers']
    if (string == 'not available'):
        continue
    start_index = string.find("SUCCESS")
    if start_index != -1:
        new_string = string[start_index: -2]
    l[index] = new_string
df2 = df1.copy()
df2['Generated Answers'] = l
df2.to_csv('new_questions_with_LLM_answers.csv', header=True, index=False)