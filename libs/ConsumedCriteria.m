(* ::Package:: *)

(* :Title: ConsumedCriteria *)

(* :Author: Yen-Hsun Lin *)

(* :Description: Determined NS is consumed by the DM forming BH or not.      *)
(*               All equations in the comments are from J. Brammante et al., *)
(*               PRD 89, 015010 (2014).                                      *)


BeginPackage["ConsumedCriteria`", {"Constants`"}]

ShowMessage::usage = "Option, Track the star will be consumed or halted at which phase. \
Defalut is False";
StarConsumed::usage = "Return a boolean value for the star will be consumed or not. \
True for yes, False for not.";

Begin["`Private`"]

(* --- Subroutine: DPS --- *)
(*Can it collapse from degenerate and partly screened phase?*)
(*Mx and Mphi are in GeV*)
CheckDPS[Mx_, Nx_, Mphi_, Alpha_, ShowMsg_] :=
 Module[{mx = Mx, nx = Nx, mphi = Mphi, a = Alpha, msg = ShowMsg, Ncolldps},
  Ncolldps = (1.1*10^61) (a^-6) (mphi^12) (mx)^-9;
  If[
   (*Can Nx collapse?*)
   nx > Ncolldps,
   If[
    (*Deg or nondeg collapse*)
    Ncolldps > 8*10^35,
    If[
     (*BH evaporation or not?*)
     Ncolldps > (3.4/mx)*10^36,
     (*Star consumed*)
     Which[
      msg == False, Return[True],
      msg == True, Return[{True, "Scenario (d)"}]
      ],
     (*BH evaporated*)
     Which[
      msg == False, Return[False],
      msg == True, Return[{False, "Scenario (e)"}]
      ]],
    (*Still in nondegenerate phase, call CheckNSS*)   
    CheckNSS[mx, nx, mphi, a, msg]
    ],
   Which[
    msg == False, Return[False],
    msg == True, 
    Return[{False, "Scenario (b)"}]]
   ]
  ];


(* --- Subroutine: DSS --- *)
(* Eq.(22) and y is holded for later use, Mx and Mphi are in GeV *)
VirialDSS[Mx_, Nx_, Mphi_, Alpha_, y_] :=
  -(3 Pi^2)^(2./3) Mphi^2/(Mx*y^2) + (4 Pi/3)^(1/3) G*
  Nx^(2/3) Mx*y^2 RhoNS/Mphi^2 + 8 Alpha*Mphi*Exp[-y] (1/y + 1)

(*Look-up table for the exponent of Ncoll, 10-base*)
dn = 0.05;
LookupNcoll = Table[n, {n, 30, 45, dn}];
MaxIt = Length[LookupNcoll];

CheckDSS[Mx_, Nx_, Mphi_, Alpha_, ShowMsg_, Lookup_: LookupNcoll, Maxit_: MaxIt] :=
  Module[{mx = Mx, nx = Nx, mphi = Mphi, a = Alpha, msg = ShowMsg, 
   lookupNcoll = Lookup, maxit = Maxit, j = 0, Ncolldss = 0, ncollexp,
   yDiscriminate, y},
  Do[
   ncollexp = lookupNcoll[[i]];
   (*Checking which Ncoll makes no solution for y, Ncoll calculated from look-up table*)
   yDiscriminate = 
    Length[FindInstance[
      VirialDSS[mx, 10^ncollexp, mphi, a, y] == 0 && y > 1, y, Reals]];
   If[(*Ncoll is found, break the loop*)
    yDiscriminate == 0,
    Ncolldss = 10^ncollexp;
    j = i;
    Break[],
    Continue[]
    ], {i, 1, maxit}];
  
  (*Following checks the collapse can happen or not?*)
  If[
   (*If j=0 or Nx < Ncolldss, no collapse*)
   j == 0 || nx < Ncolldss,
   Which[
    msg == False, Return[False],
    msg == True, 
    Return[{False, "Scenario (c)"}]],
   (*If Ncoll is found, still no guarantee collapse*)
   If[Ncolldss > 8*10^35,
    If[
     (*BH evaporation or not?*)
     Ncolldss > (3.4/mx)*10^36,
     (*Star consumed*)
     Which[
      msg == False, Return[True],
      msg == True, Return[{True, "Scenario (f)"}]
      ],
     (*BH evaporated*)
     Which[
      msg == False, Return[False],
      msg == True, Return[{False, "Scenario (g)"}]
      ]],
    (*Still in nondegenerate phase, call CheckNSS*)
    CheckNSS[mx, nx, mphi, a, msg]
    ]
   ]
  ];


