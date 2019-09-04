import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter

from acme_diags.run import runner

param = CoreParameter()

#For compy
machine_path_prefix = '/compyfs/e3sm_diags_data/'
#For cori
#machine_path_prefix = '/global/project/projectdirs/acme/acme_diags'

param.reference_data_path = os.path.join(machine_path_prefix, 'obs_for_e3sm_diags/time-series/')
param.test_data_path = os.path.join(machine_path_prefix, 'test_model_data_for_acme_diags/time-series/E3SM_v1/')

param.test_name = 'e3sm_v1'
#param.seasons = ["ANN"]  #seasons shouldn't be a parameter for area_mean_time_series, need to investigate while uncomment this line won't work
param.test_timeseries_input = True
param.test_start_yr = '2002'
param.test_end_yr = '2008'
param.ref_timeseries_input = True
param.ref_start_yr = '2002'
param.ref_end_yr = '2008'
prefix = '/compyfs/www/zhan429/run_with_api/'
param.results_dir = os.path.join(prefix, 'area_mean_no_refs')
print(param.results_dir)

#ts_param = AreaMeanTimeSeriesParameter()
#ts_param.ref_names = []
#ts_param.results_dir = '/compyfs/www/zhan429/run_with_api/area_mean_no_refs'
#print(dir(ts_param))
#print(ts_param.results_dir)

#param.multiprocessing = True
#param.num_workers =  40

# We're passing in this new object as well, in
# addtion to the CoreParameter object.

runner.sets_to_run = ['area_mean_time_series']
runner.run_diags([param])
#runner.run_diags([param,ts_param])


