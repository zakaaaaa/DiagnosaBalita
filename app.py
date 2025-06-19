from flask import Flask, render_template, request

app = Flask(__name__)

# RULES
rules = {
    "flu": {"demam", "batuk", "pilek"},
    "diare": {"muntah", "feses_cair", "lemas"},
    "campak": {"demam", "ruam", "mata_merah"},
    "radang_tenggorokan": {"sakit_tenggorokan", "demam", "tidak_nafsu_makan"},
    "infeksi_telinga": {"telinga_nyeri", "demam", "rewel"},
}

gejala_semua = sorted({g for s in rules.values() for g in s})

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected = set(request.form.getlist("gejala"))
        hasil = [p for p, gejala in rules.items() if gejala.issubset(selected)]
        return render_template("index.html", gejala=gejala_semua, hasil=hasil, selected=selected)
    return render_template("index.html", gejala=gejala_semua)

if __name__ == "__main__":
    app.run(debug=True)
