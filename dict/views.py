# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def entry_list(request):
    return render(request, 'dict/entry_list.html', {})
