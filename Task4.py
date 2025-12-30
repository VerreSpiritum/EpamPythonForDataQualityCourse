import random
import string
import re

def generate_random_dicts(min_dicts=2, max_dicts=10):
    dict_list = []
    for _ in range(random.randint(min_dicts, max_dicts)):
        key_count = random.randint(1, 5)
        keys = random.sample(string.ascii_lowercase, key_count)
        d = {key: random.randint(0, 100) for key in keys}
        dict_list.append(d)
    return dict_list


def merge_dicts_with_max_values(dict_list):
    tracker = {}
    # Track max values and the index of the dict they came from
    for idx, d in enumerate(dict_list, start=1):
        for key, value in d.items():
            if key not in tracker or value > tracker[key][0]:
                tracker[key] = (value, idx)

    result = {}
    for key, (value, idx) in tracker.items():
        # Count occurrences to decide if renaming is necessary
        count = sum(1 for d in dict_list if key in d)
        if count > 1:
            result[f"{key}_{idx}"] = value
        else:
            result[key] = value
    return result


def normalize_and_fix_text(input_text):
    # 1. Fix "iz" using word boundaries (case-insensitive)
    processed_text = re.sub(r'\biz\b', 'is', input_text, flags=re.IGNORECASE)

    # 2. Split into sentences and normalize each
    # Regex splits by sentence endings followed by whitespace
    raw_sentences = re.split(r'(?<=[.!?:\s])\s+', processed_text.strip())

    normalized_sentences = []
    last_words = []

    for sentence in raw_sentences:
        clean_s = sentence.strip().lower()
        if clean_s:
            # Capitalize first letter only
            clean_s = clean_s[0].upper() + clean_s[1:]
            normalized_sentences.append(clean_s)

            # Identify the last word (ignoring punctuation)
            words = re.findall(r'\b\w+\b', clean_s)
            if words:
                last_words.append(words[-1])

    # 3. Create the summary sentence
    if last_words:
        summary = " ".join(last_words).capitalize() + "."
        normalized_sentences.append(summary)

    return " ".join(normalized_sentences)


def count_all_whitespaces(text):
    return len(re.findall(r'\s', text))

# Task 2 execution
my_dicts = generate_random_dicts()
merged_result = merge_dicts_with_max_values(my_dicts)

print("Generated Dicts:", my_dicts)
print("Merged Result:", merged_result)

#Task 3 execution
temp_var = ('homEwork:'
            '  tHis iz your homeWork, copy these Text to variable.'
            '  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.'
            '  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.'
            '  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
            )

final_text = normalize_and_fix_text(temp_var)
ws_count = count_all_whitespaces(final_text)

print(f"Final Text:\n{final_text}")
print(f"\nNumber of whitespace characters: {ws_count}")