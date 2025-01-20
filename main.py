# main.py
import sys
import streamlit.web.cli as stcli

def main():
    # symulujemy "streamlit run app.py":
    sys.argv = ["streamlit", "run", "app.py", "--server.port=8502"]
    stcli.main()

if __name__ == "__main__":
    main()
