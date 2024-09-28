#removing punctuation
import re
text = "Hurray! Today I am Learning Regex 1234"
cleaned_text = re.sub(r'[^\w\s\d+]','',text)
print(cleaned_text)