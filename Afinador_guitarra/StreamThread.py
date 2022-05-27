from threading import Thread, Event
import numpy as np
import sounddevice as sd

class StreamThread(Thread):

    def __init__(self, app):
        super().__init__()        
        self.dispoitivo_input = 1
        self.dispoitivo_output = 3
        self.tamano_bloque = 8000
        self.frecuencia_muestreo = 44100
        self.canales = 1
        self.tipo_dato = np.int16
        self.latencia = "high"
        self.app = app

    def callback_stream(self, indata, outdata, frames, time, status):

        data = indata[:,0]
        transformada = np.fft.rfft(data)
        periodo_muestreo = 1/self.frecuencia_muestreo
        frecuencias = np.fft.rfftfreq(len(data), periodo_muestreo)
        frecuencia_fundamental = frecuencias[np.argmax(np.abs(transformada))]
        print("frecuencia fundamental: " + str(frecuencias[np.argmax(np.abs(transformada))]))

        if frecuencia_fundamental <= 80:
            print("Apretar cuerda para tecla 6 (E2)")
            self.app.win.fill(self.app.black)    
            self.app.win.blit(self.app.letter2, (150,130))  
        if frecuencia_fundamental >= 81 and frecuencia_fundamental <= 83:
            print("Tecla 6 (E)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter1, (150,130))  
        if frecuencia_fundamental >= 84 and frecuencia_fundamental <= 100:
            print("Aflojar cuerda para tecla 6 (E2)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter2, (150,130))  

        if frecuencia_fundamental >= 101 and frecuencia_fundamental <= 108:
            print("Apretar cuerda para tecla 5 (A2)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter4, (150,130))  
        if frecuencia_fundamental >= 109 and frecuencia_fundamental <= 111:
            print("Tecla 5 (A)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter3, (150,130))  
        if frecuencia_fundamental >= 112 and frecuencia_fundamental <= 120:
            print("Aflojar cuerda para tecla 5 (A2)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter4, (150,130))  
            

        if frecuencia_fundamental >= 121 and frecuencia_fundamental <= 144:
            print("Apretar cuerda para tecla 4 (D3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter6, (150,130))
        if frecuencia_fundamental >= 145 and frecuencia_fundamental <= 148:
            print("Tecla 4 (D)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter5, (150,130))  
        if frecuencia_fundamental >= 149 and frecuencia_fundamental <= 170:
            print("Aflojar cuerda para tecla 4 (D3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter6, (150,130))  
            

        if frecuencia_fundamental >= 171 and frecuencia_fundamental <= 194:
            print("Apretar cuerda para tecla 3 (G3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter8, (150,130))  
        if frecuencia_fundamental >= 195 and frecuencia_fundamental <= 197:
            print("Tecla 3 (G)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter7, (150,130))  
        if frecuencia_fundamental >= 198 and frecuencia_fundamental <= 212:
            print("Aflojar cuerda para tecla 3 (G3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter8, (150,130))  

        if frecuencia_fundamental >= 212 and frecuencia_fundamental <= 244:
            print("Apretar cuerda para tecla 2 (B3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter10, (150,130))  
        if frecuencia_fundamental >= 245 and frecuencia_fundamental <= 247:
            print("Tecla 2 (B)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter9, (150,130))  
        if frecuencia_fundamental >= 248 and frecuencia_fundamental <= 300:
            print("Aflojar cuerda para tecla 2 (B3)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter10, (150,130))  
            

        if frecuencia_fundamental >= 301 and frecuencia_fundamental <= 327:
            print("Apretar cuerda para tecla 1 (E4)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter12, (150,130))  
        if frecuencia_fundamental >= 328 and frecuencia_fundamental <= 330:
            print("Tecla 1 (E)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter11, (150,130))  
        if frecuencia_fundamental >= 331:
            print("Aflojar cuerda para tecla 1 (E4)")
            self.app.win.fill(self.app.black)   
            self.app.win.blit(self.app.letter12, (150,130)) 
            

        
        return

    def run(self):
        try:
            self.event = Event()
            with sd.Stream(
                device=(self.dispoitivo_input, self.dispoitivo_output), #Se eligen dispositivos (entrada, salida)
                blocksize= self.tamano_bloque, # 0 significa que la tarjeta de sonido decide el mejor tamaño
                samplerate= self.frecuencia_muestreo, # frecuencia de muestreo
                channels= self.canales, #numero de canales1
                dtype= self.tipo_dato, #Tipo de dato (profundidad de bits)
                latency=self.latencia, # Latencia, que tanto tiempo pasa desde entrada hasta la salida
                callback= self.callback_stream
            ) as self.stream:
                self.event.wait()

        except Exception as e:
            print(str(e))

