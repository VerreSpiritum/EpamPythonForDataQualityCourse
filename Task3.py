import re

temp_var = ('homEwork:'
            '  tHis iz your homeWork, copy these Text to variable.'
            '  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.'
            '  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.'
            '  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
            )

# 1. Standardize "iz" -> "is" first (case-insensitive)
# We do this early to ensure the logic "only when it is a mistake" is handled by word boundaries
temp_var = re.sub(r'\biz\b', 'is', temp_var, flags=re.IGNORECASE)

# 2. Split into sentences while keeping delimiters
# This regex looks for punctuation followed by whitespace or start of string
sentence_list = re.split(r'(?<=[.!?:\s])\s+', temp_var.strip())

normalized_sentences = []
last_words = []

for sentence in sentence_list:
    # Clean up the sentence: lowercase everything, then capitalize first letter
    clean_s = sentence.strip().lower()
    if clean_s:
        # Capitalize the first letter of the sentence
        clean_s = clean_s[0].upper() + clean_s[1:]
        normalized_sentences.append(clean_s)

        # Extract the last word (ignoring trailing punctuation)
        words = re.findall(r'\b\w+\b', clean_s)
        if words:
            last_words.append(words[-1])

# 3. Create and append the new sentence
summary_sentence = " ".join(last_words).capitalize() + "."
normalized_sentences.append(summary_sentence)

# 4. Join and calculate whitespaces
final_text = " ".join(normalized_sentences)
whitespace_count = len(re.findall(r'\s', final_text))

print(f"Final Text:\n{final_text}")
print(f"\nNumber of whitespace characters: {whitespace_count}")