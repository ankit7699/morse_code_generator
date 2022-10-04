import streamlit as st
import os



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt_to_morse_code(term):
    results = ''.join([MORSE_CODE_DICT.get(i,i) for i in list(term)])
    return results

def main():
    st.title("Morse code App")
    st.subheader("Enter text in Upper case for results")

    menu = ["Home"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")


        with st.form(key='encryptform',clear_on_submit=True):
            raw_text = st.text_area("Enter Text here")
            submit_button = st.form_submit_button(label='encrypt')

        if submit_button:
            col1,col2 = st.columns([2,1])
            with col1:
                st.info("Morse Code")
                st.write("orignal text : {}".format(raw_text))
                results = encrypt_to_morse_code(raw_text)
                st.write(results)
                st.code(results)

            with col2:
                st.info("Morse code Audio")
                with st.expander("Play Audio"):
                    for i in list(raw_text.upper()):
                        audio_file = open(os.path.join('morse_code_audio_files', '{}_morse_code.ogg'.format(i)), 'rb')
                        audio_bytes = audio_file.read()
                        st.write('{}'.format(i))
                        st.audio(audio_bytes)





    else:
        st.subheader("About")

if __name__ == '__main__':
    main()