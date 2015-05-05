from django.conf import settings


def head_body_settings(request):
    # settings-file located code blocks to be inserted before closing 'head' and 'body' tags respectively
    context = dict()

    try:
        context['HEAD_CLOSING'] = settings.HEAD_CLOSING
    except AttributeError:
        pass

    try:
        context['BODY_CLOSING'] = settings.BODY_CLOSING
    except AttributeError:
        pass

    return context
