class GrammarStats:
    def __init__(self):
        self.total_texts_checked = 0
        self.passed_text_count = 0

    def check(self, text):
       if not text:
        return False  # Return False for empty strings
       passed = text[0].isupper() and text[-1] in [".", "!", "?", "..."]
       if passed:
          self.passed_text_count += 1
       self.total_texts_checked += 1
       return passed
       
        

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_texts_checked == 0:
           return 0
        return int((self.passed_text_count / self.total_texts_checked) * 100 )
        
