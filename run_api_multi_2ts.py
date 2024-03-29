import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter
from acme_diags.run import runner

param = CoreParameter()


param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/time-series/'
param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/time-series/E3SM_v1/'

param.test_name = 'e3sm_v1'
param.seasons = ["ANN"]  #seasons shouldn't be a parameter for area_mean_time_series, need to investigate while uncomment this line won't work
#param.seasons = []  #seasons shouldn't be a parameter for area_mean_time_series, need to investigate while uncomment this line won't work
param.test_timeseries_input = True
param.test_start_yr = '1998'
param.test_end_yr = '2004'
param.ref_timeseries_input = True
param.ref_start_yr = '1998'
param.ref_end_yr = '2004'

param.multiprocessing = True
param.num_workers = 40
prefix = '/compyfs/www/zhan429/tests'
param.results_dir = os.path.join(prefix, 'multiple_sets_2ts')


# Set specific parameters for new sets
ts_param = AreaMeanTimeSeriesParameter()
ts_param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/time-series/'
ts_param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/time-series/E3SM_v1/'
ts_param.test_name = 'e3sm_v1'
#ts_param.ref_names = ['none']
ts_param.start_yr = '1998'
ts_param.end_yr = '2008'

# We're passing in this new object as well, in
# addtion to the CoreParameter object.
# runner.sets_to_run = ['lat_lon', 'area_mean_time_series']
# runner.run_diags([param, ts_param])
runner.sets_to_run = ['lat_lon', 'area_mean_time_series']
runner.run_diags([param, ts_param])
