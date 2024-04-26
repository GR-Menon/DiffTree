import os
import re
import streamlit as st
import difflib as dl

from txt2tree import txt2tree
from utils import get_pred, text_diff

# Streamlit Elements

# st.set_page_config(layout="wide")
header = st.container()
upload = st.container()
output = st.container()

# App Content

with header:
    st.markdown("<h1 style='text-align: center; color: white;'>DiffTree</h1>", unsafe_allow_html=True)

with upload:
    gt_path = "labels/actual_labels/"
    pred_path = "labels/predicted_labels/"
    gt_file_list = sorted(os.listdir(gt_path))
    pred_file_list = sorted(os.listdir(pred_path))

    gt_file = st.selectbox("Select Files", options=gt_file_list)

with output:
    gt_tree = txt2tree(os.path.join(gt_path, gt_file))
    pred = get_pred(gt_file, pred_file_list)
    pred_tree = txt2tree(os.path.join(pred_path, pred))
    col1, col2 = st.columns(2)

    gt_nodes = pred_tree.keys() - gt_tree.keys()
    pred_nodes = gt_tree.keys() - pred_tree.keys()
    all_keys = sorted(gt_tree.keys() | pred_tree.keys())

    with col1:
        st.subheader(gt_file)
        for key in all_keys:
            if key in gt_nodes:
                st.markdown(
                    f'<span style="color:white">{key} </span><span style="color:cyan">x-x-x-x-x-x-x-x-x</span>',
                    unsafe_allow_html=True)
            elif key not in gt_nodes:
                st.write(f"{key} - {gt_tree[key][0]} - {gt_tree[key][1]}")

    with col2:
        st.subheader(pred)
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
