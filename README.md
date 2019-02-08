# RFMIP-IRF-Scripts

This Python script generates empty ESGF- and CMIP6-compliant files for offline radiative transfer calculations. The script uses the netCDF4 module. 

The script requires the RFMIP-IRF input profiles from the [input4MIPs site](https://esgf-node.llnl.gov/search/input4mips/?institution_id=UColorado&target_mip_list=RFMIP).

Users will also want to edit the model-specific information starting on line 30 of the script, being careful to follow the CMIP6 Controlled Vocabulary entries for their model and institution. It would also be reasonable to update the "create_date" attribute when wrtiting data to the file, being careful to preserve the required formatting. 
