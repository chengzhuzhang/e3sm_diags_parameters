import os
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter
from acme_diags.run import runner

param = CoreParameter()

#For compy
#machine_path_prefix = '/compyfs/e3sm_diags_data/'
#For cori
#machine_path_prefix = '/global/project/projectdirs/acme/acme_diags'
#for acme1
machine_path_prefix = '/p/user_pub/e3sm/e3sm_diags_data/'

#param.reference_data_path = os.path.join(machine_path_prefix, 'obs_for_e3sm_diags/time-series/')
#param.test_data_path = os.path.join(machine_path_prefix, 'test_model_data_for_acme_diags/time-series/CESM1-CAM5_cmip/')
param.reference_data_path = '/p/user_pub/e3sm/zhang40/e3sm_cmip6_xmls/v1_water_cycle/historical/'
param.test_data_path = '/p/user_pub/e3sm/zhang40/e3sm_cmip6_xmls/v1_water_cycle/historical/r1i1p1f1'
param.test_name = 'e3sm_v1_hist_r1'

#For compy
#prefix = '/compyfs/www/zhan429/doc_examples/'
#For cori
#prefix = '/global/project/projectdirs/acme/www/zhang40/'
#For acme1
prefix = '/var/www/acme/acme-diags/zhang40/tests/'
param.results_dir = os.path.join(prefix, 'area_mean_hist_r1-5')
param.multiprocessing = True
param.num_workers =  25

# We're passing in this new object as well, in
# addition to the CoreParameter object.

ts_param = AreaMeanTimeSeriesParameter()
ts_param.ref_names = ['r2i1p1f1', 'r3i1p1f1', 'r4i1p1f1', 'r5i1p1f1']   #This setting plot model data only
ts_param.start_yr = '1850'
ts_param.end_yr = '2014'

runner.sets_to_run = ['area_mean_time_series']
runner.run_diags([param, ts_param])


