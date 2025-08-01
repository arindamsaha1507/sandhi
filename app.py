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

        with st.container(border=True):
            st.write("### Processed Sentence:")
            st.write(result[0])

        with st.expander("View Sandhi Summary"):
            st.write("This is the sandhi summary.")
            st.write(result[1])

        with st.expander("View Prakriya"):
            st.write("This is the prakriya.")
            st.write(result[2])


if __name__ == "__main__":
    main()
