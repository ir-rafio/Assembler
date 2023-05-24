import requests
import json
import time
import CF

now = time.time()

def getCFdata(CFhandle):
	user = CF.user(CFhandle)
	if(user == None): return None

	recent = 0
	levels = {}
	difficulties = {}
	tags = {}

	for problem in user['solved'].values():
		level = problem['level']
		difficulty = problem['difficulty']
		submissionTime = problem['submissionTime']
		
		point = difficulty*difficulty/1e6
		if problem['contestFlag']: point *= 1.5

		levels[level] = levels[level] + 1 if level in levels else 1
		difficulties[difficulty] = difficulties[difficulty] + 1 if difficulty in difficulties else 1
		if now-submissionTime < 30*86400: recent += point
		for tag in problem['tags']: tags[tag] = tags[tag] + point if tag in tags else point

	data = {
		'Handle': user['info']['handle'],
		'Photo': user['info']['titlePhoto'] if 'titlePhoto' in user['info'] else None,
		'Max Rating': user['info']['maxRating'] if 'maxRating' in user['info'] else 0,
		'Rating': user['info']['rating'] if 'rating' in user['info'] else 0,
		'Solve Count': len(user['solved']),
		'Contest Count': len(user['contests']),
		'Recent Activity Point': recent,
		'Levels': dict(sorted(levels.items())),
		'Difficulties': dict(sorted(difficulties.items())),
		'Tags': dict(sorted(tags.items(), key=lambda x: x[1], reverse=True))
	}

	return data