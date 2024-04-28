from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def spam_text():
    lokasi = ''
    pesan = ''
    jumlah = ''
    
    if request.method == 'POST':
        lokasi = request.form.get('lokasi', '')
        pesan = request.form.get('pesan', '')
        jumlah = request.form.get('jumlah', '')
        
        # Validasi input untuk jumlah spam
        if not jumlah.isdigit():
            return render_template('form.html', lokasi=lokasi, pesan=pesan, jumlah=jumlah, error="Jumlah spam harus berupa bilangan bulat.")
        
        jumlah = int(jumlah)
        
        angka = 1
        with open(f"{lokasi}", "w") as file:
            while angka <= jumlah:
                file.write(f"{pesan}\n")
                angka += 1
                
                if angka == 1000:
                    breaking = request.form.get('berhenti')
                    if breaking == "y":
                        break
        
        # After processing, render the same form template
        return render_template('form.html', lokasi='', pesan='', jumlah='', error=None)
    
    # For GET requests, just render the form template
    return render_template('form.html', lokasi='', pesan='', jumlah='', error=None)

if __name__ == '__main__':
    app.run(debug=True)
