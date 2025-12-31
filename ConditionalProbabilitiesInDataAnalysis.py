import pandas as pd
df = pd.read_csv('data.csv')
#print(df.shape)
#print(df.head())
#print(df.columns.tolist())
#print(df.info())

df['TextLength'] = df['Text'].apply(len)
medianTextLength = df['TextLength'].median()
#print(df['TextLength'])
#print(medianTextLength)
denominator = df['HelpfulnessDenominator'].replace(0, 1)
df['Helpfulness'] = df['HelpfulnessNumerator'] / denominator
df['IsHelpful'] = (df['Helpfulness'] > 0.5) & (df['HelpfulnessDenominator'] > 0)
print(f"Какова вероятность, что отзыв хороший, если отзыв длинный?\n"
      f"Расчет по формуле:")
pLong = (df['TextLength'] > medianTextLength).mean()
#print(pLong)
pGoodAndLong = ((df['Score'] >= 4) & (df['TextLength'] > medianTextLength)).mean()
#print(pGoodAndLong)
pGoodIfLong = pGoodAndLong / pLong
print(pGoodIfLong)
print(f"Какова вероятность, что отзыв хороший, если отзыв длинный?\n"
      f"Расчет через фильтр:")
df['IsGood'] = (df['Score'] >= 4).astype(int)
longReviews = df[df['TextLength'] > medianTextLength]
pGoodIfLongFilter = longReviews['IsGood'].mean()
print(pGoodIfLongFilter)
print(f"Какова вероятность, что отзыв хороший, если отзыв короткий?\n"
      f"Расчет по формуле:")
pShort = (df['TextLength'] <= medianTextLength).mean()
pGoodAndShort = ((df['Score'] >= 4) & (df['TextLength'] <= medianTextLength)).mean()
pGoodIfShort = pGoodAndShort / pShort
print(pGoodIfShort)
print(f"Какова вероятность, что отзыв хороший, если отзыв короткий?\n"
      f"Расчет через фильтр:")
shortReviews = df[df['TextLength'] <= medianTextLength]
pGoodIfShortFilter = shortReviews['IsGood'].mean()
print(pGoodIfShortFilter)
print(f"Какова вероятность, что отзыв полезный, если он хороший?"
      f"Расчет по формуле:")
pHighScore = (df['Score'] >= 4).mean()
pHelpfulAndHigh = (df['IsHelpful'] & (df['Score'] >= 4)).mean()
pHelpfulIfHigh = pHelpfulAndHigh / pHighScore
print(pHelpfulIfHigh)
print(f"Какова вероятность, что отзыв полезный, если он хороший?"
      f"Расчет через фильтр:")
highScoreReviews = df[df['Score'] >= 4]
pHelpfulIfHighFilter = highScoreReviews['IsHelpful'].mean()
print(pHelpfulIfHighFilter)

