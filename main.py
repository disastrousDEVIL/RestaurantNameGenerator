import streamlit as st
import langchain_helper as lh
st.title("Restraunt Name Generator")
cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexican","German","Scottish"))
if cuisine:
    response=lh.generate(cuisine)
    st.header(response['restaurant_name'])
    menu_items=response['items_list'].split(",")
    st.write("**MENU ITEMS**")
    for i in menu_items:
        st.write("-",i)
