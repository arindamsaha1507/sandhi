"""Main streamlit app."""

import streamlit as st

from vaakya_sandhi import vaakya_sandhi


def main():
    """Main function of the App."""

    st.title("Hello World")
    st.write("This is a test to see if streamlit works.")
    string = st.text_area("This is a text area.")
    string = string.strip()

    if st.button("Submit"):

        result = vaakya_sandhi(string)

        st.write(result[0])


if __name__ == "__main__":
    main()
