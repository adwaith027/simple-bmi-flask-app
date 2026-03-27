ht_options = {
    1: ['feet(ft)', 'feet', 'ft'],
    2: ['meters(m)', 'meters', 'm'],
    3: ['inches(in)', 'inches', 'in'],
    4: ['centimeters(cm)', 'centimeters', 'cm']
}

wt_options = {
    1: ['pounds(lbs)', 'pounds', 'lbs'],
    2: ['kilograms(kg)', 'kilograms', 'kg']
}


def _convert_value(selection, target):
    try:
        return target(selection)
    except ValueError:
        return None


class BMICalc():
    def __init__(self):
        self.height = None
        self.height_unit = None
        self.weight = None
        self.weight_unit = None

    def _convert_unit(self, data):
        # height
        if data['height'] is not None and data['height_unit']:
            self.height_unit = data['height_unit']

            if self.height_unit == 'ft':
                self.height = data['height'] * 0.3048
            elif self.height_unit == 'm':
                self.height = data['height']
            elif self.height_unit == 'in':
                self.height = data['height'] * 0.0254
            elif self.height_unit == 'cm':
                self.height = data['height'] / 100

        # weight
        if data['weight'] is not None and data['weight_unit']:
            self.weight_unit = data['weight_unit']

            if self.weight_unit == 'lbs':
                self.weight = data['weight'] * 0.453592
            elif self.weight_unit == 'kg':
                self.weight = data['weight']

    def _calculate_bmi(self):
        if self.height is None or self.weight is None:
            return None, None, None

        if self.height <= 0 or self.weight <= 0:
            return None, None, None

        bmi = round(self.weight / (self.height ** 2), 2)

        if bmi < 16.0:
            custom_message = "Severe Underweight"
            feedback = "You should consult a doctor or nutritionist."
        elif 16.0 <= bmi <= 18.4:
            custom_message = "Underweight"
            feedback = "You may need to gain some weight for a healthier range."
        elif 18.5 <= bmi <= 24.9:
            custom_message = "Normal Weight"
            feedback = "Great! You are in a healthy weight range."
        elif 25.0 <= bmi <= 29.9:
            custom_message = "Overweight (Pre-obese)"
            feedback = "Consider regular exercise and a balanced diet."
        elif 30.0 <= bmi <= 34.9:
            custom_message = "Obese Class I (Moderate)"
            feedback = "Consult a doctor and watch diet and exercise."
        elif 35.0 <= bmi <= 39.9:
            custom_message = "Obese Class II (Severe)"
            feedback = "Medical supervision recommended for weight management."
        else:
            custom_message = "Obese Class III (Morbid)"
            feedback = "Seek urgent medical advice for your health."

        return bmi, custom_message, feedback