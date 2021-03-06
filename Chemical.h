/* The header file for chemical being applied to skin
   It should include all the properties (descriptors) of the chemical */
#ifndef _H_CHEMICAL_
#define _H_CHEMICAL_

#include "Config.h"

class Chemical
{
 public:
  double m_mw, // molecular weight
    m_K_ow,	//partition coefficient between octanol and water
    m_pKa, // ionisation
    m_frac_non_ion, // fraction of solute non-ionised at pH 7.4
    m_frac_unbound, // fraction of solute unbound in a 2.7% albumin solution at pH 7.4
    m_r_s; // solute radius

  char m_acid_base; // whether it's acid ('A') or base ('B')


 public:
  Chemical(void) {};
  ~Chemical(void) {};

  void operator=(const Chemical &other);

  void Init(double, double, double, double, double, char);
  // void Init(const Chemical &other);
  void InitConfig(const Config &conf);
  void calcIon();
  void calcBinding();
};

#endif
