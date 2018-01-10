import csv
import pandas as pd



toxicDf = pd.read_csv("toxicWords.csv")
toxicWords = toxicDf['words'].tolist()

insultDf = pd.read_csv("insultWords.csv")
insultWords = insultDf['words'].tolist()

severeToxicDf = pd.read_csv("severeToxicWords.csv")
severeToxicWords = severeToxicDf['words'].tolist()

threatDf = pd.read_csv("threatWords.csv")
threatWords = threatDf['words'].tolist()

obsceneDf = pd.read_csv("obsceneWords.csv")
obsceneWords = obsceneDf['words'].tolist()

identityHateDf = pd.read_csv("identityHateWords.csv")
identityHateWords = identityHateDf['words'].tolist()


testData = pd.read_csv("test.csv")

toxicPercents = []
severeToxicPercents = []
insultPercents = []
obscenePercents = []
threatPercents = []
identityHatePercents = []

for index, row in testData.iterrows():
    if index%100 == 0:
        print(index)
    comment = row['comment_text']
    
    insult = 0.0
    toxic = 0.0
    severeToxic = 0.0
    threat = 0.0
    obscene = 0.0
    identityHate = 0.0
    length = 0.0
    if isinstance(comment, str):
        for i in comment.split():
            length+=1
            if i in insultWords:
                insult+=1
            if i in toxicWords:
                toxic+=1
            if i in severeToxicWords:
                severeToxic+=1
            if i in threatWords:
                threat+=1
            if i in obsceneWords:
                obscene+=1
            if i in identityHateWords:
                identityHate+=1
    insultPer = insult/length
    toxicPer = toxic/length
    severeToxicPer = severeToxic/length
    threatPer = threat/length
    obscenePer = obscene/length
    identityPer = identityHate/length

    totalPer = insultPer+toxicPer+severeToxicPer+threatPer+obscenePer+identityPer
    if totalPer == 0.0:
        totalPer = 1.0
    toxicPercents.append(toxicPer/totalPer)
    insultPercents.append(insultPer/totalPer)
    severeToxicPercents.append(severeToxicPer/totalPer)
    threatPercents.append(threatPer/totalPer)
    obscenePercents.append(obscenePer/totalPer)
    identityHatePercents.append(identityPer/totalPer)

testClassifier = [('id', testData['id'].tolist()),
                  ('toxic', toxicPercents),
                  ('severe_toxic', severeToxicPercents),
                  ('obscene', obscenePercents),
                  ('threat', threatPercents),
                  ('insult', insultPercents),
                  ('identity_hate', identityHatePercents)]

dfTestClassifier = pd.DataFrame.from_items(testClassifier)
dfTestClassifier.to_csv('results.csv', index = False)
    
     
        
