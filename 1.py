wordlist = input().split(' ')
wordfreq = [wordlist.count(p) for p in wordlist]
result = dict(sorted(dict(zip(wordlist,wordfreq)).items()))
print(result)
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.