import streamlit as st
import pandas as pd
table=pd.DataFrame({"Column1":[1,2,3,4,5,6,7],"Column2":[11,12,13,14,15,16,17]})
st.title("Hello! My New Dashboard App")
st.subheader("Hello! i'm trying to make a attractive dashboard")
st.header("Hello! This is my first dashboard")
st.text("Hello! I am text function and programme uses me inplace of paragraph tags")
st.markdown("**Hello** *World*") #bold ke liye humne *world* inka use kiya
st.markdown("# HELLO WORLD") #heading ko bada dikhane ke liye humne hash ka use kiya hai
st.markdown("[YOUTUBE](https://www.youtube.com/watch?v=ogG2fPLY544&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=4)")#iska use humne koi bhi link ko add krne ke liye kiya hai
st.markdown("----") #ye dash ka use humne line bnane ke liye hai
st.caption("hello i'm a caption ")
st.latex(r"\begin{pmatrix} a&b\\c&d\end{pmatrix}") #iaka use hum matrix format me use krne ke liye krte hai
json={"a":"1,2,3,4,5","b":"6,7,8,9,10"}
st.json(json)
code="""
print("hello world)
def funct():
    return 0;"""
st.code(code,language="python")
st.write("## HELLO")
st.metric(label="Wind speed",value="120ms\^-1",delta="1.4ms\^-1")

st.table(table)
st.dataframe(table)
st.image("image.png")
