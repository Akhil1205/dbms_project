import streamlit as st
import mysql.connector
from create_crime import create


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS PES1UG20CS108_PROJECT;")


def main():
    st.title("Crime Data Management System")
    menu = ["Add Crime Details", "View Crime Details", "Edit Crime Details", "Remove Crime Details"]
    choice = st.sidebar.selectbox("Menu", menu)

    
    if choice == "Add Crime Details":
        st.subheader("Enter Crime Details:")
        create()

    elif choice == "View Trains":
        st.subheader("View Train Details:")
        

    elif choice == "Edit Train Info":
        st.subheader("Edited Train Details:")
        

    elif choice == "Remove Train":
        st.subheader("Delete Train:")
        

    else:
        st.subheader("About Train")


if __name__ == '__main__':
    main()