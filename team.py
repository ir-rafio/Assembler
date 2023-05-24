import time
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import preprocessor

def adjustDF(df):
    for col in df.columns:
        if df[col].nunique() == 1: df[col] = 0

    df['Max Rating'] *= df['Max Rating']
    df['Max Rating'] *= df['Max Rating']

    wt = []
    with open("weights.txt", "r") as file:
        for line in file:
            weight = float(line.strip())
            wt.append(weight)

    scaler = MinMaxScaler()
    df.iloc[:, 1:] = scaler.fit_transform(df.iloc[:, 1:])
    df.iloc[:, 1] *= wt[0]
    df.iloc[:, 2:6] *= wt[1]/4
    df.iloc[:, 6:] *= wt[2]/(len(df.columns)-6)

    return df;

def createDF(userList, verbose=True):
    # data = []
    # for handle in userList:
    #     try:
    #         user = preprocessor.getCFdata(handle)
    #         user.pop('Photo')
    #         user.pop('Levels')
    #         user.pop('Difficulties')
    #         data.append(user)
    #     except:
    #         if(verbose): print('User Not Found:', handle)
    #     else:
    #         if(verbose): print('User Found:', user['Handle'])
    #     finally:
    #         time.sleep(2)
    
    # df = pd.json_normalize(data).fillna(0)
    # df = pd.concat([df.iloc[:, :6], df[sorted(df.columns[6:])]], axis=1)

    # df = adjustDF(df)
    
    # df.to_csv('data.csv', index=False)
    df = pd.read_csv('data.csv')

    return df

def skillIndex(df, members):
    membersData = df.loc[df['Handle'].isin(members)]
    return membersData.iloc[:, 1:6].mean().sum() + membersData.iloc[:, 6:].max().sum()

def assemble(allUsersDF, df, teamCount, teamSize=3, n_iters = 250, verbose=True):
    teams = []
    maxScore = 0
    
    n = len(df)
    s_iters = 2 * n_iters // 5
    
    df['SkillIndex'] = df['Handle'].apply(lambda x: skillIndex(allUsersDF, [x]))
    topUsersDF = df.sort_values(by='SkillIndex', ascending=False).head(min(n, 2*teamSize*teamCount))

    for itr in range(n_iters):
        if(verbose): print('Running iter', itr+1, '/', n_iters)
        remUsersDF = topUsersDF if itr < s_iters else df
        
        medoids = remUsersDF.sample(teamCount)
        clusters = [[handle] for handle in medoids['Handle'].tolist()]
        remUsersDF = remUsersDF.loc[~remUsersDF['Handle'].isin(medoids['Handle'].tolist())]

        while any(len(cluster) < teamSize for cluster in clusters):
            if random.random() < 0.1: clusters = sorted(clusters, key=lambda x: skillIndex(allUsersDF, x), reverse=True)
            else: random.shuffle(clusters)

            for i, cluster in enumerate(clusters):
                requiredMembers = teamSize - len(cluster)
                if(requiredMembers < 1): continue
                r = random.randint(1, requiredMembers)

                for _ in range(r):
                    remUsersDF = remUsersDF.reset_index(drop=True)
                    bestRecruit = remUsersDF.iloc[remUsersDF.apply(lambda x: skillIndex(allUsersDF, cluster + [x['Handle']]), axis=1).idxmax()]
                    cluster.append(bestRecruit['Handle'])
                    remUsersDF = remUsersDF.loc[~remUsersDF['Handle'].isin([bestRecruit['Handle']])]

        score = sum(skillIndex(allUsersDF, cluster) for cluster in clusters)
        if score > maxScore:
            maxScore = score
            teams = clusters

    df = df.drop(columns='SkillIndex')
    remUsersDF = df.loc[~df['Handle'].isin([member for team in teams for member in team])]

    return teams, remUsersDF