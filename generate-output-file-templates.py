#!/usr/bin/python
#
# Prepare files containing optimized subsets of columns for distribution on the 
#   Earth System Grid 
#
# Robert Pincus, Robert.Pincus@colorado.edu, 2016-2017
#
# ---------------------------------------------------------------------------------
from netCDF4 import Dataset  
# ---------------------------------------------------------------------------------
# Copy a variable and all its attributes from one netCDF file to another 
#
def copyVar(nc_in, nc_out, name, newname=None) :   
	if newname is None : 
		newname = name
	nc_out.createVariable(newname, nc_in.variables[name].dtype, nc_in.variables[name].dimensions) 
	nc_out.variables[newname].setncatts(nc_in.variables[name].__dict__)
	nc_out.variables[newname][:] = nc_in.variables[name][:] 
# ---------------------------------------------------------------------------------

atmos_file = Dataset('multiple_input4MIPs_radiation_RFMIP_UColorado-RFMIP-0-4_none.nc', mode='r') 

short_names = ['rlu','rsu', 'rld', 'rsd'] 
stand_names = ['upwelling_longwave_flux_in_air','upwelling_shortwave_flux_in_air', 
               'downwelling_longwave_flux_in_air','downwelling_shortwave_flux_in_air'] 

               
for short, std in zip(short_names, stand_names) : 
    out_file_name = short + "_template.nc"
    print('Creating ' + out_file_name)
    out_file = Dataset(out_file_name, mode='w', FORMAT='NETCDF4_CLASSIC')
    out_file.setncatts({
       'title':'',
       'institution_id':'', 
       'institution'   :'', 
       'activity_id'   :'CMIP', 
       'Conventions'   :'CF-1.6',  
       'creation_date' :'', 
       'realm'         :'atmos', 
       'data_structure':'sites',  
       'source'        :'', 
       'source_id'     :'',
       'history'       :'',
       'contact'       :'', 
       'references'    :'', 
       'dataset_category'      :'radiation',
       'dataset_version_number':'',
       'further_info_url'      :'',
       'mip_era'       :'CMIP6',
       'target_mip'    :'RFMIP',
       'grid_label'    :'none',
       'license':''})
    d = out_file.createDimension('expt',  atmos_file.dimensions['expt'].size) 
    d = out_file.createDimension('site',  atmos_file.dimensions['site'].size) 
    d = out_file.createDimension('level', atmos_file.dimensions['level'].size) 
    copyVar(atmos_file, out_file, 'lat') 
    copyVar(atmos_file, out_file, 'lon') 
    copyVar(atmos_file, out_file, 'time') 
    copyVar(atmos_file, out_file, 'pres_level', 'plev') 
    v = out_file.createVariable(short,   'f4', ('expt', 'site', 'level')) 
    v.setncatts({'standard_name':std, 
                 'units'        :'W m-2', 
                 'coordinates'  : 'lon lat time'}) 
    copyVar(atmos_file, out_file, 'profile_weight') 
    out_file.close()


