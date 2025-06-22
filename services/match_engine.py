def is_remix(original_title, candidate_title):
    original = original_title.lower()
    candidate = candidate_title.lower()
    keywords = ["remix", "edit", "rework", "version", "bootleg", "vip", "mix"]

    if any(kw in candidate for kw in keywords) and original.split()[0] in candidate:
        return True
    return False
