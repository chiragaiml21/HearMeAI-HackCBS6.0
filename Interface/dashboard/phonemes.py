from playsound import playsound

import nltk

d={
    "IY1":["eee.mpeg","Tongue is  High and close to the roof of the mouth and Lips Spread , also Tension is  Tense.","examples of words with this phoneme  are  ","beet","feet","meet","sheet","see","key","ski","believe","chief","achieve"],
    "IH1":["I.mpeg","Tongue is  High-mid and slightly forward in the mouth and Lips are Slightly relaxed and Tension: Slightly tense","examples of words with this phoneme  are ","sit","bit","ship","thick","lid","kid","this","him","with","miss","fish","sill","spill","grin","fill"],
    "EY1":["eh.mpeg","Tongue is  High-mid and slightly forward and Lips are Slightly spread and Tension is  Tense","examples of words with this phoneme  are ","pen","bet","met","set","pet","bell","tell","red","wet","best","end","men","dress","bless","chef","head","friend","said","again","break"],
    "EH1":["eh.mpeg","Tongue is  Mid and slightly forward and Lips are  Slightly relaxed and Tension is Relaxed","examples of words with this phoneme  are ","red", "pen", "bed", "bell", "said", "wet", "pet", "head", "get", "chef"],
    "AE1":["ae.mpeg","Tongue is  Low and front Lips are Relaxed and Tension is  Relaxed","examples of words with this phoneme  are ","cat", "man", "bat", "hat", "sand", "map", "crab", "plan", "apple", "black"],
    "AA1":["aaa.mpeg","Tongue is Low and back and Lips are Relaxed and Tension is Relaxed","examples of words with this phoneme  are ","father," "barn," "car," "start," "far," "large," "guard," "hard," "par," "charming"],
    "AO1":["walk.mpeg","Tongue is Mid-back and slightly rounded and Lips are Rounded and Tension Tense","examples of words with this phoneme are","thought", "caught", "walk", "talk", "law", "ball", "fall", "small", "chalk", "thoughtful"],
    "OW1":["walk.mpeg","Tongue is High-mid and back also Lips are Rounded and Tension is Tense","examples of words with this phoneme  are ", "coat," "so," "go," "no," "throw," "show," "below," "yellow," "hello"],
    "UH1":["uh.mpeg","Tongue is High-mid and back also Lips are slightly Rounded and Tension is Tense.","examples of words with this phoneme are","book", "good", "put", "wood", "should", "could", "woman", "push", "butcher", "full"],
    "UW1":["uu.mpeg","Tongue is High and back also Lips are Rounded and Tension is Tense","examples of words with this phoneme are","blue," "shoe," "true," "crew," "fruit," "rude," "mood," "cruise," "flute," "brutal"],
    "AY1":["ai.mpeg","Tongue is High-mid and gliding from a front position to a glide towards the back and Lips are Slightly spread and Tension is Tense","examples of words with this phoneme are","buy," "high," "pie," "sky," "cry," "myth," "fly," "drive," "light," "thigh"],
    "AW1":["ao.mpeg","Tongue is High-mid and gliding from a front position to a glide towards the back and Lips are Rounded and Tension is Tense","house," "cloud," "mouse," "out," "about," "doubt," "shout," "south," "loud," "pout"],
    "EY1":["cake.mpeg","Tongue is High-mid and gliding from a slightly forward position to a glide towards the back and Lips are Slightly spread and Tension is Tense","examples of words with this phoneme are","cake", "great", "make", "break", "stake", "brace", "ate", "lake", "bake", "snake"],
    "OY1":["ocoin.mpeg","Tongue is Mid-back and gliding from a front position to a glide towards the back and Lips are Rounded and Tension is Tense","examples of words with this phoneme are","boy," "toy," "enjoy," "coin," "voice," "moist," "choice," "noise," "destroy," "employ"],
    "OW1":["sofa.mpeg","Tongue is  Mid-central and Lips are Neutral and Tension is Relaxed","examples of words with this phoneme are","sofa", "banana", "happen", "mother", "another", "problem", "teacher", "computer", "doctor", "visitor"],
    "ER1":["abird.mpeg","Tongue is Rhotic vowel, tongue may be bunched or curved back and Lips are Neutral and Tension is Tense","examples of words with this phoneme are","bird","heard","word","world","girl","curb","serve","learn","burn","first"],
    "ER0":["rr.mpeg","pronounced with the tip of the tongue curled up towards the hard palate and Lips are Neutral and Tension is Tense","examples of words with this phoneme are","teacher", "sister", "labor", "honor", "guitar", "forever", "doctor", "chore", "border", "adore"],
    "AH1":["cup.mpeg","Tongue is in a mid-central position and lips are relaxed","examples of words with this phoneme are","cup","luck","butter","duck","cut","up","but","under","cousin","shut"],
    "AH0":["sofa.mpeg","Tongue is mid central and lips are neutral","examples of words with this phoneme are","sofa", "banana", "so", "under", "enjoy", "problem", "computer", "attention", "celebrate", "together"],


    "P":["p.mpeg","The lips come together to block the airflow, and then they release","examples of words with this phoneme are","pat", "pen", "apple", "stop", "happy", "people", "jump", "cup", "hope", "purple"],
    "T":["t.mpeg","The tongue tip touches the alveolar ridge (just behind the upper front teeth), blocking the airflow, and then releases","examples of words with this phoneme are","cat", "table", "water", "hat", "butter", "computer", "letter", "guitar", "wait", "matter"],
    "K":["kk.mpeg","The back of the tongue contacts the soft palate (velum), blocking the airflow, and then releases","examples of words with this phoneme are","cat", "kite", "cookie", "computer", "back", "kangaroo", "black", "key", "kettle", "crack"],
    "R":["rr.mpeg","The tongue tip curls back and touches the retroflex ridge (a bit farther back in the mouth), blocking the airflow, and then releases","examples of words with this phoneme are","start", "cart", "part", "tart", "smart"],
    "HH":["h.mpeg","The vocal cords are relaxed, and air passes through a narrow constriction in the glottis","examples of words with this phoneme are","hat", "house", "happy", "hello", "high", "help", "hope", "honor", "holiday", "hard"],
    "B":["b.mpeg","The lips come together to block the airflow, and then they release with vibration of the vocal cords ","examples of words with this phoneme are","bat", "ball", "book", "butter", "rabbit", "table", "bubble", "able", "big", "web"],
    "D":["d.mpeg","The tongue tip touches the alveolar ridge (just behind the upper front teeth), blocking the airflow, and then releases but with voicing","examples of words with this phoneme are","dog", "desk", "dance", "doctor", "sudden", "addition", "bed", "bad", "ride", "ladder"],
    "G":["g.mpeg","The back of the tongue contacts the soft palate (velum), blocking the airflow, and then releases but with voicing","examples of words with this phoneme are","dog", "big", "goat", "good", "game", "get", "argue", "begin", "give", "mug"],
    "F":["f.mpeg"," The bottom lip lightly touches the upper teeth while airflow is constricted","examples of words with this phoneme are","fish", "funny", "family", "office", "coffee", "elephant", "free", "phone", "surf", "buffet"],
    "TH":["th.mpeg","The tip of the tongue lightly touches the upper front teeth while airflow is constricted","examples of words with this phoneme are","thin", "math", "teeth", "bath", "clothes", "moth", "ether", "path", "tooth", "leather"],
    "S":["s.mpeg","Air flows through a narrow gap between the tongue and alveolar ridge", "sit", "song", "rose", "class", "moss", "bus", "glass", "miss", "pass", "wasp"],
    "SH":["sh.mpeg","Air flows through a narrow gap between the tongue and alveolar ridge but with a slightly different tongue position","examples of words with this phoneme are","shoe", "she", "sure", "fish", "mission", "ash", "pressure", "wish", "fashion", "caution"],
    "CH":["ch.mpeg","The tongue approaches the hard palate without touching it","examples of words with this phoneme are","cheese","cheer","teach","chill","beach","rich","speech","watch","teacher","march"],
    "V":["v.mpeg","The bottom lip lightly touches the upper teeth while airflow is constricted","examples of words with this phoneme are","vase", "venture", "over", "love", "voice", "never", "river", "serve", "very", "favorite"],
    "DH":["dh.mpeg"," The tip of the tongue lightly touches the upper front teeth while airflow is constricted but with voicing","examples of words with this phoneme are","this," "that," "the," "there," "feather," "father," "brother," "clothe," "bathe," "breathe"],
    "Z":["zz.mpeg","Air flows through a narrow gap between the tongue and alveolar ridge but with voicing","examples of words with this phoneme are","zebra", "zero", "zeppelin", "zest", "zigzag", "zipper", "zodiac"],
    "JH":["job.mpeg","start with the front part of your tongue against the alveolar ridge and The tip of your tongue should be pressed against the alveolar ridge ","examples of words with this phoneme are","judge," "adjust," "giant," "badge," "dodge," "edge," "lodge," "pledge," "wedge," "fudge"],
    "M":["mm.mpeg","The lips are close, allowing air to flow through the nasal passage","examples of words with this phoneme are","mom","hammer","drama","summit","clam","glimmer","jam","comma"],
    "N":["nn.mpeg","The tongue tip contacts the alveolar ridge, allowing air to flow through the nasal passage","examples of words with this phoneme are","and", "banana", "onion", "knock", "dentist", "function", "invent", "antenna", "noodle", "annual"],
    "NG":["in.mpeg","The back of the tongue contacts the velum, allowing air to flow through the nasal passage","examples of words with this phoneme are","running","jumping","swimming","laughing","singing","dancing","eating","working","reading","sleeping"],
    "W":["v.mpeg","The bottom lip lightly touches the upper teeth while airflow is constricted","examples of words with this phoneme are","vase", "venture", "over", "love", "voice", "never", "river", "serve", "very", "favorite"]
}
# Download the CMU Pronouncing Dictionary data (if not already downloaded)
# nltk.download('cmudict')

