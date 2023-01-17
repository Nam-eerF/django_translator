from django.shortcuts import render
from googletrans import Translator

from .forms import TranslateForm


def translator_view(request):
    if request.method == 'GET':
        form = TranslateForm()
        return render(request, 'translator/translator.html', context={'form': form})
    else:
        form = TranslateForm(request.POST)
        lang_from = request.POST.get('lang_from')
        lang_to = request.POST.get('lang_to')
        text_from = request.POST.get('text')

        translator = Translator()

        try:
            result = translator.translate(text_from, src=lang_from, dest=lang_to)
        except Exception as e:
            result = ''
            print(e)

        context = {'translate_text': result.text, 'form': form}
        return render(request, 'translator/translator.html', context=context)
