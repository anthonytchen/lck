/* The header file for the vehicle  */
#ifndef _H_VEHICLE_
#define _H_VEHICLE_

#include "Comp.h"

class Vehicle : public Comp
{
 public:
  double m_T, m_eta, // temperature, water viscosity at the temperature
    m_K_vw,  // partition between vehicle and water
    m_D, // diffusion coefficient in vehicle
    m_init_concChem; // initial vehicle concentration

public:
  Vehicle(void) {};	
  ~Vehicle(void) {};
  void Init(double, double, double, int, int, double, double, double, CoordSys, BdyCond, BdyCond, BdyCond, BdyCond);
  void Release();

  void createGrids(Chemical, double, double);
 
  // I/O functions
  void saveCoord(const char [], const char []);
};

#endif
