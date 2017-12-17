import pandas as pd
import numpy as np

current_word = None
current_count = 0
word = None
book = open('mushrooms1.csv')
lines = book.readlines()
lines1 = []

count1 = []
word1 = []
# input comes from STDIN
for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
    lines1.append(line)
    words = line.split(',')
    for word in words:
        count = 1
        count1.append(count)
        word1.append(word)
    #word1 = np.array(word1, dtype=None)
    #count1 = np.array(count1, dtype=np.int8)

    # parse the input we got from mapper.py
    #word, count = line.split(',', 1)
#print(lines1[0])
#word1 = np.array(word1,dtype=None)
#count1 = np.array(count1,dtype=np.int8)
#count_word = np.ones((word1.shape[0],))
#word1 = np.reshape(word1,)
#output_map = np.concatenate((word1, count_word), axis=1)
#print(count_word.shape,word1.shape)
count1 = np.array(count1,dtype=np.int8)
worda1 = np.array(word1,dtype=None)
output_map = np.stack((worda1, count1.T), axis=1)
print(output_map)


df = pd.DataFrame(data=output_map,columns=['word','count'])
df = df.sort_values('word')
#df.to_csv('output_map.csv')

word_new = None
count_new = 0
word_reduce = []
count_reduce = []
for row in df.itertuples():
    #row[0] = int(row[0])
    iteration_count = int(getattr(row, "count"))
    if word_new == getattr(row, "word"):
        count_new += iteration_count
    else:
        word_reduce.append(word_new)
        count_reduce.append(count_new)
        word_new = getattr(row, "word")
        count_new = iteration_count
#print(word_reduce,count_reduce)
count_reduce = np.array(count_reduce,dtype=np.int8)
word_reduce = np.array(word_reduce,dtype=None)
output_reduce = np.stack((word_reduce, count_reduce.T), axis=1)
print(output_reduce)