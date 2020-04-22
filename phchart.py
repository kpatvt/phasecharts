import CoolProp
from CoolProp.Plots import PropertyPlot

type_of_chart = 'PH'
for fl in ['Oxygen', 'Nitrogen', 'Argon']:
    th_plot = PropertyPlot(fl, type_of_chart, unit_system='EUR')
    th_plot.title('Pressure-Enthalpy Chart for ' + fl)
    th_plot.axis.set_yscale('log')
    th_plot.calc_isolines()
    th_plot.savefig(fl+'_'+type_of_chart+'.pdf')
