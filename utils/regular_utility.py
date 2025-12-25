
class Regular:

    def text_spliting(self,text):
        actual_text = text.split("$")[1].strip()
        return actual_text