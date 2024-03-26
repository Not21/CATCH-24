from.models import Studentinfomodel
from django import forms



class Studentinfomodelform(forms.ModelForm):

    departchoices=[('--select department--','--select department--'),('Cyber security','Cyber security'),('AIDS','AIDS'),('ECE','ECE'),('Pharma','Pharma'),('Agriculture','Agriculture'),('EEE','EEE'),
                ('Civil','Civil'),('Food tech','Food tech'),('Aerospace','Aerospace'),('Aeronautical','Aeronautical'),('MECH','MECH'),('CSE','CSE'),
                ('IT','IT'),('Chemical','Chemical'),('Mechatronics','Mechatronics')]
    department=forms.ChoiceField(choices=departchoices) 
    genderchoice=[('male','male'),('female','female')]
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=genderchoice)
    yearchoice=[('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th')]
    year=forms.ChoiceField(choices=yearchoice)
    password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    hostelchoice=[('Hosteller','Hosteller'),('DaysScholar','DaysScholar')]
    hostel_or_dayscholar=forms.ChoiceField(widget=forms.RadioSelect,choices=hostelchoice)
    quotachoice=[('Management Quota','Management Quota'),('Government Quota','Government Quota')]
    quota=forms.ChoiceField(widget=forms.RadioSelect,choices=quotachoice)



    class Meta:
        model=Studentinfomodel
        fields='__all__'