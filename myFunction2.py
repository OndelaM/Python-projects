def replace(sentence):
    sentence_list = sentence.split()
    for counter, word in enumerate(sentence_list):
        if counter % 2 == 0:
            sentence_list[counter] = "Hello"
    new_sentence = " ".join(sentence_list)   
    print(new_sentence)

replace(input("Enter a sentence: "))