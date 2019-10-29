python run_e3sm_diags_hist_all.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_hist_r1-5_atm' -d area_mean_time_series_model_vs_model_cmip_amon.cfg
python run_e3sm_diags_hist_all.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_hist_r1-5_ocean' -d area_mean_time_series_model_vs_model_cmip_omon.cfg
python run_e3sm_diags_hist_all.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_hist_r1-5_land' -d area_mean_time_series_model_vs_model_cmip_lmon.cfg
python run_e3sm_diags_amip_all.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_amip_r1-3_atm' -d area_mean_time_series_model_vs_model_cmip_amon.cfg
python run_e3sm_diags_amip_all.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_amip_r1-3_land' -d area_mean_time_series_model_vs_model_cmip_lmon.cfg
python run_e3sm_diags_piControl.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_piControl_atm' -d area_mean_time_series_model_vs_model_cmip_amon.cfg
python run_e3sm_diags_piControl.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_piControl_ocean' -d area_mean_time_series_model_vs_model_cmip_omon.cfg
python run_e3sm_diags_piControl.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_piControl_land' -d area_mean_time_series_model_vs_model_cmip_lmon.cfg
python run_e3sm_diags_CO2.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_CO2_atm' -d area_mean_time_series_model_vs_model_cmip_amon.cfg
python run_e3sm_diags_CO2.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_CO2_ocean' -d area_mean_time_series_model_vs_model_cmip_omon.cfg
python run_e3sm_diags_CO2.py --results_dir '/var/www/acme/acme-diags/zhang40/cmip_20191014/area_mean_CO2_land' -d area_mean_time_series_model_vs_model_cmip_lmon.cfg


