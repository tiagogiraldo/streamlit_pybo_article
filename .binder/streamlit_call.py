from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(
        [
            "streamlit", 
            "run", 
            "app03.py", 
            "--browser.serverAddress=0.0.0.0", 
            "--server.enableCORS=False",
            "--runner.fixMatplotlib=True"
        ]
    )