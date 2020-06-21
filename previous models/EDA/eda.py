import random
from random import shuffle
random.seed(1)

def not_modify(word, answer):
	answer_list = answer.split(' ')
	if word in answer:
		return True
	for i in answer_list:
		if i in word:
			return True
	return False
########################################################################
# Random deletion
# Randomly delete words from the sentence with probability p
########################################################################

def random_deletion(words, p):

	#obviously, if there's only one word, don't delete it
	if len(words) == 1:
		return words

	#randomly delete words with probability p
	new_words = []
	for word in words:
		r = random.uniform(0, 1)
		if r > p:
			new_words.append(word)

	#if you end up deleting all words, just return a random word
	if len(new_words) == 0:
		rand_int = random.randint(0, len(words)-1)
		return [words[rand_int]]

	return new_words

def random_deletion_context(words, p, answer):

	answer_list = answer.split(' ')
	#obviously, if there's only one word, don't delete it
	if len(words) == 1:
		return words

	#randomly delete words with probability p
	new_words = []
	for word in words:
		r = random.uniform(0, 1)
		if r > p or not_modify(word, answer):
			new_words.append(word)

	#if you end up deleting all words, just return a random word
	if len(new_words) == 0:
		rand_int = random.randint(0, len(words)-1)
		return [words[rand_int]]

	#assert answer in ' '.join(new_words)

	return new_words

########################################################################
# Random swap
# Randomly swap two words in the sentence n times
########################################################################

def random_swap(words, n):
	new_words = words.copy()
	for _ in range(n):
		new_words = swap_word(new_words)
	return new_words

def swap_word(new_words):
	random_idx_1 = random.randint(0, len(new_words)-1)
	random_idx_2 = random_idx_1
	counter = 0
	while random_idx_2 == random_idx_1:
		random_idx_2 = random.randint(0, len(new_words)-1)
		counter += 1
		if counter > 3:
			return new_words
	new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
	return new_words

def random_swap_context(words, n, answer):
	new_words = words.copy()
	for _ in range(n):
		new_words = swap_word_context(new_words, answer)
	return new_words

def swap_word_context(new_words, answer):
	random_idx_1 = random.randint(0, len(new_words)-1)
	counter2 = 0
	while not_modify(new_words[random_idx_1], answer):
		random_idx_1 = random.randint(0, len(new_words)-1)
		counter2 += 1
		if counter2 > 10:
			return new_words
	random_idx_2 = random_idx_1
	counter = 0
	while random_idx_2 == random_idx_1 and not_modify(new_words[random_idx_2], answer):
		random_idx_2 = random.randint(0, len(new_words)-1)
		counter += 1
		if counter > 10:
			return new_words

	new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
	return new_words


########################################################################
# Random duplication
# Randomly duplicate n words into the sentence
########################################################################

def random_duplication(words, n, answer):
	new_words = words.copy()
	for _ in range(n):
		duplicate_word(new_words, answer)
	return new_words

def duplicate_word(new_words, answer):
	synonyms = []
	counter = 0

	random_word = new_words[random.randint(0, len(new_words)-1)]
	random_idx = random.randint(0, len(new_words)-1)
	if random_idx==0:
		new_words.insert(random_idx, random_word)
	elif random_idx==len(new_words)-1:
		new_words.insert(random_idx+1, random_word)
	else:
		if not not_modify(new_words[random_idx-1], answer) and not not_modify(new_words[random_idx+1], answer):
			new_words.insert(random_idx, random_word)

########################################################################
# main data augmentation function
########################################################################

def eda_question(sentence, alpha_rs=0.1):


	words = sentence.split(' ')
	if len(words)<=5:
		return sentence
	num_words = len(words)
	n_rs = max(1, int(alpha_rs*num_words))

	a_words = random_swap(words, n_rs)

	#a_words = random_deletion(a_words, p_rd)

	augmented_sentence = ' '.join(a_words)
	return augmented_sentence


def eda_context(sentence, answer, alpha_rs=0.05, alpha_rdu=0.05, p_rd=0.05):
	words = sentence.split(' ')
	num_words = len(words)
	n_rs = max(1, int(alpha_rs*num_words))
	n_rdu = max(1, int(alpha_rdu*num_words))

	a_words = random_swap_context(words, n_rs, answer)
	a_words = random_deletion_context(a_words, p_rd, answer)
	a_words = random_duplication(a_words, n_rdu, answer)

	augmented_sentence = ' '.join(a_words)
	return augmented_sentence
