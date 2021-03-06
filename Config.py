# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Config', [dirname(__file__)])
        except ImportError:
            import _Config
            return _Config
        if fp is not None:
            try:
                _mod = imp.load_module('_Config', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Config = swig_import_helper()
    del swig_import_helper
else:
    import _Config
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class Config(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Config, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Config, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_sComps"] = _Config.Config_m_sComps_set
    __swig_getmethods__["m_sComps"] = _Config.Config_m_sComps_get
    if _newclass:
        m_sComps = _swig_property(_Config.Config_m_sComps_get, _Config.Config_m_sComps_set)
    __swig_setmethods__["m_nChem"] = _Config.Config_m_nChem_set
    __swig_getmethods__["m_nChem"] = _Config.Config_m_nChem_get
    if _newclass:
        m_nChem = _swig_property(_Config.Config_m_nChem_get, _Config.Config_m_nChem_set)
    __swig_setmethods__["m_mw"] = _Config.Config_m_mw_set
    __swig_getmethods__["m_mw"] = _Config.Config_m_mw_get
    if _newclass:
        m_mw = _swig_property(_Config.Config_m_mw_get, _Config.Config_m_mw_set)
    __swig_setmethods__["m_K_ow"] = _Config.Config_m_K_ow_set
    __swig_getmethods__["m_K_ow"] = _Config.Config_m_K_ow_get
    if _newclass:
        m_K_ow = _swig_property(_Config.Config_m_K_ow_get, _Config.Config_m_K_ow_set)
    __swig_setmethods__["m_pKa"] = _Config.Config_m_pKa_set
    __swig_getmethods__["m_pKa"] = _Config.Config_m_pKa_get
    if _newclass:
        m_pKa = _swig_property(_Config.Config_m_pKa_get, _Config.Config_m_pKa_set)
    __swig_setmethods__["m_frac_non_ion"] = _Config.Config_m_frac_non_ion_set
    __swig_getmethods__["m_frac_non_ion"] = _Config.Config_m_frac_non_ion_get
    if _newclass:
        m_frac_non_ion = _swig_property(_Config.Config_m_frac_non_ion_get, _Config.Config_m_frac_non_ion_set)
    __swig_setmethods__["m_frac_unbound"] = _Config.Config_m_frac_unbound_set
    __swig_getmethods__["m_frac_unbound"] = _Config.Config_m_frac_unbound_get
    if _newclass:
        m_frac_unbound = _swig_property(_Config.Config_m_frac_unbound_get, _Config.Config_m_frac_unbound_set)
    __swig_setmethods__["m_acid_base"] = _Config.Config_m_acid_base_set
    __swig_getmethods__["m_acid_base"] = _Config.Config_m_acid_base_get
    if _newclass:
        m_acid_base = _swig_property(_Config.Config_m_acid_base_get, _Config.Config_m_acid_base_set)
    __swig_setmethods__["m_partition_vehicle"] = _Config.Config_m_partition_vehicle_set
    __swig_getmethods__["m_partition_vehicle"] = _Config.Config_m_partition_vehicle_get
    if _newclass:
        m_partition_vehicle = _swig_property(_Config.Config_m_partition_vehicle_get, _Config.Config_m_partition_vehicle_set)
    __swig_setmethods__["m_diffu_vehicle"] = _Config.Config_m_diffu_vehicle_set
    __swig_getmethods__["m_diffu_vehicle"] = _Config.Config_m_diffu_vehicle_get
    if _newclass:
        m_diffu_vehicle = _swig_property(_Config.Config_m_diffu_vehicle_get, _Config.Config_m_diffu_vehicle_set)
    __swig_setmethods__["m_conc_vehicle"] = _Config.Config_m_conc_vehicle_set
    __swig_getmethods__["m_conc_vehicle"] = _Config.Config_m_conc_vehicle_get
    if _newclass:
        m_conc_vehicle = _swig_property(_Config.Config_m_conc_vehicle_get, _Config.Config_m_conc_vehicle_set)
    __swig_setmethods__["m_x_len_vehicle"] = _Config.Config_m_x_len_vehicle_set
    __swig_getmethods__["m_x_len_vehicle"] = _Config.Config_m_x_len_vehicle_get
    if _newclass:
        m_x_len_vehicle = _swig_property(_Config.Config_m_x_len_vehicle_get, _Config.Config_m_x_len_vehicle_set)
    __swig_setmethods__["m_area_vehicle"] = _Config.Config_m_area_vehicle_set
    __swig_getmethods__["m_area_vehicle"] = _Config.Config_m_area_vehicle_get
    if _newclass:
        m_area_vehicle = _swig_property(_Config.Config_m_area_vehicle_get, _Config.Config_m_area_vehicle_set)
    __swig_setmethods__["m_bInfSrc"] = _Config.Config_m_bInfSrc_set
    __swig_getmethods__["m_bInfSrc"] = _Config.Config_m_bInfSrc_get
    if _newclass:
        m_bInfSrc = _swig_property(_Config.Config_m_bInfSrc_get, _Config.Config_m_bInfSrc_set)
    __swig_setmethods__["m_n_layer_x_sc"] = _Config.Config_m_n_layer_x_sc_set
    __swig_getmethods__["m_n_layer_x_sc"] = _Config.Config_m_n_layer_x_sc_get
    if _newclass:
        m_n_layer_x_sc = _swig_property(_Config.Config_m_n_layer_x_sc_get, _Config.Config_m_n_layer_x_sc_set)
    __swig_setmethods__["m_n_layer_y_sc"] = _Config.Config_m_n_layer_y_sc_set
    __swig_getmethods__["m_n_layer_y_sc"] = _Config.Config_m_n_layer_y_sc_get
    if _newclass:
        m_n_layer_y_sc = _swig_property(_Config.Config_m_n_layer_y_sc_get, _Config.Config_m_n_layer_y_sc_set)
    __swig_setmethods__["m_offset_y_sc"] = _Config.Config_m_offset_y_sc_set
    __swig_getmethods__["m_offset_y_sc"] = _Config.Config_m_offset_y_sc_get
    if _newclass:
        m_offset_y_sc = _swig_property(_Config.Config_m_offset_y_sc_get, _Config.Config_m_offset_y_sc_set)
    __swig_setmethods__["m_n_grids_x_ve"] = _Config.Config_m_n_grids_x_ve_set
    __swig_getmethods__["m_n_grids_x_ve"] = _Config.Config_m_n_grids_x_ve_get
    if _newclass:
        m_n_grids_x_ve = _swig_property(_Config.Config_m_n_grids_x_ve_get, _Config.Config_m_n_grids_x_ve_set)
    __swig_setmethods__["m_n_grids_x_de"] = _Config.Config_m_n_grids_x_de_set
    __swig_getmethods__["m_n_grids_x_de"] = _Config.Config_m_n_grids_x_de_get
    if _newclass:
        m_n_grids_x_de = _swig_property(_Config.Config_m_n_grids_x_de_get, _Config.Config_m_n_grids_x_de_set)
    __swig_setmethods__["m_x_len_ve"] = _Config.Config_m_x_len_ve_set
    __swig_getmethods__["m_x_len_ve"] = _Config.Config_m_x_len_ve_get
    if _newclass:
        m_x_len_ve = _swig_property(_Config.Config_m_x_len_ve_get, _Config.Config_m_x_len_ve_set)
    __swig_setmethods__["m_x_len_de"] = _Config.Config_m_x_len_de_set
    __swig_getmethods__["m_x_len_de"] = _Config.Config_m_x_len_de_get
    if _newclass:
        m_x_len_de = _swig_property(_Config.Config_m_x_len_de_get, _Config.Config_m_x_len_de_set)
    __swig_setmethods__["m_partition_dermis2blood"] = _Config.Config_m_partition_dermis2blood_set
    __swig_getmethods__["m_partition_dermis2blood"] = _Config.Config_m_partition_dermis2blood_get
    if _newclass:
        m_partition_dermis2blood = _swig_property(_Config.Config_m_partition_dermis2blood_get, _Config.Config_m_partition_dermis2blood_set)
    __swig_setmethods__["m_Kclear_blood"] = _Config.Config_m_Kclear_blood_set
    __swig_getmethods__["m_Kclear_blood"] = _Config.Config_m_Kclear_blood_get
    if _newclass:
        m_Kclear_blood = _swig_property(_Config.Config_m_Kclear_blood_get, _Config.Config_m_Kclear_blood_set)
    __swig_setmethods__["m_n_grids_x_sb_sur"] = _Config.Config_m_n_grids_x_sb_sur_set
    __swig_getmethods__["m_n_grids_x_sb_sur"] = _Config.Config_m_n_grids_x_sb_sur_get
    if _newclass:
        m_n_grids_x_sb_sur = _swig_property(_Config.Config_m_n_grids_x_sb_sur_get, _Config.Config_m_n_grids_x_sb_sur_set)
    __swig_setmethods__["m_n_grids_y_sb_sur"] = _Config.Config_m_n_grids_y_sb_sur_set
    __swig_getmethods__["m_n_grids_y_sb_sur"] = _Config.Config_m_n_grids_y_sb_sur_get
    if _newclass:
        m_n_grids_y_sb_sur = _swig_property(_Config.Config_m_n_grids_y_sb_sur_get, _Config.Config_m_n_grids_y_sb_sur_set)
    __swig_setmethods__["m_n_grids_x_sb_har"] = _Config.Config_m_n_grids_x_sb_har_set
    __swig_getmethods__["m_n_grids_x_sb_har"] = _Config.Config_m_n_grids_x_sb_har_get
    if _newclass:
        m_n_grids_x_sb_har = _swig_property(_Config.Config_m_n_grids_x_sb_har_get, _Config.Config_m_n_grids_x_sb_har_set)
    __swig_setmethods__["m_n_grids_y_sb_har"] = _Config.Config_m_n_grids_y_sb_har_set
    __swig_getmethods__["m_n_grids_y_sb_har"] = _Config.Config_m_n_grids_y_sb_har_get
    if _newclass:
        m_n_grids_y_sb_har = _swig_property(_Config.Config_m_n_grids_y_sb_har_get, _Config.Config_m_n_grids_y_sb_har_set)
    __swig_setmethods__["m_x_len_sb_sur"] = _Config.Config_m_x_len_sb_sur_set
    __swig_getmethods__["m_x_len_sb_sur"] = _Config.Config_m_x_len_sb_sur_get
    if _newclass:
        m_x_len_sb_sur = _swig_property(_Config.Config_m_x_len_sb_sur_get, _Config.Config_m_x_len_sb_sur_set)
    __swig_setmethods__["m_y_len_sb_har"] = _Config.Config_m_y_len_sb_har_set
    __swig_getmethods__["m_y_len_sb_har"] = _Config.Config_m_y_len_sb_har_get
    if _newclass:
        m_y_len_sb_har = _swig_property(_Config.Config_m_y_len_sb_har_get, _Config.Config_m_y_len_sb_har_set)

    def ReadConfigFile(self, arg2):
        return _Config.Config_ReadConfigFile(self, arg2)

    def Tokenize(self, *args):
        return _Config.Config_Tokenize(self, *args)

    def __init__(self):
        this = _Config.new_Config()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _Config.delete_Config
    __del__ = lambda self: None
Config_swigregister = _Config.Config_swigregister
Config_swigregister(Config)

# This file is compatible with both classic and new-style classes.


