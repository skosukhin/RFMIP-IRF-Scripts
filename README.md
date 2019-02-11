# RFMIP-IRF-Scripts

This Python script generates empty ESGF- and CMIP6-compliant files for offline radiative transfer calculations. The script uses the netCDF4 module. 

The script requires the RFMIP-IRF input profiles from the [input4MIPs site](https://esgf-node.llnl.gov/search/input4mips/?institution_id=UColorado&target_mip_list=RFMIP). Get help with the --help flag to the script. 

The script takes three optional arguments: 
```
  --source_id SOURCE_ID
                        Source ID, must match CMIP Controlled Vocabulary at
                        https://github.com/WCRP-
                        CMIP/CMIP6_CVs/blob/master/CMIP6_source_id.json
  --forcing_index FORCING_INDEX
                        Forcing index (1 = all available greenhouse gases; 2 =
                        CO2, CH4, N2O, CFC11eq; 3 = CO2, CH4, N2O, CFC12eq,
                        HFC-134eq)
  --physics_index PHYSICS_INDEX
                        Physics index, e.g. for different approximations
```
If no arguments are provided the script produces files for `LBLRTM-12-8`. 

It would  be reasonable to update the "create_date" attribute when writing data to the file, being careful to preserve the required formatting. 

If you are publishing the data on the ESGF (rather than providing it to a publisher) recall that the directory structure needs to follow the conventions described in the [CMIP6 conventions document](https://goo.gl/v1drZl)

Directory structure =
<mip_era>/
<activity_id>/
<institution_id>/
<source_id>/
<experiment_id>/
<member_id>/
<table_id>/
<variable_id>/
<grid_label>/
<version>

Note:

<version> has the form “vYYYYMMDD” (e.g., “v20160314”), indicating a representative date for the version.   Note that files contained in a single <version>  subdirectory at the end of the directory path should represent all the available time-samples reported from the simulation; a time-series can be split across several files, but all the files must be found in the same subdirectory.  This implies that <version> will not generally be the actual date that all files in the subdirectory were written or published.

So an example directory will be:   CMIP6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f1/Efx/rlu/gn/v20190215/
