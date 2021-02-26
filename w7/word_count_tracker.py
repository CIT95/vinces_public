#This data dictionary will log the amount of words I typed for various fanfiction
#projects, I worked on for the week of 1/10 - 1/16 of this year.

import statistics #To gain access to the mean


def average: #I need to establish an average of word count typed each day
    word_count_list = []
    for index in sorted_word_count_dd_list:
        word_count_list.append(index[1])

#My average = total word count / number of days
    average_word_count = sum(word_count_list) / len(days_list)

    print('The average word count written per day is \ {average_word_count}.')

def total(): #Total number of days I worked on fanfiction
    days_list = []
    for index in sorted_word_count_dd_list:
        days_list.append(index[1])

    print('The total number of days in which I worked on fanfiction is \ {sum(days_list)}.') 

word_count_list = {
    '1/10', 'Word Count': 2000
    '1/11', 'Word Count': 500
    '1/12', 'Word Count': 0
    '1/13', 'Word Count': 0
    '1/14', 'Word Count': 300
    '1/15', 'Word Count': 2500
    '1/16', 'Word Count': 2700 
}
sorted_word_count_dd_list = sorted(word_count_list.items(), key=lambda x: x[1], reverse=True)
#This should sort the word count list in descending order, thanks for the link, it really helped!

print('The days in which I worked the most on my fanfiction are:')
for index in sorted_word_count_dd_list:
    print(index [0], index[1])

minimum = min(item['Word Count'] for item in word_count_list)
print('The minimum amount in the word count data dictionary is:')
print(minimum)

maximum = max(item['Word Count'] for item in word_count_list)
print('The maximum amount in the word count data dictionary is:')
print(maximum)

total = sum(item['Word Count'] for item in word_count_list)
print('The combined total word count in the data dictionary is:')
print(total)

average = statistics.mean(item['Word Count'] for item in word_count_list) #Again, statistics was imported for acces to mean
print('The average word count in the data dictionary is:')
print(average)