import json


def pack(text):
    return json.dumps({'text': text})


def unpack(obj):
    if isinstance(obj, str):
        return obj
    if isinstance(obj, list):
        return "".join(unpack(e) for e in obj)
    if isinstance(obj, dict):
        text = ""
        if "translate" in obj:
            text += obj["translate"]
            if "with" in obj:
                args = u", ".join(unpack(e) for e in obj["with"])
                text += u"{%s}" % args
        if "text" in obj:
            text += obj["text"]
        if "extra" in obj:
            text += unpack(obj["extra"])
        return text
    raise ValueError(obj)