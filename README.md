# RI-complex-aqueous-solution

Calculate the real part of the refractive index of aquesous solutions containing orgnaic solutes and/or ions as a function of wavelength in the visible region and solute concentration using the effective oscillator model developed by Bain and Preston:

Bain, A., & Preston, T. C. (2020). The wavelength-dependent optical properties of weakly absorbing aqueous aerosol particles. Chemical Communications, 56, 8928–8931.https://doi.org/10.1039/d0cc02737e

Inorganic ions: NH_4^+, Ca^2+, Li^+, Mg^2+, Na^+, K^+, Cl^-, HSO_4^-, SO_4^2-, Br^-, NO_3^-, H^+

Organic solutes: Malonic acid, Glutaric acid, Citric acid, Tartaric acid, Sucrose, Mannose

Refractive index of pure water is taken from: Daimon, M., & Masumura, A. (2007). Measurement of the refractive index of distilled water from the near-infrared region to the ultraviolet region. Applied Optics, 46(18), 3811. https://doi.org/10.1364/AO.46.003811

Input parameters:

solutes: for inorganic solutes each ion is entered individually, . solute mass fraction: for inorganic solutes the mass fraction of each ion is entered individually. Example: input=[['NH4',0.0546],['SO4',0.14539],['tartaric acid',0.2]]

wavelength: wavelength in micrometers at which the refractive index will be calcualted (Na D-line = 0.589 micrometers) Can accept a single wavelength or an array of wavelengths: Example for 2 discrete wavlenghts: wavelength=np.array([0.589,0.650]) Example for a range of wavelengths: wavelength=np.linspace(0.3,0.7,5,endpoint=True)

Import Oscillator data for solute: Ion oscillator parameter are in 'oscillator-parameters.txt' file. Change the file path to wherever this is saved. file=(".../oscillator-parameters.txt") #full path for file

OutPut parameters:

Output file name and location. Output will be in .csv format. Change the name of the output directory and the base file name Name of output directory: dir_name='' Base file name: base_filename=''
