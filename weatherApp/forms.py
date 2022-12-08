from django.contrib.gis import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Weather, Location
from .widgets import DatePickerInput


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LocationRequestForm(forms.ModelForm):
    city = forms.CharField(max_length=50,)
    location = forms.PointField(widget=forms.OSMWidget(
            attrs={'map_width': 800,
                   'map_height': 600,
                   'template_name': 'gis/openlayers-osm.html',
                   'default_zoom': 8,
                   'default_lat': 10.82,        # default location on map - Saigon, Vietnam :)
                   'default_lon': 106.62,
                   }))

    class Meta:
        model = Location
        fields = ('city', 'location',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].required = False
        self.fields["location"].required = False


# 'template_name': 'gis/openlayers-osm.html',
# 'default_lat': 42.1710962,
# 'default_lon': 18.8062112,
# 'default_zoom': 6

class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('favourite',)

    favourite = forms.BooleanField()


class DateRequestForm(forms.ModelForm):
    date_from = forms.DateField(
        label="Date or date from",
        widget=DatePickerInput(),
        help_text="Select date from",
    )
    date_to = forms.DateField(label="Date to", widget=DatePickerInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_from"].required = True
        self.fields["date_to"].required = True

    class Meta:
        model = Weather
        fields = ('date',)
