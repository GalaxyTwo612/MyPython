import streamlit as st


st.title("Fibonacci Sequence")


term=st.number_input("Enter the number of sequence:")
sequence=int(term)

num1=0
num2=1
def result(se,a,b):
    if se<2:
        st.write("Please enter at least two terms!")
    elif se>=2:
        st.write("The fibonacci sequence")
        while se>0:  
            st.text(a)
            c=a+b
            a=b
            b=c
            se-=1
    else:
        st.write("Something wrong:(")

a=st.button("Run")
if a==1:
    result(sequence,num1,num2)


