import pandas as pd
   
df = pd.read_csv('./dnps_score.csv', encoding='utf-8')

def condition_based_B(value):
    if value >= 95:
        return '你的作業展現了超水準的資訊軟體應用能力，表現極為出色。'
    elif value >= 90:
        return '你的作業展現了高水準的資訊軟體應用能力，表現相當出色。'
    elif value >= 85:
        return '你在課堂中展現穩定的學習能力，完成了大部分的課堂作業。'
    elif value >= 80:
        return '你的課堂表現偶有佳作，完成了部分的作業，但還有進步的空間。'
    else:
        return '你掌握了一些基本的資訊技能，但還有很大的進步空間。'


df['comments'] = df['score'].apply(condition_based_B)

#print(df)

df.to_excel('./dnps_comments.xlsx', index=False, encoding='utf-8')