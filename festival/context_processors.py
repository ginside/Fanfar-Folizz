from inspect import stack, getmodule

def get_module_name(request):
    """Template context with current_view value,
    a string with the full namespaced django view in use.
    """
    context = {}
    name = getmodule(stack()[2][0]).__name__
    context['current_view'] = "%s.%s" % (name, stack()[2][3])
    context['current_module'] = name.split('.')[0]
    return context