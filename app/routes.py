from flask import Blueprint,render_template,request
from app.bmi import _convert_value,BMICalc

# 'bmi' is internal name
bmi_bp=Blueprint('bmi',__name__)


@bmi_bp.route('/',methods=['GET','POST'])
def landing():
    if request.method=="POST":
        height=request.form.get('height')
        height_unit=request.form.get('height_unit')
        weight=request.form.get('weight')
        weight_unit=request.form.get('weight_unit')

        height=_convert_value(height,float)
        weight=_convert_value(weight,float)

        if height is None :
            return render_template('index.html',error="Please enter a valid height")
        elif weight is None:
            return render_template('index.html',error="Please enter a valid weight")

        calc_instance=BMICalc()

        calc_instance._convert_unit(data={'height':height,'height_unit':height_unit,'weight':weight,'weight_unit':weight_unit})

        bmi, custom_message, feedback = calc_instance._calculate_bmi()

        return render_template('index.html',bmi=bmi,message=custom_message,feedback=feedback)
    
    else:
        return render_template('index.html')