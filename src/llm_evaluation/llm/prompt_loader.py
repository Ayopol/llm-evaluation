



def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(template, text):
    return template.replace("{text}", text)
