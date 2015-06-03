from django import template
import json
register = template.Library()

@register.inclusion_tag('admin_highcharts/js.html')
def highcharts_for_result(cl):
    def get_verbose_name(name):
        for item in  cl.model._meta.fields:
            if item.name==name:
                return item.verbose_name
        try:
            func = getattr(cl.model_admin,name)
            return func.short_description
        except AttributeError:
            pass
    def get_attr(obj,name):
        if type(obj) is dict:
            return obj[name]
        else:
            try:
                return getattr(obj, name)
            except AttributeError:
                func = getattr(cl.model_admin,name)
                return func(obj)
    def get_names():       
        category_name = cl.model_admin.list_display[0] if not hasattr(cl.model_admin, 'chart_category_name') else cl.model_admin.chart_category_name
        if hasattr(cl.model_admin,'chart_serial_names'):
            serial_names = cl.model_admin.chart_serial_names
        else:
            serial_names = []
            for name in cl.model_admin.list_display:
                if name==category_name:
                    continue
                serial_names.append(name)
        return category_name,serial_names
    category_name,serial_names = get_names()
    chart_type = 'line' if not hasattr(cl.model_admin, 'chart_type') else cl.model_admin.chart_type
    categories = []
    for item in cl.result_list:
        categories.append(get_attr(item,category_name))
    series = []
    for key in serial_names:
        data = []
        for item in cl.result_list:
            data.append(get_attr(item,key))
        series.append({
                       'name':get_verbose_name(key),
                       'data':data,
                       })
    result = {
              'categories':categories,
              'series':series,
              'type':chart_type,
              'option':json.dumps(cl.model_admin.chart_option),
    }
    return result
