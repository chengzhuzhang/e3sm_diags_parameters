import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter

from acme_diags.run import runner

param = CoreParameter()

#For compy
machine_path_prefix = '/compyfs/e3sm_diags_data/'
#For cori
#machine_path_prefix = '/global/project/projectdirs/acme/acme_diags'

param.test_data_path = os.path.join(machine_path_prefix, 'test_model_data_for_acme_diags/time-series/E3SM_v1_historical_r1/')
#param.reference_data_path = os.path.join(machine_path_prefix, 'obs_for_e3sm_diags/time-series/')
param.reference_data_path = os.path.join(machine_path_prefix, 'test_model_data_for_acme_diags/time-series/')
param.test_name = 'e3sm_v1'
param.rune_type = 'model-vs-model'

prefix = '/compyfs/www/zhan429/examples/'
param.results_dir = os.path.join(prefix, 'area_mean_with_models')
param.multiprocessing = True
param.num_workers =  40

# We're passing in this new object as well, in
# addtion to the CoreParameter object.

ts_param = AreaMeanTimeSeriesParameter()
ts_param.ref_names = ['E3SM_v1_historical_r2', 'E3SM_v1_historical_r3', 'E3SM_v1_historical_r4', 'E3SM_v1_historical_r5']   #This setting plot model data only
ts_param.start_yr = '1850'
ts_param.end_yr = '2014'

runner.sets_to_run = ['area_mean_time_series']
runner.run_diags([param, ts_param])