from nltk.corpus import cmudict

# Initialize the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Faunction to segment a sentence into phonemes along with corresponding letters
def segment_sentence_to_phonemes(sentence):
    words = nltk.word_tokenize(sentence.lower())  # Tokenize and convert to lowercase
    phoneme_sequence = []

    for word in words:
        # Get the phoneme transcription for each word (if available)
        if word in pronouncing_dict:
            phonemes = pronouncing_dict[word][0]
            for i in range(len(word)):
                phoneme_sequence.append((word[i], phonemes[i] if i < len(phonemes) else ""))
        else:
            # If the word is not in the dictionary, just use the word itself
            phoneme_sequence.extend([(char, char) for char in word])

    return phoneme_sequence

# Input sentence
# sentence = input("enter")


# import pyttsx3
# voiceEngine = pyttsx3.init()
 
# rate = voiceEngine.getProperty('rate')
# volume = voiceEngine.getProperty('volume')
# voice = voiceEngine.getProperty('voice')
 
# print rate
# print volume
# print voice
 
# newVoiceRate = 1

# voiceEngine.setProperty('rate', newVoiceRate)
# voiceEngine.say(sentence)
# voiceEngine.runAndWait()
   

# # for hearing impairment
# newVolume = 1

# voiceEngine.setProperty('volume', newVolume)
# # voiceEngine.say('Testing different voice volumes.')
# voiceEngine.runAndWait()


# Perform phoneme segmentation
# phonemes = segment_sentence_to_phonemes(sentence)
# print(phonemes)
# print(type(phonemes))

# # Print the segmented output along with letters that generate each phoneme
# print("Input Sentence:", sentence)
# for letter, phoneme in phonemes:
#     print(f"Letter: {letter}, Phoneme: {phoneme}")


    # --------------------------------

# for letter , phoneme in phonemes:
#     for i in d:
#         if phoneme == i:
#             audio=d[i][0]
#             playsound(audio)