(* --- Subroutine: NSS --- *)
Rth[Mx_] := 250 cm2GeV/Sqrt[Mx];
ynss[Mx_, Nx_, Mphi_] := 1.6*Mphi*Rth[Mx]/Nx^(1/3);
VirialNSS[Mx_, Nx_, Mphi_, 
  Alpha_] := (4 Pi/3)^(1/3) G*Nx^(2/3)*RhoNS*Mx*
   ynss[Mx, Nx, Mphi]^2/Mphi^2 + (4 Pi/3)^(1/3) G*Nx^(2/3) Mx^2*
   Mphi/ynss[Mx, Nx, Mphi] + 
  8 Alpha*Mphi*Exp[-ynss[Mx, Nx, Mphi]] (1/ynss[Mx, Nx, Mphi] + 1)

CheckNSS[Mx_, Nx_, Mphi_, Alpha_, ShowMsg_] :=
 Module[{mx = Mx, nx = Nx, mphi = Mphi, a = Alpha, msg = ShowMsg, 
   ncollseed = 30, ncollsol, Ncollnss, ncollexp},
  (*ncollseed=Log10[nx];*)
  ncollsol = 
   FindRoot[Log10[VirialNSS[mx, 10^ncollexp, mphi, a]] == Log10[3*NSTemp*K2GeV], {ncollexp, ncollseed}];
  Ncollnss = 10^ncollexp /. ncollsol;
  (*Following checks the collapse can happen or not?*)
  If[
   nx > Ncollnss && Ncollnss < 8*10^35,
   If[(*Checking screened phase*)
    2*10^4 mphi/Sqrt[mx] < 1,
    (*Partly screened*)
    If[a > 1.6*10^4 mphi^2/Sqrt[mx^3],
     If[Ncollnss > (3.4/mx)*10^36,
      Which[
       msg == False, Return[True],
       msg == True, 
       Return[{True, 
         "Scenario (m)"}]
       ],
      Which[
       msg == False, Return[False],
       msg == True, 
       Return[{False, 
         "Scenario (n)"}]
       ]],
     Which[
      msg == False, Return[False],
      msg == True, 
      Return[{False, 
        "Scenario (j)"}]
      ]],
    (*Strongly screened*)
    If[a > 2.7*10^-9 Exp[
         2.1*10^4 mphi/
           Sqrt[mx]]/(mphi/(1 + 4.7*10^-5 (1/mphi) Sqrt[mx])),
     If[Ncollnss > (3.4/mx)*10^36,
      Which[
       msg == False, Return[True],
       msg == True, 
       Return[{True, 
         "Scenario (k)"}]
       ],
      Which[
       msg == False, Return[False],
       msg == True, 
       Return[{False, 
         "Scenario (l)"}]
       ]],
     Which[
      msg == False, Return[False],
      msg == True, 
      Return[{False, 
        "Scenario (i)"}]
      ]]
    ],
   Which[
    msg == False, Return[False],
    msg == True, 
    Return[{False, 
      "Scenario (h)"}]
    ]
   ]
  ];


(* --- Main routine: StarConsumed ---*)
(* Default option value *)
Options[StarConsumed] = {ShowMessage -> False};

(*Mx is in GeV and Mphi in MeV*)
StarConsumed[Mx_ /; NumericQ[Mx], Nx_ /; NumericQ[Nx], Mphi_ /; NumericQ[Mphi],
 Alpha_ /; NumericQ[Alpha], OptionsPattern[]] :=
 Module[{mx = Mx, nx = Nx, mphi = Mphi/1000, a = Alpha, msg = OptionValue[ShowMessage]},
  If[
   (*Can collapse relativistically?*)
   a > 4.7*(mphi/mx)^2,
   If[
    (* Strongly screened phase? *)
    a > mphi/mx,
    (* True, call CheckDSS *)
    CheckDSS[mx, nx, mphi, a, msg],
    (* False, partly screened, call CheckDPS*)
    CheckDPS[mx, nx, mphi, a, msg]
    ],
   (*Unable to collapse relativistically*)
   Which[
    msg == False, Return[False],
    msg == True, Return[{False, "Scenario (a)"}]
    ]
   ]
  ];


Protect[ShowMessage, StarConsumed];

End[]

EndPackage[]
