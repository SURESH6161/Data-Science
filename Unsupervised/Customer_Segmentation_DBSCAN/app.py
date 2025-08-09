from flask import Flask, render_template, request
import os
from create_model import run_dbscan

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Save uploaded file
        file = request.files["file"]
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Run DBSCAN
            df, plot_path = run_dbscan(file_path)

            # Convert dataframe to HTML table
            table_html = df.to_html(classes="table table-striped", index=False)
            return render_template("index.html", table=table_html, plot_path=plot_path)

    return render_template("index.html", table=None, plot_path=None)


if __name__ == "__main__":
    app.run(debug=True)
