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
            fp, pathname, description = imp.find_module('_Skin_Setup', [dirname(__file__)])
        except ImportError:
            import _Skin_Setup
            return _Skin_Setup
        if fp is not None:
            try:
                _mod = imp.load_module('_Skin_Setup', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Skin_Setup = swig_import_helper()
    del swig_import_helper
else:
    import _Skin_Setup
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



def new_doubleP():
    return _Skin_Setup.new_doubleP()
new_doubleP = _Skin_Setup.new_doubleP

def copy_doubleP(value):
    return _Skin_Setup.copy_doubleP(value)
copy_doubleP = _Skin_Setup.copy_doubleP

def delete_doubleP(obj):
    return _Skin_Setup.delete_doubleP(obj)
delete_doubleP = _Skin_Setup.delete_doubleP

def doubleP_assign(obj, value):
    return _Skin_Setup.doubleP_assign(obj, value)
doubleP_assign = _Skin_Setup.doubleP_assign

def doubleP_value(obj):
    return _Skin_Setup.doubleP_value(obj)
doubleP_value = _Skin_Setup.doubleP_value
class Reaction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Reaction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Reaction, name)
    __repr__ = _swig_repr
    __swig_setmethods__["idx_substrate"] = _Skin_Setup.Reaction_idx_substrate_set
    __swig_getmethods__["idx_substrate"] = _Skin_Setup.Reaction_idx_substrate_get
    if _newclass:
        idx_substrate = _swig_property(_Skin_Setup.Reaction_idx_substrate_get, _Skin_Setup.Reaction_idx_substrate_set)
    __swig_setmethods__["idx_product"] = _Skin_Setup.Reaction_idx_product_set
    __swig_getmethods__["idx_product"] = _Skin_Setup.Reaction_idx_product_get
    if _newclass:
        idx_product = _swig_property(_Skin_Setup.Reaction_idx_product_get, _Skin_Setup.Reaction_idx_product_set)
    __swig_setmethods__["Vmax"] = _Skin_Setup.Reaction_Vmax_set
    __swig_getmethods__["Vmax"] = _Skin_Setup.Reaction_Vmax_get
    if _newclass:
        Vmax = _swig_property(_Skin_Setup.Reaction_Vmax_get, _Skin_Setup.Reaction_Vmax_set)
    __swig_setmethods__["Km"] = _Skin_Setup.Reaction_Km_set
    __swig_getmethods__["Km"] = _Skin_Setup.Reaction_Km_get
    if _newclass:
        Km = _swig_property(_Skin_Setup.Reaction_Km_get, _Skin_Setup.Reaction_Km_set)

    def __init__(self):
        this = _Skin_Setup.new_Reaction()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _Skin_Setup.delete_Reaction
    __del__ = lambda self: None
Reaction_swigregister = _Skin_Setup.Reaction_swigregister
Reaction_swigregister(Reaction)

