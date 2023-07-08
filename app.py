import cv2
import threading
from flask import Flask, render_template, Response
import os
import playsound


app = Flask(__name__)
# URL video streaming
url = 'http://192.168.1.8:8080/video'
# url = 'http://192.168.140.164:8080/video'
# 192.168.140.215

# Buat objek VideoCapture menggunakan URL
cap = cv2.VideoCapture(url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

stop_program = False
classId_Result = []
classId_Result_lock = threading.Lock()

def process_image():
    global classId_Result, stop_program
    while not stop_program:
        success, img = cap.read()
        classIds, confs, bbox = net.detect(img, confThreshold=0.5)

        with classId_Result_lock:
            classId_Result = classIds # Salin nilai classIds ke classId_Result
        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 0), 2)
                cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 0), 2)

        ret, frame = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
        frame = frame.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

def process_sound():
    global classId_Result, stop_program  # Menggunakan shared variable classIds dan stop_program

    while not stop_program:
        with classId_Result_lock:
            current_classId_Result = classId_Result  # Salin nilai classId_Result ke current_classId_Result
        sound_folder = os.path.join(os.path.dirname(__file__), "sounds")
        sound_file= ""

        with open('coco.names', 'rt') as f:
            labels = f.readlines()
            if len(current_classId_Result) > 0:
                label_first = current_classId_Result[0]
                label_number = label_first - 1
                label_index = label_number  # Indeks label yang ingin diakses

                if label_index < len(labels):
                    label = labels[label_index].strip()
                    print("Ini labelnya", label)
                    if label == "manusia":
                        sound_file = os.path.join(sound_folder, "manusia.wav")  # Menggunakan file suara dengan nama yang sesuai dengan label
                    elif label == "sepeda":
                        sound_file = os.path.join(sound_folder, "sepeda.wav") 
                    elif label == "mobil":
                        sound_file = os.path.join(sound_folder, "mobil.wav") 
                    elif label == "motor":
                        sound_file = os.path.join(sound_folder, "motor.wav") 
                    elif label == "pesawat":
                        sound_file = os.path.join(sound_folder, "pesawat.wav") 
                    elif label == "bis":
                        sound_file = os.path.join(sound_folder, "bis.wav") 
                    elif label == "kereta":
                        sound_file = os.path.join(sound_folder, "kereta.wav") 
                    elif label == "truk":
                        sound_file = os.path.join(sound_folder, "truk.wav") 
                    elif label == "kapal":
                        sound_file = os.path.join(sound_folder, "kapal.wav") 
                    elif label == "lampu lalu lintas":
                        sound_file = os.path.join(sound_folder, "lampu lalu lintas.wav") 
                    elif label == "keran kebakaran":
                        sound_file = os.path.join(sound_folder, "keran kebakaran.wav") 
                    elif label == "tanda jalan":
                        sound_file = os.path.join(sound_folder, "tanda jalan.wav") 
                    elif label == "tanda berhenti":
                        sound_file = os.path.join(sound_folder, "tanda berhenti.wav") 
                    elif label == "parkir":
                        sound_file = os.path.join(sound_folder, "parkir.wav") 
                    elif label == "bangku":
                        sound_file = os.path.join(sound_folder, "bangku.wav") 
                    elif label == "bir":
                        sound_file = os.path.join(sound_folder, "bir.wav") 
                    elif label == "kucing":
                        sound_file = os.path.join(sound_folder, "kucing.wav") 
                    elif label == "anjing":
                        sound_file = os.path.join(sound_folder, "anjing.wav") 
                    elif label == "kuda":
                        sound_file = os.path.join(sound_folder, "kuda.wav") 
                    elif label == "domba":
                        sound_file = os.path.join(sound_folder, "domba.wav") 
                    elif label == "sapi":
                        sound_file = os.path.join(sound_folder, "sapi.wav") 
                    elif label == "gajah":
                        sound_file = os.path.join(sound_folder, "gajah.wav") 
                    elif label == "beruang":
                        sound_file = os.path.join(sound_folder, "beruang.wav") 
                    elif label == "zebra":
                        sound_file = os.path.join(sound_folder, "zebra.wav") 
                    elif label == "jerapa":
                        sound_file = os.path.join(sound_folder, "jerapa.wav") 
                    elif label == "topi":
                        sound_file = os.path.join(sound_folder, "topi.wav") 
                    elif label == "tas":
                        sound_file = os.path.join(sound_folder, "tas.wav") 
                    elif label == "payung":
                        sound_file = os.path.join(sound_folder, "payung.wav") 
                    elif label == "sepatu":
                        sound_file = os.path.join(sound_folder, "sepatu.wav") 
                    elif label == "kacamata": 
                        sound_file = os.path.join(sound_folder, "kacamata.wav")
                    elif label == "tas tangan":
                        sound_file = os.path.join(sound_folder, "tas tangan.wav") 
                    elif label == "dasi":
                        sound_file = os.path.join(sound_folder, "dasi.wav") 
                    elif label == "koper":
                        sound_file = os.path.join(sound_folder, "koper.wav") 
                    elif label == "frisbee":
                        sound_file = os.path.join(sound_folder, "frisbee.wav") 
                    elif label == "ski":
                        sound_file = os.path.join(sound_folder, "ski.wav") 
                    elif label == "papan seluncur":
                        sound_file = os.path.join(sound_folder, "papan seluncur.wav") 
                    elif label == "bola":
                        sound_file = os.path.join(sound_folder, "bola.wav") 
                    elif label == "layang-layang":
                        sound_file = os.path.join(sound_folder, "layang-layang.wav") 
                    elif label == "tongkat pemukul baseball":
                        sound_file = os.path.join(sound_folder, "tongkat pemukul baseball.wav") 
                    elif label == "sarung baseball":
                        sound_file = os.path.join(sound_folder, "sarung baseball.wav") 
                    elif label == "skateboard":
                        sound_file = os.path.join(sound_folder, "skateboard.wav") 
                    elif label == "papan luncur":
                        sound_file = os.path.join(sound_folder, "papan luncur.wav") 
                    elif label == "raket tenis":
                        sound_file = os.path.join(sound_folder, "raket tenis.wav") 
                    elif label == "botol":
                        sound_file = os.path.join(sound_folder, "botol.wav") 
                    elif label == "piring":
                        sound_file = os.path.join(sound_folder, "piring.wav") 
                    elif label == "gelas anggur":
                        sound_file = os.path.join(sound_folder, "gelas anggur.wav") 
                    elif label == "cangkir":
                        sound_file = os.path.join(sound_folder, "cangkir.wav") 
                    elif label == "garpu":
                        sound_file = os.path.join(sound_folder, "garpu.wav") 
                    elif label == "Hati-hati benda tajam, pisau":
                        sound_file = os.path.join(sound_folder, "Hati-hati benda tajam, pisau.wav") 
                    elif label == "sendok":
                        sound_file = os.path.join(sound_folder, "sendok.wav") 
                    elif label == "mangkuk":
                        sound_file = os.path.join(sound_folder, "mangkuk.wav") 
                    elif label == "pisang":
                        sound_file = os.path.join(sound_folder, "pisang.wav") 
                    elif label == "apel":
                        sound_file = os.path.join(sound_folder, "apel.wav") 
                    elif label == "sandwich":
                        sound_file = os.path.join(sound_folder, "sandwich.wav") 
                    elif label == "oranye":
                        sound_file = os.path.join(sound_folder, "oranye.wav") 
                    elif label == "Brokoli":
                        sound_file = os.path.join(sound_folder, "Brokoli.wav") 
                    elif label == "wortel":
                        sound_file = os.path.join(sound_folder, "wortel.wav") 
                    elif label == "Hot Dog":
                        sound_file = os.path.join(sound_folder, "Hot Dog.wav") 
                    elif label == "Pizza":
                        sound_file = os.path.join(sound_folder, "pizza.wav")    
                    elif label == "donat":
                        sound_file = os.path.join(sound_folder, "donat.wav") 
                    elif label == "kue":
                        sound_file = os.path.join(sound_folder, "kue.wav") 
                    elif label == "kursi":
                        sound_file = os.path.join(sound_folder, "kursi.wav") 
                    elif label == "sofa":
                        sound_file = os.path.join(sound_folder, "sofa.wav") 
                    elif label == "tanaman di dalam pot":
                        sound_file = os.path.join(sound_folder, "tanaman di dalam pot.wav") 
                    elif label == "tempat tidur":
                        sound_file = os.path.join(sound_folder, "tempat tidur.wav") 
                    elif label == "cermin":
                        sound_file = os.path.join(sound_folder, "cermin.wav") 
                    elif label == "meja makan":
                        sound_file = os.path.join(sound_folder, "meja makan.wav")
                    elif label == "jendela":
                        sound_file = os.path.join(sound_folder, "jendela.wav") 
                    elif label == "meja":
                        sound_file = os.path.join(sound_folder, "meja.wav") 
                    elif label == "toilet":
                        sound_file = os.path.join(sound_folder, "toilet.wav") 
                    elif label == "pintu":
                        sound_file = os.path.join(sound_folder, "pintu.wav") 
                    elif label == "televisi":
                        sound_file = os.path.join(sound_folder, "televisi.wav") 
                    elif label == "laptop":
                        sound_file = os.path.join(sound_folder, "laptop.wav") 
                    elif label == "mouse":
                        sound_file = os.path.join(sound_folder, "mouse.wav") 
                    elif label == "terpencil":
                        sound_file = os.path.join(sound_folder, "terpencil.wav") 
                    elif label == "papan ketik":
                        sound_file = os.path.join(sound_folder, "papan ketik.wav") 
                    elif label == "telepon selular":
                        sound_file = os.path.join(sound_folder, "telepon selular.wav") 
                    elif label == "gelombang mikro":
                        sound_file = os.path.join(sound_folder, "gelombang mikro.wav") 
                    elif label == "oven":
                        sound_file = os.path.join(sound_folder, "oven.wav") 
                    elif label == "pemanggang roti":
                        sound_file = os.path.join(sound_folder, "pemanggang roti.wav")
                    elif label == "tenggelam":
                        sound_file = os.path.join(sound_folder, "tenggelam.wav") 
                    elif label == "lemari es":
                        sound_file = os.path.join(sound_folder, "lemari es.wav") 
                    elif label == "blender":
                        sound_file = os.path.join(sound_folder, "blender.wav") 
                    elif label == "buku":
                        sound_file = os.path.join(sound_folder, "buku.wav") 
                    elif label == "jam":
                        sound_file = os.path.join(sound_folder, "jam.wav") 
                    elif label == "vas":
                        sound_file = os.path.join(sound_folder, "vas.wav") 
                    elif label == "Hati-hati benda tajam, gunting":
                        sound_file = os.path.join(sound_folder, "Hati-hati benda tajam, gunting.wav") 
                    elif label == "beruang teddy":
                        sound_file = os.path.join(sound_folder, "beruang teddy.wav") 
                    elif label == "pengering rambut":
                        sound_file = os.path.join(sound_folder, "pengering rambut.wav") 
                    elif label == "sikat gigi":
                        sound_file = os.path.join(sound_folder, "sikat gigi.wav") 
                    elif label == "sikat rambut":
                        sound_file = os.path.join(sound_folder, "sikat rambut.wav") 
                    
                    else :
                        continue
                    playsound.playsound(sound_file)
                else:
                    print("Invalid label index.")


classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Membuat thread untuk pemrosesan gambar dan pemutaran suara
image_thread = threading.Thread(target=process_image)
sound_thread = threading.Thread(target=process_sound)

# Menjalankan thread secara bersamaan
image_thread.start()
sound_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(process_image(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
    stop_program = True  # Mengubah nilai stop_program menjadi True
    image_thread.join()  # Menunggu thread image_thread selesai
    sound_thread.join()  # Menunggu thread sound_thread selesai
    cap.release()  # Melepas sumber video
    cv2.destroyAllWindows()  # Menutup jendela OpenCV



