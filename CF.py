import requests
import json
import operator

def getLevel(index):
    if index and index[0].isalpha(): return index[0].upper()
    else: return '0'

def user(handle):
    response = requests.get(f'https://codeforces.com/api/user.info?handles={handle}').json()
    if(response['status'] == 'OK'): info = response['result'][0]
    else: return None

    submissions = []
    solved = {}
    contests = set()

    response = requests.get(f'https://codeforces.com/api/user.status?handle={handle}').json()
    if(response['status'] == 'OK'): submissions = sorted(response['result'], key = operator.itemgetter('creationTimeSeconds'), reverse = True)

    for submission in submissions:
        problem = submission['problem']
        contestFlag = submission['author']['participantType'] == 'CONTESTANT'

        if('contestId' in problem):
            contest = problem['contestId']
            key = str(contest) + problem['index']

        if('verdict' in submission):
            if(submission['verdict'] == 'OK'):
                solved[key] = {
                'name': problem['name'],
                'level': getLevel(problem['index']),
                'difficulty': problem['rating'] if 'rating' in problem else 700,
                'submissionTime': submission['creationTimeSeconds'],
                'contestFlag': contestFlag,
                'tags': problem['tags']
                }
        
        if(contestFlag): contests.add(contest)

    return {
        'info': info,
        'solved': solved,
        'contests': contests
    }