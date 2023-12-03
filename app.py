"""Main streamlit app."""


import streamlit as st

from sandhi import VarnaSandhi, VisargaSandhi


def main():
    """Main function of the App."""

    varna_sandhi = VarnaSandhi()
    visaarga_sandhi = VisargaSandhi()

    st.title("Hello World")
    st.write("This is a test to see if streamlit works.")
    string = st.text_area("This is a text area.")
    string = string.strip()

    if st.button("Submit"):

        words = string.split(" ")

        result = words[0]

        for index in range(1, len(words)):
            if result[-1] == "ः":
                result = visaarga_sandhi.sandhi(result, words[index])
            else:
                result = varna_sandhi.sandhi(result, words[index])

        st.write(result)


if __name__ == "__main__":
    main()
