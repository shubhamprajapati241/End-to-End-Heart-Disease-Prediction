from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict_datapoints():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # data=CustomData( 
        #     carat=float(request.form.get('carat')),
        #     cut = request.form.get('cut')
        # )
        # this is my final data
        # final_data=data.get_data_as_dataframe()
        # predict_pipeline=PredictPipeline()
        # pred=predict_pipeline.predict(final_data)
        # result=round(pred[0],2)
        # return render_template("result.html",final_result=result)
        return 

## execution begin 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)