import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    post_office_details = None
    
    if request.method == 'POST':
        pincode = request.form.get('zipCode')
        
        if not pincode.isnumeric() or len(pincode) != 6:
            error = "Incorrect Pin Code (String / False Code entered)"
            return render_template('index.html', error=error)
        
        try:
            url = f"https://api.postalpincode.in/pincode/{pincode}"
            response = requests.get(url)
            data = response.json()
            
            if data[0]['Status'] == 'Success':
                post_office = data[0]['PostOffice'][0]
                return render_template('results.html', 
                                       post_office=post_office['State'],
                                       name=post_office['Name'],
                                       block=post_office['Block'],
                                       district=post_office['District'])
            else:
                error = "No post office found for this pincode"
        except Exception as e:
            error = "Error fetching post office details"
    
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)