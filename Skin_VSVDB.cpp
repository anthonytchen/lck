#include "stdafx.h"
#include "Skin_VSVDB.h"

void Skin_VSVDB::Init(Chemical *chemSolute, int nChem, 
		      double *conc_vehicle, double *partition_vehicle, double *diffu_vehicle, 
		      double dx_vehicle, double area_vehicle, 
		      int n_layer_x_sc, int n_layer_y_sc, double offset_y_sc,
		      double x_len_ve, int n_grids_x_ve, double x_len_de, int n_grids_x_de,
		      double *par_dermis2blood, double *blood_k_clear,
		      bool bInfSrc)
{

  int i;
  double coord_x_start, coord_y_start, coord_x_end, coord_y_end;
  double x_len_sc, y_len_sc, y_len_ve, y_len_de;

  m_dz_dtheta = 0.01; // fixing dz, the dimension perpendicular to x-y domain

  m_b_has_SC = m_b_has_VE = m_b_has_DE = m_b_has_blood = true;

  // boundary condition: up, left, right, down
  BdyCondStr bdys_vh = {ZeroFlux,  Periodic, Periodic, FromOther};
  BdyCondStr bdys_sc = {FromOther, Periodic, Periodic, FromOther};
  BdyCondStr bdys_ve = bdys_sc;
  BdyCondStr bdys_de = {FromOther, Periodic, Periodic, ZeroFlux};

  m_nChem = nChem;

  /*  set up the compartments */

  // SC
  // coord_x_start = dx_vehicle; coord_y_start = 0;
  coord_x_start = 0; coord_y_start = 0;
  createSC(chemSolute, coord_x_start, coord_y_start, n_layer_x_sc, n_layer_y_sc, offset_y_sc, 
	   bdys_sc, &coord_x_end, &coord_y_end);
  x_len_sc = coord_x_end - coord_x_start;
  y_len_sc = coord_y_end - coord_y_start;

  // VE
  coord_x_start = coord_x_end; coord_y_start = 0;
  createVE(chemSolute, coord_x_start, coord_y_start, x_len_ve, y_len_sc, n_grids_x_ve, 1,
	   bdys_ve, &coord_x_end, &coord_y_end);

  // DE
  coord_x_start = coord_x_end; coord_y_start = 0;
  createDE(chemSolute, coord_x_start, coord_y_start, x_len_de, y_len_sc, n_grids_x_de, 1, true,
	   bdys_de, &coord_x_end, &coord_y_end);

  // BD
  createBD(par_dermis2blood, blood_k_clear);

  // VH
  // coord_x_start = 0; coord_y_start = 0;
  coord_x_start = -dx_vehicle; coord_y_start = 0;
  createVH(chemSolute, conc_vehicle, partition_vehicle, diffu_vehicle,
	   coord_x_start, coord_y_start, dx_vehicle, y_len_sc, area_vehicle,
	   bInfSrc, bdys_vh, &coord_x_end, &coord_y_end);


  /* link the compartments through boundary setting
     bdy conditions: up/left/right/down */

  for (i=0; i<m_nChem; i++) {

    m_Vehicle[i].createBoundary(0, m_StraCorn[i].m_ny);    
    m_Vehicle[i].setBoundaryGrids(NULL, m_StraCorn[i].m_grids);

    m_StraCorn[i].createBoundary(0, m_ViaEpd[i].m_ny);
    m_StraCorn[i].setBoundaryGrids(NULL, m_ViaEpd[i].m_grids);

    m_ViaEpd[i].createBoundary(0, m_Dermis[i].m_ny);
    m_ViaEpd[i].setBoundaryGrids(NULL, m_Dermis[i].m_grids);

    m_Dermis[i].createBoundary(0, 0);    
    m_Dermis[i].setBoundaryGrids(NULL, NULL);

  }

  // overall dimension
  m_dim_all =  m_dim_vh + m_dim_sc + m_dim_ve + m_dim_de + m_dim_bd;

  // If InitReaction() is not called, set m_React.idx_substrate to -1 to indicate no reaction
  m_React.idx_substrate = -1;
}

void Skin_VSVDB::Release(void)
{
  Skin::Release();
}
