import streamlit as st
import difflib as dl

from txt2tree import txt2tree

# Streamlit Elements

# st.set_page_config(layout="wide")
header = st.container()
upload = st.container()
output = st.container()


def text_diff(text1, text2):
    matcher = dl.SequenceMatcher(None, text1, text2)
    opcodes = matcher.get_opcodes()

    colored_diff = []
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == 'replace':
            colored_diff.append(f'<span style="color:magenta">{text2[j1:j2]}</span>')
        elif tag == 'delete':
            colored_diff.append(f'<span style="color:red">{text1[i1:i2]}</span>')
        elif tag == 'insert':
            colored_diff.append(f'<span style="color:green">{text2[j1:j2]}</span>')
        elif tag == 'equal':
            colored_diff.append(text1[i1:i2])
    return ''.join(colored_diff)


with header:
    st.markdown("<h1 style='text-align: center; color: white;'>DiffTree</h1>", unsafe_allow_html=True)

with upload:
    gt_file = st.file_uploader("Ground Truth File", type=['txt'])
    pred_files = st.file_uploader("Predictions File", type=['txt'], accept_multiple_files=True)

with output:
    gt_tree = txt2tree(gt_file.name)
    if gt_file and pred_files:
        for pred in pred_files:
            col1, col2 = st.columns(2)
            pred_tree = txt2tree(pred.name)

            gt_nodes = pred_tree.keys() - gt_tree.keys()
            pred_nodes = gt_tree.keys() - pred_tree.keys()
            all_keys = sorted(gt_tree.keys() | pred_tree.keys())

            with col1:
                st.subheader(gt_file.name)
                for key in all_keys:
                    if key in gt_nodes:
                        st.markdown(
                            f'<span style="color:white">{key} </span><span style="color:cyan">x-x-x-x-x-x-x-x-x</span>',
                            unsafe_allow_html=True)
                    elif key not in gt_nodes:
                        st.write(f"{key} - {gt_tree[key][0]} - {gt_tree[key][1]}")

            with col2:
                st.subheader(pred.name)
                for key in all_keys:
                    if key in pred_nodes:
                        st.markdown(
                            f'<span style="color:white">{key} </span><span style="color:cyan">x-x-x-x-x-x-x-x-x</span>',
                            unsafe_allow_html=True)

                    elif key not in gt_nodes and gt_tree[key][0] != pred_tree[key][0]:
                        st.markdown(

                            f'<span style="color:white">{key} - </span><span style="color:orange">{pred_tree[key][0]}</span><span style="color:white"> - {text_diff(gt_tree[key][1], pred_tree[key][1])}</span>',
                            unsafe_allow_html=True)
                    elif key not in gt_nodes:
                        st.write(f'{key} - {pred_tree[key][0]} - {text_diff(gt_tree[key][1], pred_tree[key][1])}',
                                 unsafe_allow_html=True)
                    elif key in gt_nodes:
                        st.write(f"{key} - {pred_tree[key][0]} - {pred_tree[key][1]}")

            st.write(f"GT Nodes Missing: {gt_nodes}")
            st.write(f"Prediction Nodes Missing: {pred_nodes}")
            st.markdown("------------------------------")
