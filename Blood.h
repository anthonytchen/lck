#ifndef _H_BLOOD_
#define _H_BLOOD_

#include "Chemical.h"
#include "Dermis.h"

class Blood
{
public:
  double m_flow_capil, // volumetric capillary blood flow rate
    m_vol_blood_body, // blood volume of the entire body
    m_concChem, // solute concentration in blood
    m_k_clear, // the clearance constant
    m_f_unbound; // fraction of unbounded solute in blood

  // solute mass transport into and out from dermis
  double m_mass_into_dermis, m_mass_outfrom_dermis;

  Grid m_gridVehicle, m_gridSink;

public:
  Blood(void) {};	
  ~Blood(void) {};
  void Init(double frac_unbound, double body_mass=70, char gender='M');
  void Release();
  
  void updateMassInOutDermis(double, double, double);
	
  // Functions needed for ODE solver
  void compODE_dydt (double, const double[], double []);	
	
  // I/O functions
  double getConcChem() { return m_concChem; };
  void displayGrids();
  void saveConc(bool, const char []);
};

#endif
