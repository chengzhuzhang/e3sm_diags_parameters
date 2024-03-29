import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter
from acme_diags.parameter.zonal_mean_2d_parameter import ZonalMean2dParameter

from acme_diags.run import runner

param = CoreParameter()

param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/climatology/'
param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/climatology/'
param.test_name = '20161118.beta0.FC5COSP.ne30_ne30.edison'
param.seasons = ["ANN"]
param.multiprocessing = True
param.num_workers = 40
prefix = '/compyfs/www/zhan429/tests'
param.results_dir = os.path.join(prefix, 'all_sets')

#
##Set specific parameters for new sets
ts_param = AreaMeanTimeSeriesParameter()
ts_param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/time-series/'
ts_param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/time-series/E3SM_v1/'
ts_param.test_name = 'e3sm_v1'
ts_param.start_yr = '2002'
ts_param.end_yr = '2008'

runner.sets_to_run = ['lat_lon','zonal_mean_xy', 'zonal_mean_2d', 'polar', 'cosp_histogram', 'meridional_mean_2d', 'area_mean_time_series']
runner.run_diags([param, ts_param])

#runner.sets_to_run = ['area_mean_time_series']
#runner.run_diags([param, ts_param])
