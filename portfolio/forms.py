from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Submit, Layout, ButtonHolder, Fieldset
from crispy_forms.bootstrap import FormActions


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('email'),
            ),
            Row(
                Column('phone'),
            ),
            Row(
                Column('message'),
            ),
            Row(
                Submit('submit', 'Submit', css_class="btn btn-primary"),
            ),
        )

