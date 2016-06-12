from django import forms

class BMIForm(forms.Form):
    weight = forms.IntegerField(label = 'Your weight (in kg)', required = True, min_value = 0)
    size = forms.IntegerField(label = 'Your size (in cm)', required = True, min_value = 0)
    
class EERForm(forms.Form):
    sexChoices = [('man', 'Man'), ('woman', 'Woman')]
    activityChoices = [(0, 'None'), 
                       (1, 'Moderate (1h - 2h per week)'), 
                       (2, 'Active (30m - 1h per day)'), 
                       (3, 'Very active (more than 1h per day)')]
    
    age = forms.IntegerField(label = 'Your age', required = True, min_value = 0)
    weight = forms.IntegerField(label = 'Your weight (in kg)', required = True, min_value = 0)
    size = forms.IntegerField(label = 'Your size (in cm)', required = True, min_value = 0)
    sex = forms.ChoiceField(choices = sexChoices, widget = forms.RadioSelect(), required = True)
    activity = forms.ChoiceField(choices = activityChoices, required = True)
    