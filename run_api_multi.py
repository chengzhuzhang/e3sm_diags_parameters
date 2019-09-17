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
prefix = '/compyfs/www/zhan429/run_with_api'
param.results_dir = os.path.join(prefix, 'multiple')
#param.results_dir = os.path.join(prefix, 'all_sets_ANN')

##Set specific parameters for new sets
#zm2d_param = ZonalMean2dParameter()
#
##Set specific parameters for new sets
#mm2d_param = MeridionalMean2dParameter()

# Set specific parameters for new sets
ts_param = AreaMeanTimeSeriesParameter()
ts_param.reference_data_path = '/compyfs/e3sm_diags_data/obs_for_e3sm_diags/time-series/'
ts_param.test_data_path = '/compyfs/e3sm_diags_data/test_model_data_for_acme_diags/time-series/E3SM_v1/'
ts_param.test_name = 'e3sm_v1'
#ts_param.test_timeseries_input = True
ts_param.test_start_yr = '2002'
ts_param.test_end_yr = '2008'
#ts_param.ref_timeseries_input = True
ts_param.ref_start_yr = '2002'
ts_param.ref_end_yr = '2008'

print('*******************************')

attrs = vars(param)
print (', '.join("%s: %s" % item for item in attrs.items()))

attrs = vars(ts_param)
print (', '.join("%s: %s" % item for item in attrs.items()))

# We're passing in this new object as well, in
# addtion to the CoreParameter object.
# runner.sets_to_run = ['lat_lon', 'area_mean_time_series']
# runner.run_diags([param, ts_param])
runner.sets_to_run = ['lat_lon','zonal_mean_xy', 'zonal_mean_2d', 'polar', 'cosp_histogram', 'meridional_mean_2d', 'area_mean_time_series']
#runner.sets_to_run = ['lat_lon' , 'polar', 'area_mean_time_series']
#runner.sets_to_run = ['lat_lon', 'area_mean_time_series']
runner.run_diags([param, ts_param])
