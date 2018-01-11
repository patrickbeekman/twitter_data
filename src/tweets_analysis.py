"""
General analysis of tweets from a file
"""


def main():
    the_word_love = count_word_occurrence('graysons_tweets.txt', 'love', True)
    print("Grayson tweeted/retweeted the word 'love' {} times".format(the_word_love))
    patrick_mentions = count_word_occurrence('graysons_tweets.txt', '@patrickbeekman')
    print("Grayson tweeted at or mentioned me @patrickbeekman {} times".format(patrick_mentions))


def count_word_occurrence(filename, word, check_RTs=True):
    """
    Counts the amount of times a word or phrase occurs in a file
    :param filename: The file to search through
    :param word: The word or phrase to search for
    :param check_RTs: A boolean to choose whether to look at the users retweets or not
    :return: The count of occurrences
    """
    file = open(filename)
    total_word_count = 0
    if not check_RTs:
        for line in file:
            if line[0:2] is not 'RT':
                total_word_count += line.count(word)
    else:
        for line in file:
            total_word_count += line.count(word)

    return total_word_count


if __name__ == "__main__":
    main()