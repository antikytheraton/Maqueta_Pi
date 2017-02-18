#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, send_from_directory
from time import sleep, strftime, gmtime
import RPi.GPIO as GPIO
from multiprocessing import Process
import fileID

app = Flask(__name__)

def pushState(val):
    fileID.overwriteID("state.txt",val)

def popState():
    val = fileID.readID("state.txt") 
    return str(val)

def init_process():
	processInterface = Process(target=set_input_pi, args=())
    processInterface.start()

def scan_state():
	#state = 1:Entrada,2:Descarga,3:Carga,4:Salida
	value = popState()
	return value

def set_input_pi():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	while True:
    	entrada = GPIO.input(13)
    	carga = GPIO.input(15)
    	descarga = GPIO.input(16)
    	salida = GPIO.input(18)
    	if entrada == True:
        	pushState(1)
        	time.sleep(0.2)
        if carga == True:
        	pushState(2)
        	time.sleep(0.2)
        if descarga == True:
        	pushState(3)
        	time.sleep(0.2)
        if salida == True:
        	pushState(4)
        	time.sleep(0.2)
        else:
        	pushState(0)
	 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/state', methods=['GET'])
def get_tasks():
	state = scan_state()
	return jsonify({'state':state})

@app.route('/init', methods=['GET'])
def iniciar():
	init_process()
	return jsonify({'state':'iniciando...'})


if __name__ == '__main__':
    app.run(debug=True, host="192.168.12.205", port=3000)
    #10.42.0.1
