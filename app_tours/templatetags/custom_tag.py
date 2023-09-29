from django.template.defaulttags import register

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]


@register.filter(name='concatenate')
def concatenate(value, arg):
    return f"{value}{arg}"
