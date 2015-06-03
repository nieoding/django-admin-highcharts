django-admin-highcharts/README.rst
=====
admin-highcharts
=====

help to add highcharts in django admin 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "admin_highcharts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'admin_highcharts',
    )
2. add highchart to admin your app model,for example::

	your model defined(models.py)
	class MyStats(models.Model):
		stats_date = models.DateField()
		pv = models.IntegerField()
		uv = models.IntegerField()
		
	admin your model(admins.py)
	from django.contrib import admin
	from .models import MyStats
	from admin_highcharts.admin import HighchartsModelAdmin
	admin.site.register(MyStats,HighchartsModelAdmin,list_display=('stats_date','pv','uv'))

3. advance method in HighchartsModelAdmin::

    chart_category_name:
        default -> the first elem in list_display,you can set manual
    chart_serial_names:
        default -> list_display exclude chart_category_name,you can set manual
    chart_type:
        default -> line
        options: line,column,area,areaspline,spline,
	for example:
	admin.site.register(MyStats,HighchartsModelAdmin,list_display=('pv','uv','stats_date'),chart_serial_names=('uv',))
	or
	@admin.register(MyStats)
	class MyStatsAdmin(HighchartsModelAdmin):
		list_display=('pv','uv','stats_date')
		chart_serial_names=('uv',)