from django import forms
from .models import Contact, Book, Publisher
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Submit, Layout, ButtonHolder, HTML


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


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('year'),
            ),
            Row(
                Column('description'),
            ),
            Row(
                Column('publisher'),
            ),
            Row(
                HTML("""<a class="classes-for-styling" href="{% url 'addpublisher' %}">Add a new Publisher</a>"""),
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class="btn btn-primary"),
            ),
        )


class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('country'),
            ),
            Row(
                Column('address'),
            ),
            Row(
                Submit('submit', 'Submit', css_class="btn btn-primary"),
            ),
        )
