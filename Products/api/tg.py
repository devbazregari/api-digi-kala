def get_queryset(self):
    entries = [x for x in Entry.objects.all() if x.publications]
    return entries



def_entries = [x.pk for x in Entry.objects.all() if x.publications]
entries = Entry.objects.filter(pk__in=def_entries)
return entries