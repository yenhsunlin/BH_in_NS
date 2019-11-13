(* ::Package:: *)

(* :Title: Constants *)

(* :Author: Yen-Hsun Lin *)

(* :Description: Defined useful constants *)


BeginPackage["Constants`"]

(* Function usage *)
erg2GeV::usage = "Convert erg to natural unit, GeV.";
K2GeV::usage = "Convert Kelvin to natural unit, GeV.";
g2GeV::usage = "Convert gram to natural unit, GeV.";
cm2GeV::usage = "Convert centimeter to natural unit, \!\(\*SuperscriptBox[\(GeV\), \(-1\)]\).";
Vol2GeV::usage = "Convert volume, \!\(\*SuperscriptBox[\(cm\), \(3\)]\), to natural unit, \!\(\*SuperscriptBox[\(GeV\), \(-3\)]\).";
sec2GeV::usage = "Convert second to natural unit, \!\(\*SuperscriptBox[\(GeV\), \(-1\)]\).";
c::usage = "Speed of light, \!\(\*
StyleBox[\"m\",\nFontSlant->\"Italic\"]\)/\!\(\*
StyleBox[\"s\",\nFontSlant->\"Italic\"]\).";
MPl::usage = "Planck mass in natural unit, GeV.";
G::usage = "Gravitational constant in natural unit, \!\(\*SuperscriptBox[\(GeV\), \(-2\)]\).";
NSTemp::usage="NS core temperature, Kelvin.";
RhoNS::usage="NS core density in natural unit, \!\(\*SuperscriptBox[\(GeV\), \(4\)]\)";
LocalDM::usage="Local DM density, GeV/\!\(\*SuperscriptBox[\(cm\), \(3\)]\)";
LocalVecDisp::usage="Local DM velocity dispersion, km/s"

Begin["`Private`"]

erg2GeV = (1.602*10^-3)^-1(*GeV*);
K2GeV = (1.161*10^13)^-1(*GeV*);
g2GeV = (1.783*10^-24)^-1(*GeV*);
cm2GeV = (1.973*10^-14)^-1(*GeV^-1*);
Vol2GeV = cm2GeV^-3(*cm^-3 to GeV^3*);
sec2GeV = (6.529*10^-25)^-1(*GeV^-1*);
c = 2.998*10^8(*m/s*);
MPl = 1.221*10^19(*GeV*);
G = MPl^-2(*GeV^-2*);
NSTemp = 10^5;
RhoNS = 0.00432376;
LocalDM = 0.3;
LocalVecDisp = 220;

(* Protect the parameter name space *)
Protect[
    erg2GeV, K2GeV, g2GeV, cm2GeV, 
    Vol2GeV, sec2GeV, c, MPl, G
    ];

End[]

EndPackage[]