class CompIdx(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CompIdx, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CompIdx, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _Skin_Setup.CompIdx_type_set
    __swig_getmethods__["type"] = _Skin_Setup.CompIdx_type_get
    if _newclass:
        type = _swig_property(_Skin_Setup.CompIdx_type_get, _Skin_Setup.CompIdx_type_set)
    __swig_setmethods__["pComp"] = _Skin_Setup.CompIdx_pComp_set
    __swig_getmethods__["pComp"] = _Skin_Setup.CompIdx_pComp_get
    if _newclass:
        pComp = _swig_property(_Skin_Setup.CompIdx_pComp_get, _Skin_Setup.CompIdx_pComp_set)

    def __init__(self):
        this = _Skin_Setup.new_CompIdx()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _Skin_Setup.delete_CompIdx
    __del__ = lambda self: None
CompIdx_swigregister = _Skin_Setup.CompIdx_swigregister
CompIdx_swigregister(CompIdx)

class Skin(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Skin, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Skin, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_concVehicleInit"] = _Skin_Setup.Skin_m_concVehicleInit_set
    __swig_getmethods__["m_concVehicleInit"] = _Skin_Setup.Skin_m_concVehicleInit_get
    if _newclass:
        m_concVehicleInit = _swig_property(_Skin_Setup.Skin_m_concVehicleInit_get, _Skin_Setup.Skin_m_concVehicleInit_set)
    __swig_setmethods__["m_dz_dtheta"] = _Skin_Setup.Skin_m_dz_dtheta_set
    __swig_getmethods__["m_dz_dtheta"] = _Skin_Setup.Skin_m_dz_dtheta_get
    if _newclass:
        m_dz_dtheta = _swig_property(_Skin_Setup.Skin_m_dz_dtheta_get, _Skin_Setup.Skin_m_dz_dtheta_set)
    __swig_setmethods__["m_x_length"] = _Skin_Setup.Skin_m_x_length_set
    __swig_getmethods__["m_x_length"] = _Skin_Setup.Skin_m_x_length_get
    if _newclass:
        m_x_length = _swig_property(_Skin_Setup.Skin_m_x_length_get, _Skin_Setup.Skin_m_x_length_set)
    __swig_setmethods__["m_y_length"] = _Skin_Setup.Skin_m_y_length_set
    __swig_getmethods__["m_y_length"] = _Skin_Setup.Skin_m_y_length_get
    if _newclass:
        m_y_length = _swig_property(_Skin_Setup.Skin_m_y_length_get, _Skin_Setup.Skin_m_y_length_set)
    __swig_setmethods__["m_x_length_ve"] = _Skin_Setup.Skin_m_x_length_ve_set
    __swig_getmethods__["m_x_length_ve"] = _Skin_Setup.Skin_m_x_length_ve_get
    if _newclass:
        m_x_length_ve = _swig_property(_Skin_Setup.Skin_m_x_length_ve_get, _Skin_Setup.Skin_m_x_length_ve_set)
    __swig_setmethods__["m_dim_vh"] = _Skin_Setup.Skin_m_dim_vh_set
    __swig_getmethods__["m_dim_vh"] = _Skin_Setup.Skin_m_dim_vh_get
    if _newclass:
        m_dim_vh = _swig_property(_Skin_Setup.Skin_m_dim_vh_get, _Skin_Setup.Skin_m_dim_vh_set)
    __swig_setmethods__["m_dim_sc"] = _Skin_Setup.Skin_m_dim_sc_set
    __swig_getmethods__["m_dim_sc"] = _Skin_Setup.Skin_m_dim_sc_get
    if _newclass:
        m_dim_sc = _swig_property(_Skin_Setup.Skin_m_dim_sc_get, _Skin_Setup.Skin_m_dim_sc_set)
    __swig_setmethods__["m_dim_ve"] = _Skin_Setup.Skin_m_dim_ve_set
    __swig_getmethods__["m_dim_ve"] = _Skin_Setup.Skin_m_dim_ve_get
    if _newclass:
        m_dim_ve = _swig_property(_Skin_Setup.Skin_m_dim_ve_get, _Skin_Setup.Skin_m_dim_ve_set)
    __swig_setmethods__["m_dim_de"] = _Skin_Setup.Skin_m_dim_de_set
    __swig_getmethods__["m_dim_de"] = _Skin_Setup.Skin_m_dim_de_get
    if _newclass:
        m_dim_de = _swig_property(_Skin_Setup.Skin_m_dim_de_get, _Skin_Setup.Skin_m_dim_de_set)
    __swig_setmethods__["m_dim_bd"] = _Skin_Setup.Skin_m_dim_bd_set
    __swig_getmethods__["m_dim_bd"] = _Skin_Setup.Skin_m_dim_bd_get
    if _newclass:
        m_dim_bd = _swig_property(_Skin_Setup.Skin_m_dim_bd_get, _Skin_Setup.Skin_m_dim_bd_set)
    __swig_setmethods__["m_dim_sb_sur"] = _Skin_Setup.Skin_m_dim_sb_sur_set
    __swig_getmethods__["m_dim_sb_sur"] = _Skin_Setup.Skin_m_dim_sb_sur_get
    if _newclass:
        m_dim_sb_sur = _swig_property(_Skin_Setup.Skin_m_dim_sb_sur_get, _Skin_Setup.Skin_m_dim_sb_sur_set)
    __swig_setmethods__["m_dim_sb_har"] = _Skin_Setup.Skin_m_dim_sb_har_set
    __swig_getmethods__["m_dim_sb_har"] = _Skin_Setup.Skin_m_dim_sb_har_get
    if _newclass:
        m_dim_sb_har = _swig_property(_Skin_Setup.Skin_m_dim_sb_har_get, _Skin_Setup.Skin_m_dim_sb_har_set)
    __swig_setmethods__["m_dim_all"] = _Skin_Setup.Skin_m_dim_all_set
    __swig_getmethods__["m_dim_all"] = _Skin_Setup.Skin_m_dim_all_get
    if _newclass:
        m_dim_all = _swig_property(_Skin_Setup.Skin_m_dim_all_get, _Skin_Setup.Skin_m_dim_all_set)
    __swig_setmethods__["m_nChem"] = _Skin_Setup.Skin_m_nChem_set
    __swig_getmethods__["m_nChem"] = _Skin_Setup.Skin_m_nChem_get
    if _newclass:
        m_nChem = _swig_property(_Skin_Setup.Skin_m_nChem_get, _Skin_Setup.Skin_m_nChem_set)
    __swig_setmethods__["m_Vehicle_area"] = _Skin_Setup.Skin_m_Vehicle_area_set
    __swig_getmethods__["m_Vehicle_area"] = _Skin_Setup.Skin_m_Vehicle_area_get
    if _newclass:
        m_Vehicle_area = _swig_property(_Skin_Setup.Skin_m_Vehicle_area_get, _Skin_Setup.Skin_m_Vehicle_area_set)
    __swig_setmethods__["m_bInfSrc"] = _Skin_Setup.Skin_m_bInfSrc_set
    __swig_getmethods__["m_bInfSrc"] = _Skin_Setup.Skin_m_bInfSrc_get
    if _newclass:
        m_bInfSrc = _swig_property(_Skin_Setup.Skin_m_bInfSrc_get, _Skin_Setup.Skin_m_bInfSrc_set)
    __swig_setmethods__["m_b_has_blood"] = _Skin_Setup.Skin_m_b_has_blood_set
    __swig_getmethods__["m_b_has_blood"] = _Skin_Setup.Skin_m_b_has_blood_get
    if _newclass:
        m_b_has_blood = _swig_property(_Skin_Setup.Skin_m_b_has_blood_get, _Skin_Setup.Skin_m_b_has_blood_set)
    __swig_setmethods__["m_coord_sys"] = _Skin_Setup.Skin_m_coord_sys_set
    __swig_getmethods__["m_coord_sys"] = _Skin_Setup.Skin_m_coord_sys_get
    if _newclass:
        m_coord_sys = _swig_property(_Skin_Setup.Skin_m_coord_sys_get, _Skin_Setup.Skin_m_coord_sys_set)
    __swig_setmethods__["m_React"] = _Skin_Setup.Skin_m_React_set
    __swig_getmethods__["m_React"] = _Skin_Setup.Skin_m_React_get
    if _newclass:
        m_React = _swig_property(_Skin_Setup.Skin_m_React_get, _Skin_Setup.Skin_m_React_set)
    __swig_setmethods__["m_n_amount"] = _Skin_Setup.Skin_m_n_amount_set
    __swig_getmethods__["m_n_amount"] = _Skin_Setup.Skin_m_n_amount_get
    if _newclass:
        m_n_amount = _swig_property(_Skin_Setup.Skin_m_n_amount_get, _Skin_Setup.Skin_m_n_amount_set)
    __swig_setmethods__["m_amount"] = _Skin_Setup.Skin_m_amount_set
    __swig_getmethods__["m_amount"] = _Skin_Setup.Skin_m_amount_get
    if _newclass:
        m_amount = _swig_property(_Skin_Setup.Skin_m_amount_get, _Skin_Setup.Skin_m_amount_set)
    __swig_setmethods__["m_Vehicle"] = _Skin_Setup.Skin_m_Vehicle_set
    __swig_getmethods__["m_Vehicle"] = _Skin_Setup.Skin_m_Vehicle_get
    if _newclass:
        m_Vehicle = _swig_property(_Skin_Setup.Skin_m_Vehicle_get, _Skin_Setup.Skin_m_Vehicle_set)
    __swig_setmethods__["m_Sebum"] = _Skin_Setup.Skin_m_Sebum_set
    __swig_getmethods__["m_Sebum"] = _Skin_Setup.Skin_m_Sebum_get
    if _newclass:
        m_Sebum = _swig_property(_Skin_Setup.Skin_m_Sebum_get, _Skin_Setup.Skin_m_Sebum_set)
    __swig_setmethods__["m_SurSebum"] = _Skin_Setup.Skin_m_SurSebum_set
    __swig_getmethods__["m_SurSebum"] = _Skin_Setup.Skin_m_SurSebum_get
    if _newclass:
        m_SurSebum = _swig_property(_Skin_Setup.Skin_m_SurSebum_get, _Skin_Setup.Skin_m_SurSebum_set)
    __swig_setmethods__["m_StraCorn"] = _Skin_Setup.Skin_m_StraCorn_set
    __swig_getmethods__["m_StraCorn"] = _Skin_Setup.Skin_m_StraCorn_get
    if _newclass:
        m_StraCorn = _swig_property(_Skin_Setup.Skin_m_StraCorn_get, _Skin_Setup.Skin_m_StraCorn_set)
    __swig_setmethods__["m_ViaEpd"] = _Skin_Setup.Skin_m_ViaEpd_set
    __swig_getmethods__["m_ViaEpd"] = _Skin_Setup.Skin_m_ViaEpd_get
    if _newclass:
        m_ViaEpd = _swig_property(_Skin_Setup.Skin_m_ViaEpd_get, _Skin_Setup.Skin_m_ViaEpd_set)
    __swig_setmethods__["m_Dermis"] = _Skin_Setup.Skin_m_Dermis_set
    __swig_getmethods__["m_Dermis"] = _Skin_Setup.Skin_m_Dermis_get
    if _newclass:
        m_Dermis = _swig_property(_Skin_Setup.Skin_m_Dermis_get, _Skin_Setup.Skin_m_Dermis_set)
    __swig_setmethods__["m_Blood"] = _Skin_Setup.Skin_m_Blood_set
    __swig_getmethods__["m_Blood"] = _Skin_Setup.Skin_m_Blood_get
    if _newclass:
        m_Blood = _swig_property(_Skin_Setup.Skin_m_Blood_get, _Skin_Setup.Skin_m_Blood_set)
    __swig_setmethods__["m_nVehicle"] = _Skin_Setup.Skin_m_nVehicle_set
    __swig_getmethods__["m_nVehicle"] = _Skin_Setup.Skin_m_nVehicle_get
    if _newclass:
        m_nVehicle = _swig_property(_Skin_Setup.Skin_m_nVehicle_get, _Skin_Setup.Skin_m_nVehicle_set)
    __swig_setmethods__["m_nSurSebum"] = _Skin_Setup.Skin_m_nSurSebum_set
    __swig_getmethods__["m_nSurSebum"] = _Skin_Setup.Skin_m_nSurSebum_get
    if _newclass:
        m_nSurSebum = _swig_property(_Skin_Setup.Skin_m_nSurSebum_get, _Skin_Setup.Skin_m_nSurSebum_set)
    __swig_setmethods__["m_nSebum"] = _Skin_Setup.Skin_m_nSebum_set
    __swig_getmethods__["m_nSebum"] = _Skin_Setup.Skin_m_nSebum_get
    if _newclass:
        m_nSebum = _swig_property(_Skin_Setup.Skin_m_nSebum_get, _Skin_Setup.Skin_m_nSebum_set)
    __swig_setmethods__["m_nStraCorn"] = _Skin_Setup.Skin_m_nStraCorn_set
    __swig_getmethods__["m_nStraCorn"] = _Skin_Setup.Skin_m_nStraCorn_get
    if _newclass:
        m_nStraCorn = _swig_property(_Skin_Setup.Skin_m_nStraCorn_get, _Skin_Setup.Skin_m_nStraCorn_set)
    __swig_setmethods__["m_nViaEpd"] = _Skin_Setup.Skin_m_nViaEpd_set
    __swig_getmethods__["m_nViaEpd"] = _Skin_Setup.Skin_m_nViaEpd_get
    if _newclass:
        m_nViaEpd = _swig_property(_Skin_Setup.Skin_m_nViaEpd_get, _Skin_Setup.Skin_m_nViaEpd_set)
    __swig_setmethods__["m_nDermis"] = _Skin_Setup.Skin_m_nDermis_set
    __swig_getmethods__["m_nDermis"] = _Skin_Setup.Skin_m_nDermis_get
    if _newclass:
        m_nDermis = _swig_property(_Skin_Setup.Skin_m_nDermis_get, _Skin_Setup.Skin_m_nDermis_set)
    __swig_setmethods__["m_nBlood"] = _Skin_Setup.Skin_m_nBlood_set
    __swig_getmethods__["m_nBlood"] = _Skin_Setup.Skin_m_nBlood_get
    if _newclass:
        m_nBlood = _swig_property(_Skin_Setup.Skin_m_nBlood_get, _Skin_Setup.Skin_m_nBlood_set)
    __swig_setmethods__["m_nxComp"] = _Skin_Setup.Skin_m_nxComp_set
    __swig_getmethods__["m_nxComp"] = _Skin_Setup.Skin_m_nxComp_get
    if _newclass:
        m_nxComp = _swig_property(_Skin_Setup.Skin_m_nxComp_get, _Skin_Setup.Skin_m_nxComp_set)
    __swig_setmethods__["m_nyComp"] = _Skin_Setup.Skin_m_nyComp_set
    __swig_getmethods__["m_nyComp"] = _Skin_Setup.Skin_m_nyComp_get
    if _newclass:
        m_nyComp = _swig_property(_Skin_Setup.Skin_m_nyComp_get, _Skin_Setup.Skin_m_nyComp_set)
    __swig_setmethods__["m_CompIdx"] = _Skin_Setup.Skin_m_CompIdx_set
    __swig_getmethods__["m_CompIdx"] = _Skin_Setup.Skin_m_CompIdx_get
    if _newclass:
        m_CompIdx = _swig_property(_Skin_Setup.Skin_m_CompIdx_get, _Skin_Setup.Skin_m_CompIdx_set)

    def __init__(self):
        this = _Skin_Setup.new_Skin()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _Skin_Setup.delete_Skin
    __del__ = lambda self: None

    def Init(self):
        return _Skin_Setup.Skin_Init(self)

    def InitReaction(self, arg2, arg3, arg4, arg5):
        return _Skin_Setup.Skin_InitReaction(self, arg2, arg3, arg4, arg5)

    def Release(self):
        return _Skin_Setup.Skin_Release(self)

    def createCompMatrix(self, arg2, arg3):
        return _Skin_Setup.Skin_createCompMatrix(self, arg2, arg3)

    def releaseCompMatrix(self):
        return _Skin_Setup.Skin_releaseCompMatrix(self)

    def createVH(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, x_end_coord, y_end_coord):
        return _Skin_Setup.Skin_createVH(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, x_end_coord, y_end_coord)

    def createSurSB(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord, arg12, arg13, arg14, arg15, arg16, arg17):
        return _Skin_Setup.Skin_createSurSB(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord, arg12, arg13, arg14, arg15, arg16, arg17)

    def createSB(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord, arg12):
        return _Skin_Setup.Skin_createSB(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord, arg12)

    def createSC(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, x_end_coord, y_end_coord):
        return _Skin_Setup.Skin_createSC(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, x_end_coord, y_end_coord)

    def createVE(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord):
        return _Skin_Setup.Skin_createVE(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, x_end_coord, y_end_coord)

    def createDE(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, x_end_coord, y_end_coord):
        return _Skin_Setup.Skin_createDE(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, x_end_coord, y_end_coord)

    def createBD(self, arg2, arg3):
        return _Skin_Setup.Skin_createBD(self, arg2, arg3)

    def getSizeBdyRight(self, arg2, arg3, arg4):
        return _Skin_Setup.Skin_getSizeBdyRight(self, arg2, arg3, arg4)

    def getConcBdyRight(self, arg2, arg3, arg4, arg5, arg6, arg7):
        return _Skin_Setup.Skin_getConcBdyRight(self, arg2, arg3, arg4, arg5, arg6, arg7)

    def getSizeBdyDown(self, arg2, arg3, arg4):
        return _Skin_Setup.Skin_getSizeBdyDown(self, arg2, arg3, arg4)

    def getConcBdyDown(self, arg2, arg3, arg4, arg5, arg6, arg7):
        return _Skin_Setup.Skin_getConcBdyDown(self, arg2, arg3, arg4, arg5, arg6, arg7)

    def diffuseMoL(self, t_start, t_end):
        return _Skin_Setup.Skin_diffuseMoL(self, t_start, t_end)

    def resetVehicle(self, arg2, arg3, arg4):
        return _Skin_Setup.Skin_resetVehicle(self, arg2, arg3, arg4)

    def removeVehicle(self):
        return _Skin_Setup.Skin_removeVehicle(self)

    def compCompartAmount(self):
        return _Skin_Setup.Skin_compCompartAmount(self)

    def compFlux_2sc(self, flux):
        return _Skin_Setup.Skin_compFlux_2sc(self, flux)

    def compFlux_sc2down(self, flux):
        return _Skin_Setup.Skin_compFlux_sc2down(self, flux)

    def compODE_dydt(self, arg2, arg3, arg4):
        return _Skin_Setup.Skin_compODE_dydt(self, arg2, arg3, arg4)

    def compReaction(self):
        return _Skin_Setup.Skin_compReaction(self)
    __swig_getmethods__["static_cvODE"] = lambda x: _Skin_Setup.Skin_static_cvODE
    if _newclass:
        static_cvODE = staticmethod(_Skin_Setup.Skin_static_cvODE)

    def getSCYlen(self):
        return _Skin_Setup.Skin_getSCYlen(self)

    def getNLayerXSc(self):
        return _Skin_Setup.Skin_getNLayerXSc(self)

    def getNGridsXSc(self):
        return _Skin_Setup.Skin_getNGridsXSc(self)

    def getNGridsYSc(self):
        return _Skin_Setup.Skin_getNGridsYSc(self)

    def get1DConcSC(self, ret, dim_ret, idx_chem=0):
        return _Skin_Setup.Skin_get1DConcSC(self, ret, dim_ret, idx_chem)

    def get1DCoordSC(self, ret, dim_ret, idx_chem=0):
        return _Skin_Setup.Skin_get1DCoordSC(self, ret, dim_ret, idx_chem)

    def getGridsConc(self, ret, dim_ret, idx_chem=0):
        return _Skin_Setup.Skin_getGridsConc(self, ret, dim_ret, idx_chem)

    def getLayersAmount(self, ret, dim_ret, idx_chem=0):
        return _Skin_Setup.Skin_getLayersAmount(self, ret, dim_ret, idx_chem)

    def displayGrids(self):
        return _Skin_Setup.Skin_displayGrids(self)

    def saveGrids(self, arg2, arg3):
        return _Skin_Setup.Skin_saveGrids(self, arg2, arg3)

    def saveAmount(self, arg2, arg3):
        return _Skin_Setup.Skin_saveAmount(self, arg2, arg3)

    def getXCoord(self, coord_x, dim):
        return _Skin_Setup.Skin_getXCoord(self, coord_x, dim)

    def getYCoord(self, coord_y, dim):
        return _Skin_Setup.Skin_getYCoord(self, coord_y, dim)

    def saveCoord(self, arg2, arg3):
        return _Skin_Setup.Skin_saveCoord(self, arg2, arg3)
Skin_swigregister = _Skin_Setup.Skin_swigregister
Skin_swigregister(Skin)

def Skin_static_cvODE(arg2, arg3, arg4, arg5):
    return _Skin_Setup.Skin_static_cvODE(arg2, arg3, arg4, arg5)
Skin_static_cvODE = _Skin_Setup.Skin_static_cvODE

class Skin_Setup(Skin):
    __swig_setmethods__ = {}
    for _s in [Skin]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Skin_Setup, name, value)
    __swig_getmethods__ = {}
    for _s in [Skin]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Skin_Setup, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_sComps"] = _Skin_Setup.Skin_Setup_m_sComps_set
    __swig_getmethods__["m_sComps"] = _Skin_Setup.Skin_Setup_m_sComps_get
    if _newclass:
        m_sComps = _swig_property(_Skin_Setup.Skin_Setup_m_sComps_get, _Skin_Setup.Skin_Setup_m_sComps_set)

    def InitConfig(self, arg2, arg3):
        return _Skin_Setup.Skin_Setup_InitConfig(self, arg2, arg3)

    def Release(self):
        return _Skin_Setup.Skin_Setup_Release(self)

    def InitVecCompart(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18):
        return _Skin_Setup.Skin_Setup_InitVecCompart(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18)

    def InitMtxCompart(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18):
        return _Skin_Setup.Skin_Setup_InitMtxCompart(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18)

    def saveFlux(self, arg2, arg3, arg4):
        return _Skin_Setup.Skin_Setup_saveFlux(self, arg2, arg3, arg4)

    def __init__(self):
        this = _Skin_Setup.new_Skin_Setup()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _Skin_Setup.delete_Skin_Setup
    __del__ = lambda self: None
Skin_Setup_swigregister = _Skin_Setup.Skin_Setup_swigregister
Skin_Setup_swigregister(Skin_Setup)

# This file is compatible with both classic and new-style classes.


