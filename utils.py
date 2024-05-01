import difflib as dl
import re


def get_pred(gt_file, pred_file_list):
    gt_name = gt_file.split(".")[0]
    pred_file = [
        file for file in pred_file_list if re.match(rf"{gt_name}_.*.txt", file)
    ]
    return pred_file[0]


def text_diff(text1, text2):
    matcher = dl.SequenceMatcher(None, text1, text2)
    opcodes = matcher.get_opcodes()

    colored_diff = []
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "replace":
            colored_diff.append(f'<span style="color:magenta">{text2[j1:j2]}</span>')
        elif tag == "delete":
            colored_diff.append(f'<span style="color:red">{text1[i1:i2]}</span>')
        elif tag == "insert":
            colored_diff.append(f'<span style="color:green">{text2[j1:j2]}</span>')
        elif tag == "equal":
            colored_diff.append(text1[i1:i2])
    return "".join(colored_diff)
