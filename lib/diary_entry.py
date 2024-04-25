import math
class DiaryEntry:

    def __init__(self, title, contents) :
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents.")
        self.title = title
        self.contents = contents
        self.read_so_far = 0


    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
     
        if wpm == 0:
            raise Exception("cannot calculate reading time with wpm of 0")
        contents_word_count = len(self.contents.split())
        return math.ceil(contents_word_count / wpm)
    

    def reading_chunk(self, wpm, minutes):
        # chunk_end = min(self.read_so_far + words_user_can_read, len(words))
        words_user_can_read = wpm * minutes
        words = self.contents.split()
# Reset the reading position to the beginning if it exceeds the total number of words
        if self.read_so_far >= len(words):
            self.read_so_far = 0
# Calculate the start index for selecting the chunk of words
        chunk_start = self.read_so_far
# Calculate the end index for selecting the chunk of words
        chunk_end = self.read_so_far + words_user_can_read
 # Ensure that the end index does not exceed the length of the words list
        if chunk_end > len(words):
            chunk_end = len(words)
# Select the chunk of words
        chunk_words = words[chunk_start:chunk_end]
# Update the reading position for the next call
        self.read_so_far = chunk_end
        return " ".join(chunk_words)



    
        


