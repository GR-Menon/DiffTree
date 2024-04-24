import streamlit as st
import difflib as dl

from diff import file_diff

header = st.container()
upload = st.container()
output = st.container()


def text_diff(text1, text2):
    matcher = dl.SequenceMatcher(None, text1, text2)
    opcodes = matcher.get_opcodes()

    colored_diff = []
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == 'replace':
            colored_diff.append(f'<span style="color:blue">{text1[i1:i2]}</span>')
        elif tag == 'delete':
            colored_diff.append(f'<span style="color:red">{text1[i1:i2]}</span>')
        elif tag == 'insert':
            colored_diff.append(f'<span style="color:green">{text2[j1:j2]}</span>')

    return ''.join(colored_diff)


with header:
    st.markdown("<h1 style='text-align: center; color: white;'>DiffTree</h1>", unsafe_allow_html=True)

with upload:
    gt_file = st.file_uploader("Ground Truth File", type=['txt'])
    pred_files = st.file_uploader("Predictions File", type=['txt'], accept_multiple_files=True)

with output:
    for pred in pred_files:
        diff = file_diff(gt_file.name, pred.name)
        st.subheader(pred.name)
        st.write(diff)

        for idx, err in enumerate(diff):
            gt = err[0]
            pd = err[1]
            if type(gt) != str:
                st.write("Level Diff")
                st.write(gt)
            elif gt == pd:
                st.write("Node_Type Diff")
            elif gt != pd:
                st.markdown(text_diff(gt, pd), unsafe_allow_html=True)