from flask import Flask, render_template, request, json
import sys
import dataset_creator

app = Flask(__name__, static_url_path='/webapp')


@app.route('/')
def root():
    return render_template('index.html')


@app.route("/search", methods=['POST'])
def search():
    requestData = request.form.to_dict()
    results = dataset_creator.SoDatasetCreator.fetch_search_results(
        requestData.get("searchvalue"), requestData.get("searchtype"))
    return json.dumps(results)


if __name__ == "__main__":
    app.run()
