from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/send_html')
def send_html():
    return render_template('send_html.html')

@FAI.route('/property')
def property():
    return render_template('property.html',name='Priya')

if __name__=='__main__':
    FAI.run(debug=True)
