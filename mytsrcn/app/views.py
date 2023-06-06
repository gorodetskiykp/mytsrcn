from django.shortcuts import render
from .models import Menu


def index(request):
    template = 'app/index.html'
    context = {
        'title': 'Семейный центр помощи семье и детям «Мытищинский»',
        'hello': 'Добро пожаловать <br />на сайт Государственного казенного учреждения социального обслуживания Московской области Семейный центр помощи семье и детям «Мытищинский»',
        'intro': """
            <p>На базе нашего учреждения, <b>каждый четверг, с 10.00 до 12.00</b> вы можете получить <b>бесплатную юридическую консультацию</b> по гражданско-правовым вопросам.</p>
            <p>Приём ведётся по предварительной записи по адресу: <b>г. Мытищи, ул. Юбилейная, д. 39</b>. Контактный телефон: <b>8-495-582-54-11</b></p>
            <p>Время приёма в выходные дни – по согласованию.</p>
        """,
        'booking': """
            <p>Для записи на <u>онлайн-консультацию к психологу</u> посредством платформы Zoom необходимо связаться по телефону 8-495-582-54-11, либо заполнить заявку на сайте по кнопке ниже.</p>
        """,
    }
    return render(request, template, context)


def category(request, pk):
    cat = Menu.objects.get(pk=pk)
    if cat.slug == 'news':
        return news(request)
    elif cat.slug == 'index':
        return index(request)
    template = 'app/index.html'
    context = {
        'title': 'Заголовок',
        'content': 'Содержимое' + str(pk),
    }
    return render(request, template, context)


def news(request):
    template = 'app/news.html'
    context = {
        'title': 'Новости',
        'content': 'Новости',
    }
    return render(request, template, context)
