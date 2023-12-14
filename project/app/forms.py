from django import forms


class Product(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, label="Имя")
    surname = forms.CharField(label="Фамилия")
    email = forms.CharField(label="Почта")
    country = forms.CharField(label="Страна")
    city = forms.CharField(label="Город")
    street = forms.CharField(label="Улица")
    number_house = forms.CharField(label="Номер дома")
    apartment = forms.CharField(label="Квартира")



class UserForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)
    age = forms.IntegerField()

class NewsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(label='Текст')
    is_publisher = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ChoiceField(choices=((1,'Спорт'), (2, 'Красота'), (3,'Погода')))



class DownloadForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    url = forms.URLField(label='URL')
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    is_publisher = forms.BooleanField(label='Публикация', initial=True)
    category = forms.ChoiceField(choices=((1, 'Алабуга'), (2, 'Новостная'), (3, 'Погода')))


class news_form(forms.Form):
    name = forms.CharField()
    text = forms.CharField()