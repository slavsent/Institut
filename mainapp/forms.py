from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget

from mainapp import models as mainapp_models


class CreateCardStudentForm(forms.ModelForm):
    pass


class EditCardStudentForm(forms.ModelForm):
    class Meta:
        model = mainapp_models.CardStudent
        fields = ("student", "id_student", "name")
        widgets = {
            "student": forms.HiddenInput(),
            "id_student": forms.TextInput,
            "name": forms.TextInput,
        }

'''
class FotoFeedbackForm(forms.ModelForm):
    def __init__(self, *args, foto=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if foto and user:
            self.fields["foto"].initial = foto.pk
            self.fields["user"].initial = user.pk
        return ret

    class Meta:
        model = mainapp_models.Likes
        fields = ("foto", "user", "feedback", "on_like")
        widgets = {
            "foto": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "on_like": forms.RadioSelect(attrs={'class': 'inline'}),
        }


class MailFeedbackForm(forms.Form):
    user_id = forms.UUIDField(widget=forms.HiddenInput)
    message = forms.CharField(
        widget=forms.Textarea,
        help_text=_("Enter your message"),
        label=_("Message"),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields["user_id"].initial = user.pk


class CreateFotoForm(forms.ModelForm):
    class Meta:
        model = mainapp_models.Foto
        fields = ("name", "name_en", "description", "description_en", "path_foto_my")
        #widgets = {
        #    "id": forms.HiddenInput()
        #}


class CreateNewsForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    ret = super().__init__(*args, **kwargs)
    #    self.fields["id"].initial = value
    #    return ret

    class Meta:
        model = mainapp_models.News

        fields = ("id", "title", "title_en", "preambule", "preambule_en", "body", "body_en")
        widgets = {
            "id": forms.HiddenInput()
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class FilterNewsForm(forms.Form):
    datefrom = forms.DateField(widget=DateInput, label="Дата от")
    dateto = forms.DateField(widget=DateInput, label="Дата до")
    '''
