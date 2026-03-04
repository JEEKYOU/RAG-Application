import re

MAX_TOKENS = 800
OVERLAP = 100

def chunk_markdown(text):
    sections = re.split(r'\n## ', text)
    chunks = []

    for section in sections:
        paragraphs = section.split("\n\n")
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) < MAX_TOKENS:
                current_chunk += "\n\n" + para
            else:
                chunks.append(current_chunk.strip())
                current_chunk = para

        if current_chunk:
            chunks.append(current_chunk.strip())

    return chunks
