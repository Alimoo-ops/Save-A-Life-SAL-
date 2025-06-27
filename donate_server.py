from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Donate to Save a Life</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-image: url('{{ url_for('static', filename='donate.png') }}');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #fff;
                text-align: center;
                padding-top: 50px;
            }
            .container {
                background-color: rgba(0, 0, 0, 0.5);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                padding: 60px 40px;
                border-radius: 25px;
                display: inline-block;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
                max-width: 95%;
                width: 600px;
            }
            h1 {
                font-size: 34px;
                margin-bottom: 25px;
                text-shadow: 1px 1px 3px black;
            }
            p {
                font-size: 19px;
                margin-bottom: 30px;
                text-shadow: 1px 1px 2px black;
                line-height: 1.6em;
            }
            img {
                width: 230px;
                height: 230px;
                border-radius: 10px;
                border: 2px solid #fff;
                margin-bottom: 20px;
            }
            .btn {
                background-color: #0070ba;
                color: white;
                padding: 16px 35px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                box-shadow: 0 4px 10px rgba(0,0,0,0.4);
            }
            .btn:hover {
                background-color: #005b9e;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Donate to Save a Life</h1>
            <p>
                Welcome, and thank you for taking a moment to be here.<br><br>
                Every day, someone out there is silently battling for their life — facing hardship, hunger, illness, or hopelessness.  
                Most of them don’t have a voice loud enough to ask for help… but you being here?  
                That already means the world.<br><br>
                This platform was created with one purpose: to offer a second chance.  
                To give hope where there is none. To remind someone, somewhere, that they are not forgotten.  
                That they matter.<br><br>
                Your generosity — no matter how big or small — can become food for a hungry child, medicine for the sick, or shelter for someone cold and afraid.  
                Your kindness has power.  
                Real, life-changing power.<br><br>
                So if you're able to give, we invite you to be that miracle for someone today.  
                Help us save a life — one act of compassion at a time.
            </p>

            <!-- ✅ QR Code -->
            <img src="{{ url_for('static', filename='paypal_qr.png') }}" alt="PayPal QR Code"><br><br>

            <!-- ✅ Donate Button -->
            <form action="/donate">
                <button class="btn">Donate Now via PayPal</button>
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/donate')
def donate():
    return redirect("https://www.paypal.com/donate/?hosted_button_id=L5YDNBGVUKBWU&return_url=http://127.0.0.1:5000/thankyou")

@app.route('/thankyou')
def thankyou():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Thank You</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-image: url('{{ url_for('static', filename='donate.png') }}');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #fff;
                text-align: center;
                padding-top: 100px;
            }
            .message-box {
                background-color: rgba(0, 0, 0, 0.6);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                padding: 50px 30px;
                border-radius: 25px;
                display: inline-block;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
                max-width: 90%;
                width: 550px;
            }
            h2 {
                font-size: 32px;
                margin-bottom: 20px;
            }
            p {
                font-size: 18px;
                line-height: 1.6em;
            }
        </style>
    </head>
    <body>
        <div class="message-box">
            <h2>Thank You 🙏</h2>
            <p>
                Your donation has been received with deep gratitude.<br><br>
                You may never meet the person you've helped,  
                but know this — your generosity has created a ripple of hope  
                that can reach farther than you imagine.<br><br>
                From the bottom of our hearts, thank you for being part of this mission to save a life.
            </p>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
