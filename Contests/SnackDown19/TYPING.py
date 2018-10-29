# Rejected

def score(word, occur):
    same = change = 0
    for i in range(1, len(word)):
        if (word[i - 1] in L and word[i] in L) or (word[i - 1] in R and word[i] in R):
            same += 1
        else:
            change += 1
    sscore = (0.2 + same * 0.4 + change * 0.2)
    total = sscore + (occur - 1) * sscore / 2
    return total


def word_count(str):
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


t = int(input())
while t > 0:
    num = int(input())
    words = [0] * num
    L = ['d', 'f']
    R = ['j', 'k']
    time = 0
    counts = dict()
    for i in range(num):
        words[i] = str(input())
    word_count(words)
    for i in counts.keys():
        occur = counts.get(i)
        time += (score(i, occur))
    time=time*10
    print('%.0f'%time)
    t -= 1
