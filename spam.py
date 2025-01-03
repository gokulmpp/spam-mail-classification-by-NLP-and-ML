import streamlit as st
import pickle 

model=pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vec123.pkl','rb'))

def main():
    st.title("Email Spam Classification Application")
    st.write("This is a Machine Learning application to classify emails as spam or ham.")
    st.subheader("Classification")
    user_input=st.text_area("Enter an email to classify", height=150)
    if st.button("Classify"):
        if user_input:
            data=[user_input]
            print(data)
            vec=cv.transform(data).toarray()
            result=model.predict(vec)
            if result[0]==0:
                st.success("this is Not a Spam mail")
            else:
                st.error("this is a spam mail") 
        else:
           
            st.write("Please enter an email to classify.")        
main()