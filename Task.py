#!/usr/bin/env python
# coding: utf-8

# In[160]:


#### Define class and the functionality
class Task(object):
    def strongPasswordCheck(self, password):
        n = len(password) ### Find the length of the password

        # a flag to keep note if the password has upper case, lower and digits
        contains_upper = 0
        contains_lower = 0
        contains_digit = 0
        contains_common_word = 0

        #### REad the common word file and split the file by '/n' to get it as a set
        set_of_words = {elt.strip() for elt in open("../data/common-passwords.txt", "r").readlines()}
        
        #### Check if any of the common words i present in the list and get the count stored
        for word in set_of_words:
            contains_common_word = contains_common_word + password.count(word)

        ### Check if the password has those values and change the flag
        for c in password:
            if not contains_upper and c.isupper():
                contains_upper = 1
            if not contains_lower and c.islower():
                contains_lower = 1
            if not contains_digit and c.isdigit():
                contains_digit = 1

        ##### The number of character swaps needed if those types of char is not present
        char_swaps =  3 - contains_upper - contains_lower - contains_digit

        # check for the repeating char in order to replace
        i = 0 ### Pointer 1
        j = 1 ### Pointer 2
        reps = []

        while i < n:
            while j < n and password[i] == password[j]:
                j += 1 #### Keep incrementing 'j' when you find a repeating character
            reps.append(j-i)
            #### Swap the values of i, j and increament the j pointer by 1
            i = j
            j = j + 1

        ##### For example, the password : "a12111" will have reps = [1, 1, 1, 3]


        # To handle the different criteria
        if n < 7:
            adds = 7 - n ### Number of insertions to be made in general
            #### For n < 7 the result is simple maximum between the number of insertions and swaps for characters
            
            return max(adds, char_swaps)
    

        elif n <= 25:
            #### For n >= 7 and <=25 its the maximum between the repetition swaps and swaps for characters
            rep_swaps = sum([val // 3 for val in reps])
            
            #### If the password has a common word then that has to be swapped as well along with repetitions 
            if not contains_common_word:
                return max(char_swaps, rep_swaps)
            else:
                return max(char_swaps, rep_swaps + contains_common_word)
        else:
            #### Find the number of deletions to be done which is affected by the presence of common word in it
            deletions = n - 25 - contains_common_word
            r = len(reps)

            ##### Loop to check if we delete one chracter and number of repetition gets reduced by 1
            for i in range(r):
                if deletions >= 1 and reps[i] % 3 == 0:
                    reps[i] = reps[i] - 1
                    deletions = deletions - 1
            ##### Check if we need to now do 2 delete to break a repetition
            for i in range(r):
                if deletions >= 2 and reps[i] % 3 == 1 and reps[i] > 3:
                    reps[i] = reps[i] - 2
                    deletions = deletions - 2

            ##### For rest of the cases like %3 == 2 remove if possible and there is enough deletion left
            for i in range(r):
                if deletions > 0 and reps[i] > 2:
                    remv = min(deletions, reps[i] - 2)
                    reps[i] = reps[i] - remv
                    deletions = deletions - remv
            ### Number of repeat char that needs to be taken care of by swapping since no more deletion can be done
            rep_swaps = sum([val // 3 for val in reps])
            return max(char_swaps, rep_swaps) + (n - 25)


# In[161]:


#### Test case 1

obj = Task()
obj.strongPasswordCheck("aaa11")


# In[162]:


#### Test case 1

obj = Task()
obj.strongPasswordCheck("a111")


# In[163]:


#### Test case 2
obj = Task()
obj.strongPasswordCheck("a1122332a11")


# In[164]:


#### Test case 3
obj = Task()
obj.strongPasswordCheck("a12111")


# In[165]:


#### Test case 4
obj = Task()
obj.strongPasswordCheck("a12ad1112233iascd33fsef213123111")


# In[166]:


#### Test case 5
obj = Task()
obj.strongPasswordCheck("a12ad1112233iasAd33fsef213123111")


# In[167]:


#### Test case 6
obj = Task()
obj.strongPasswordCheck("a12111fheufheiascdaafsef21312311")


# In[168]:


#### Test case 7
obj = Task()
obj.strongPasswordCheck("112233")


# In[169]:


#### Test case 8
obj = Task()
obj.strongPasswordCheck("dubsmash")


# In[170]:


#### Test case 9
obj = Task()
obj.strongPasswordCheck("dubsmash1")


# In[171]:


#### Test case 10
obj = Task()
obj.strongPasswordCheck("aAsdD2a11")


# In[172]:


#### Test case 11
obj = Task()
obj.strongPasswordCheck("Aa13")


# In[173]:


#### Test case 12
obj = Task()
obj.strongPasswordCheck("aaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbssssssssssssssss")


# In[174]:


#### Test case 13
obj = Task()
obj.strongPasswordCheck("a12141fheufheiascdaafsef21312311")


# In[175]:


#### Test case 14
obj = Task()
obj.strongPasswordCheck("a12141fheufhAiascdaafsef22212311")


# In[ ]:





# In[ ]:




