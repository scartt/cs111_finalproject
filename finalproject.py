#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:50:22 2019

@author: scarlett
"""
# final project

import math

# an initial text model

# Part I -- 3 helper function 
def clean_text(txt):
    """ clean each character """
    text = ''
    for i in txt:
        if i not in '?!,.:':
            text += i
    return text.lower().split(' ')

# Part III -- helper function for self.num_punctuation
def clean_punctuations(txt):
    """ left with only punctuations """
    text = ''
    for i in txt:
        if i in '?!,.:' or '""':
            text += i
    return text.split(' ')
            
# Part III -- helper function for self.stems            
def stem(s):
    """ accepts a string as a parameter.
    """
    if s[-3:] == 'ing' and len(s) > 4:
        if s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
            
    elif s[-2:] == 'er':
        s = s[:-2]
        
    elif s[-1] == 's':
        if s[-2] == 's':
            s = s[:]
        elif s[-2] == 'e':
            if s[-3] == 's':
                s = s[:-1]
            else:
                s = s[:]
        else:
            s = s[:-1]
            
    elif s[-3:] == 'ies':
        s = s[:-3] + 'y'
    elif s[-1] == 'e':
        s = s[:-1]
    elif s[-2:] == 'ly':
        s = s[:-2]
    elif s[-2:] == 'ed':
        s = s[:-2]
        
    return s

# the body of the class
class TextModel:
# Part I -- 1
    def __init__(self, model_name):
        """ construct a new TextModel object """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.num_punctuations = {}

# Part I -- 2        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.num_punctuations)) + '\n'
        
        return s

# Part I -- 4
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """
    # self.num_punctuation
        self.num_punctuations = {}
        mark_list = clean_punctuations(s)

        for i in mark_list:
            if i in self.num_punctuations:
                self.num_punctuations[i] += 1
            else:
                self.num_punctuations[i] = 1


    # self.sentence_lengths
        self.sentence_lengths = {}
        sen = s
        sen = s.replace('!', '.')
        sen = s.replace('?', '.')
        sen = s.replace(',', '.')
        sentence_list = sen.split('. ')
        
        for i in sentence_list:
            word_list = clean_text(i)
            sentence_lengths = len(word_list)
            
            if sentence_lengths in self.sentence_lengths:
                self.sentence_lengths[sentence_lengths] += 1
            else:
                self.sentence_lengths[sentence_lengths] = 1
                
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        
    # self.words
        self.words = {}
        word_list = clean_text(s)
        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
                
        # Add code to update other feature dictionaries.
    # self.word_lengths
        self.word_lengths = {}
        for i in word_list:
            word_length = len(i)
            if word_length in self.word_lengths:
                self.word_lengths[word_length] += 1
            else:
                self.word_lengths[word_length] = 1
                
    # self.stems
        self.stems = {}
        for s in range(len(word_list)):
            word_stem = stem(word_list[s])
            
            if word_stem in self.stems:
                self.stems[word_stem] += 1
            else:
                self.stems[word_stem] = 1

        
                
                
# Part I -- 5
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)
 

# Part II        
# defines a small dictionary and saves it to a file       
    def save_model(self):
        """ saves the TextModel object self by writing its various feature 
        dictionaries to files
        """
        f1 = open(self.name + '_' + 'words', 'w')
        f1.write(str(self.words))
        f1.close()
        

        f2 = open(self.name + '_' + 'word_lengths', 'w')
        f2.write(str(self.word_lengths))
        f2.close()
        
        f3 = open(self.name + '_' + 'stems', 'w')
        f3.write(str(self.stems))
        f3.close()
        
        f4 = open(self.name + '_' + 'sentence_lengths', 'w')
        f4.write(str(self.sentence_lengths))
        f4.close()
        
        f5 = open(self.name + '_' + 'num_punctuations', 'w')
        f5.write(str(self.num_punctuations))
        f5.close()

# Part II  
# read the dictionary and assign to different dictioaries   
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object 
        and assigns them to the attributes of the called TextModel.
        """
        f1 = open(self.name + '_' + 'words', 'r')
        d1_str = f1.read()
        f1.close()
        
        self.words = dict(eval(d1_str))
        
        print("Inside the newly-read dictionary, d1, we have:")
        print(self.words)
        
        f2 = open(self.name + '_' + 'word_lengths', 'r')
        d2_str = f2.read()
        f2.close()
        
        self.word_lengths = dict(eval(d2_str))
        
        print("Inside the newly-read dictionary, d1, we have:")
        print(self.word_lengths)
        
        f3 = open(self.name + '_' + 'stems', 'r')
        d3_str = f3.read()
        f3.close()
        
        self.stems = dict(eval(d3_str))
        
        f4 = open(self.name + '_' + 'sentence_lengths', 'r')
        d4_str = f4.read()
        f4.close()
        
        self.sentence_lengths = dict(eval(d4_str))
        
        f5 = open(self.name + '_' + 'num_punctuations', 'r')
        d5_str = f5.read()
        f5.close()
        
        self.num_punctuations = dict(eval(d5_str))
        
        
    # Part IV - 2
    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores 
        measuring the similarity of self and other
        """
        word_score = compare_dictionaries(other.words, self.words)
        
        wordlen_score = compare_dictionaries(other.word_lengths, 
                                             self.word_lengths)
        
        senlen_score = compare_dictionaries(other.sentence_lengths, 
                                             self.sentence_lengths)
        
        wordpunc_score = compare_dictionaries(other.num_punctuations, 
                                              self.num_punctuations)
        
        wordstem_score = compare_dictionaries(other.stems, self.stems)
        
        return [word_score, wordlen_score, wordstem_score, senlen_score,  
                wordpunc_score]
    
    # Part IV -- 3
    def classify(self, source1, source2):
        """ compares the called TextModel to two other “source” TextModel objects 
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print('scores for source1: ', scores1)
        print('scores for source2: ', scores2)
        
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] 
        + 5*scores1[3] + 5*scores1[4]
        
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2]
        + 5*scores2[3] + 5*scores2[4]
    
        if weighted_sum1 > weighted_sum2:
            print(self.name + ' is more likely to come from ' + source1.name)
        else:
            print(self.name + ' is more likely to come from ' + source2.name)

# Part IV
def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs and return their 
    log similarity score """
    score = 0
    
    sum_d1 = sum(d1.values())
    
    for i in d2:
        if i in d1:
            score += math.log(d1[i] / sum_d1) * d2[i]
        else:
            score += math.log(0.5 / sum_d1) * d2[i]
        
    return score


# Part IV -- test function
def test():
    """ test two sources to see which source is more similair to the new source """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
def run_tests():
    """ test two texts to see which one is similiar to new text """
    source1 = TextModel('Wall Street Journal')
    source1.add_file('WSJ.txt')

    source2 = TextModel('New York Times')
    source2.add_file('NYT.txt')

    new1 = TextModel('Boston Globe')
    new1.add_file('BG.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('The Economist')
    new2.add_file('E.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('China Daily')
    new3.add_file('CD.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('BBC News')
    new4.add_file('BBC.txt')
    new4.classify(source1, source2)