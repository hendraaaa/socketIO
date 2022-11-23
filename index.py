from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from kafka import KafkaProducer, KafkaConsumer, TopicPartition

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*",logger=True, engineio_logger=True)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
TOPIC_NAME = "myTopicTaSM"

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@socketio.on('kafkaconsumer')
def kafka_consumer(msg):
    print(msg)
    consumer = KafkaConsumer('myTopicTaSM',bootstrap_servers=['10.0.0.94:9092'])
    for message in consumer:
        emit('kafkaconsumer', 
             {
                'data': message.value.decode('utf-8'),
                'counter': counter,})
        if message.value.decode('utf-8') == 'stop':
            consumer.commit()
            break

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)
