from parametric_simulation import run_one_parameter_parametric
from post_processor import plot_1D_results

eplus_run_path = 'home/ssyrl6/UNNC-F22-ABEE1025-Group-13-'
idf_path = 'home/ssyrl6/UNNC-F22-ABEE1025-Group-13-/1ZoneUncontrolled_win_1.idf'
output_dir = 'param_exp_1'
parameter_key = ['WindowMaterial: SimpleGlazingSystem',
				'SimpleWindow: DOUBLE PANE WINDOW',
				'solar_heat_gain_coefficent']
parameter_vals = [0.25, 0.27, 0.29, 0.31, 0.33, 0.35, 0.37,
				0.39, 0.41, 0.43, 0.45, 0.47, 0.49, 0.51,
				0.53, 0.55, 0.57, 0.59, 0.61, 0.63, 0.65,
				0.67, 0.69, 0.71, 0.73, 0.75]
plot_column_name = 'ZONE ONE: Zone Mean Air Temperature [C](TimeStep)'
y_axis_title = 'Indoor Air Temperature (C)'
plot_title = 'Simulation of Indoor Air Temperature vs. SHGC'
output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
								parameter_key, parameter_vals)

print(output_paths)
plot_1D_results(output_paths, plot_column_name,
				y_axis_title, plot_title)