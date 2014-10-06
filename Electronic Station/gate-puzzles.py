__author__ = 'Pavel.Malko'
def find_word(message):
    """
- Letter case does not matter ("A" == "a");
- If the first letters of the words are equal, then add 10%;
- If the last letters of the words are equal, then add 10%;
- Add length comparison as
(length_of_word1 / length_of_word2) * 30%, if length_of_word1 ≤ length_of_word2;
, else (length_of_word2 / length_of_word1) * 30%
- Take all unique letters from the both words in one set and count how many letters appear in the both words. Add to the coefficient (common_letter_number / unique_letters_numbers) * 50;
    """

    words = [word.strip('.,').lower() for word in message.split()]
    likeness, maxLikenes, likenes = {}, 0, ''
    for word1 in words:
        likeness[word1] = -100
        for word2 in words:
            if word1[0] == word2[0]: likeness[word1] += 10
            if word1[-1] == word2[-1]: likeness[word1] += 10
            likeness[word1] += min(len(word1), len(word2)) / max(len(word1), len(word2)) * 30
            likeness[word1] += len(set(word1) & set(word2)) / len(set(word1 + word2)) * 50
        likeness[word1] /= len(words) - 1
        maxLikenes = likeness[word1] if likeness[word1] > maxLikenes else maxLikenes
        likenes = word1 if likeness[word1] == maxLikenes else likenes
    return likenes

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # find_word("Friend Fred and friend Ted.")
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"