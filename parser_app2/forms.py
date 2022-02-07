from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('CARTOON','CARTOON'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'CARTOON':
            cartoon_parser = parser.parser()
            for i in cartoon_parser:
                models.Cartoon.objects.create(**i)
