from django.contrib import admin
from django.utils.translation import ugettext as _

'''
    chart_category_name:
        default -> the first elem in list_display,you can set manual
    chart_serial_names:
        default -> list_display exclude chart_category_name,you can set manual
    chart_type:
        default -> line
        options: line,column,area,areaspline,spline,
            
'''

class HighchartsModelAdmin(admin.ModelAdmin):
    class Media():
        js = (
              'admin_highcharts/js/jquery-2.0.2.js',
              'admin_highcharts/js/highcharts.js',
              'admin_highcharts/js/exporting.js',
              )
    @property
    def chart_option(self):
        return {
                'credits':False,
                'lang':
                 {
                  'contextButtonTitle':_('contextButtonTitle'),
                  'downloadJPEG':_('downloadJPEG'),
                  'downloadPDF':_('downloadPDF'),
                  'downloadPNG':_('downloadPNG'),
                  'downloadSVG':_('downloadSVG'),
                  'printChart':_('printChart'),
                 },
                }
    @property
    def change_list_template(self):
        return 'admin_highcharts/change_list.html'