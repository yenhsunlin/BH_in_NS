(* ::Package:: *)

(* :Title: Capture *)

(* :Author: Yen-Hsun Lin *)

(* :Description: Neutron star capture rate                          *)
(*               The capture rate valid when DM mass is larger than *)
(*               1e-6 GeV. All captured DM will evaporate lighter   *)
(*               than this mass.                                    *)
(*               See R. Garani et al., JCAP 05, 035 (2019).         *)


BeginPackage["Capture`", {"Constants`"}]

CaptureRate::usage = "Capture rate of NS, #/sec";
CaptureRateNoCorrection::usage = "Capture rate of NS without full consideration \
of Fermi-Dirac statistics in the low mass region, #/sec";
NxDecay::usage = "Number of DM captured by NS with DM decay."
NxNoDecay::usage = "Number of DM captured by NS without DM decay."

Begin["`Private`"]

cap = Interpolation[Import["nscap.dat","Data"], InterpolationOrder->1];

(* Capture rate without full Pauli blocking correction and reali- *)
(* stic NS density profile BSK-20. Inputs are the same as above.  *)
CaptureRateNoCorrection[mx_, sig_, rho_:LocalDM, vbar_:LocalVecDisp] := 
  0.8*(5.072*10^72)*(rho/(mx*vbar))*Min[10^-45,sig]*Min[1,1.47548*mx/(1+mx)];


(* mx: GeV, sig: cm^-2, rho: GeV/cm^3, vbar: km/s *)
CaptureRate[mx_,sig_,rho_:LocalDM,vbar_:LocalVecDisp] := 
  If[
    mx>10^-6,
    Which[
      mx<=1,(10^cap[Log10[mx]])*rho*(Min[sig,10^-45]/10^-45)*(220/vbar),
      mx>1,CaptureRateNoCorrection[mx,sig,rho,vbar]
      ],
      Print["Input DM mass outside capable range."]
      ];


(* DM number *)
(* w/ decay *)
NxDecay[t_, tau_, mx_, sig_, rho_: LocalDM, vbar_: LocalVecDisp] := 
  CaptureRate[mx, sig, rho, vbar]*tau*(1 - Exp[-t/tau]);
(* w/o decay*)
NxNoDecay[t_, mx_, sig_, rho_: LocalDM, vbar_: LocalVecDisp] := 
  CaptureRate[mx, sig, rho, vbar]*t;


Protect[CaptureRate,CaptureRateNoCorrection,NxDecay,NxNoDecay];

End[]

EndPackage[]