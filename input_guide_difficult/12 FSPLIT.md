# FSPLIT: Stream Splitter  

# Input Language for FSPLIT  

BLOCK blockid     FSPLIT PARAM keyword $\mathbf { \bar { \Psi } } = \mathbf { \Psi }$ value  

Optional keywords:  

PRES NPHASE PHASE MAXIT TOL  

FRAC sid frac /   
basis-FLOW sid flow [keyno]  /  .   
VOL-FLOW sid flow   
basis-LIMIT sid flow /   
VOL-LIMIT sid flow   
basis-C-LIM sid flow  /   
VOL-C-LIM sid flow  /   
R-FRAC sid frac  /   
STREAM-ORDER sid order /  .   
DEF-KEY KEYNO $\mathbf { \lambda } =$ keyno SUBSTREAM $\mathbf { \tau } =$ ssid COMPS $\mathbf { \tau } =$ cid-list  /  & SUBSTREAM $\mathbf { \lambda } =$ ssid COMPS $\mathbf { \tau } =$ cid-list  /  

# Input Language Description for FSPLIT  

PARAM  

Use to specify outlet conditions. If you do not specify the pressure, it defaults to the minimum pressure of the inlet streams.  

PRES PRES > 0 Pressure PRES ≤ 0 Pressure drop (Default $_ { = 0 }$ )  

NPHASE Number of phases in MIXED substream:  

$\begin{array} { r } { \mathsf { N P H A S E } = \textbf { 1 } } \\ { \mathsf { N P H A S E } = 2 } \\ { \mathsf { N P H A S E } = 3 } \end{array}$ One-phase calculation Two-phase flash (Default) Three-phase flash  

PHASE. Specifies the phase when NPHASE ${ \bf \varepsilon } = { \bf 1 }$ :  

PHASE = V Vapor (Default) PHASE = L Liquid PHASE $\mathbf { \sigma } = \mathbf { 5 }$ Solid. Use for electrolytes system only.  

MAXIT Maximum number of flash iterations. (Default $\ c =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

TOL Flash convergence tolerance. (Default $\ c =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

FRAC  

Use to specify the fraction of the inlet stream going to an outlet stream.  

sid. Outlet stream ID frac .. Split fraction  

basis-FLOW  

Use to specify the flow rate on a MOLE, MASS, or STDVOL basis of an outlet stream. If a key is given, use to specify the flow rate of a subset of components in an outlet stream. You cannot use STDVOL basis if any solid substreams are present. You can use only MASS basis if a substream type NC is present.  

sid Outlet stream ID flow . Flow rate  

keyno.... Key number  

VOL-FLOW  

Use to specify the actual volumetric flow rate of an outlet stream.  

sid. Outlet stream ID flow . Actual volumetric flow rate  

basis-LIMIT  

Use to specify the limit flow rate on a MOLE, MASS, or STDVOL basis of an outlet stream. You cannot use STDVOL basis if any solid substreams are present. You can use only MASS basis if a substream of type NC is present.  

sid. Outlet stream ID flow . Limit flow rate  

VOL-LIMIT  

Use to specify the actual volumetric limit flow rate of an outlet stream.  

sid. Outlet stream ID flow . Actual volumetric limit flow rate  

basis-C-LIM  

Use to specify the cumulative limit flow rate on a MOLE, MASS, or STDVOL basis of an outlet stream. You cannot use STDVOL basis if any solid substreams are present. You can use only MASS basis if a substream type NC is present.  

sid. Outlet stream ID flow . Cumulative limit flow rate  

VOL-C-LIM  

Use to specify the actual volumetric cumulative limit flow rate of an outlet stream.  

sid. Outlet stream ID flow . Actual volumetric cumulative limit flow rate  

R-FRAC  

Similar to FRAC, except use to specify the fraction of the residue going into an outlet stream. In this case, the residue is the flow of the inlet remaining after all other specifications (FRAC, basis-FLOW, VOL-FLOW, basis-LIMIT, VOL-LIMIT, basis-C-LIM, and VOL-C-LIM) are satisfied.  

sid. Outlet stream ID frac Split fraction  

STREAM-ORDER  

Use to specify order of flow split calculation for outlet streams.  

sid. Outlet stream ID  

order. Order of flow split calculation for outlet streams. Use numbers 1 to the number of outlet streams to specify the order.  

DEF-KEY  

Use to define the keys by associating a component or a group of components with a key number. One DEF-KEY statement is required for each key defined.  

keyno. Key number ssid. Substream ID (Default $\ c =$ MIXED) cid-list List of component IDs  

# Accessing Variables in FSPLIT  

Many Aspen Plus features enable you to sample or change block variables. Chapter 29 describes how to access variables. The following table lists variable names and other information needed to sample and/or change variables for this block.  

Block Input   


<html><body><table><tr><td>Sentence</td><td>Variables ID1</td></tr><tr><td>PARAM</td><td>PRES，MAXIT，OL 二</td></tr><tr><td>FRAC FRAC</td><td>sid</td></tr><tr><td>basis-FLOW</td><td>FLOW sid</td></tr><tr><td>VOL-FLOW FLOW</td><td>sid</td></tr><tr><td>basis-LIMIT FLOW</td><td>sid</td></tr><tr><td>VOL-LIMIT</td><td>FLOW sid</td></tr><tr><td>basis-C-LIM FLOW</td><td>sid</td></tr><tr><td>VOL-C-LIM FLOW</td><td>sid</td></tr><tr><td>R-FRAC</td><td>FRAC sid</td></tr></table></body></html>  