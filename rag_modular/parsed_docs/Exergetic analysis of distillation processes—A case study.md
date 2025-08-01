# Exergetic analysis of distillation processes—A case study

Antonio B. Araújo<sup>a,1</sup>, Romildo P. Brito<sup>b,*</sup>, Luís S. Vasconcelos<sup>b</sup>

<sup>a</sup>Braskem Company, Avenue Assis Chateaubriand 5260, Pontal da Barra, Maceió, Alagoas 57010 800, Brazil  <sup>b</sup>Department of Chemical Engineering, Federal University of Campina Grande, Av Aprigio Veloso, 882, Campina Grande, PB 58109 970, Brazil

Received 9 February 2006

# Abstract

The concept of exergy has been introduced to establish a universal standard for quality and efficient use of energy. In this work, applications of this concept to compression, heat exchange, and separation processes, in addition to the computation of their irreversibility rate and thermodynamic efficiency, are considered. An industrial case study on the purification of 1,2- ethylenedichloride (EDC) in a high- purity distillation column is presented. Due to its large throughput, this distillation column consumes a large amount of thermal energy (steam to the reboiler) and in order to reduce the energy requirements without large process modifications, a new configuration using a vapour compression heat pump is proposed which yields considerable improvement in the use of energy. Both configurations were implemented using the commercial simulator Aspen Plus<sup>TM</sup>, the results of the original configuration were validated with data extracted from the plant. The objective of this work was to compare the original configuration and the new proposed one, from a thermodynamic approach. Furthermore, two forms of process thermodynamic analysis based on the concept of exergy were applied to the new proposed configuration.

$(\widehat{\mathbf{C}})$  2006 Elsevier Ltd. All rights reserved.

Keywords: Exergy; Thermodynamic; Efficiency; Distillation

# 1. Basic concepts of exergy

The calculation of performance indexes can be of great importance in order to evaluate the thermodynamic efficiency of a process; however, a consistent analysis is needed to avoid incomplete or inadequate results.

Traditional techniques to evaluate the effective use of energy within a process involve basically two kinds of approaches: use of energetic balances and calculation of performance indexes. Energetic balances, essentially based on the First Law of Thermodynamics, do not distinguish among the various types of energy involved in a specific process and do not reveal whether energy losses pose a problem. However, methods based on the Second Law of Thermodynamics (in addition to the First Law) are known to provide much more valuable information since they consider the underlying idea of quality of energy.

The quality of energy can be roughly related to the capacity of a given form of energy to cause changes in a process. For example, the capacity to effect some desired change when  $100\mathrm{J}$  of electric energy is available is greater than that of  $100\mathrm{J}$  of thermal energy available at  $1000\mathrm{K}$  when the temperature of the environment is, i.e.,  $300\mathrm{K}$ . This difference in quality may give rise to misleading results when analysing the performance of thermal processes [1].

It is discussed in Ref. [1] that the quality of a given form of energy depends on its type. This may be either ordered or disordered (random). Ordered forms of energy, which basically comprises potential energy and kinetic energy, have invariant quality and are fully convertible, through work interaction, to other forms of energy. Internal energy, thermal radiation, and chemical energy are different forms of disordered energy and have variable quality, which depends both on the form of energy and on the parameters of the energy carrier and of the environment. To account for the variable quality of disordered energy forms in the

analysis of thermal and chemical plants, a universal standard of quality is needed. It follows that the most natural and convenient standard is the maximum work which can be obtained from a given form of energy using the environment as the reference state. This standard of energy quality is called exergy.

The concept of exergy establishes a universal standard of quality of energy in a given environment. An exergetic balance gives information on how much exergy supplied to the process will be lost. That is to say, these exergetic losses (also known as irreversibility rate) are a measure of degradation of the quality of energy.

Mathematically, the exergy  $(E)$  of a stream of matter is written as

In this work, an exegetic analysis has been applied to a real process consisting of the purification of EDC in a highpurity distillation column. In order to efficiently use energy in this process without the need for large design modifications, a new configuration using a vapour compression heat pump is proposed.

# 2. Performance criteria

Cornelissen [3] defines three basic forms to calculate the thermodynamic efficiency of a process. The first is known as simple efficiency

$$
\eta = \frac{E_{OUT}}{E_{IN}}. \tag{6}
$$

In this case, there is a direct relation between the exergy flowing from the process,  $E_{OUT}$  to that flowing into the process,  $E_{IN}$

Another form, known as the rational efficiency [1], is defined as

$$
\psi = \frac{\sum\Delta E_{OUT}}{\sum\Delta E_{IN}}. \tag{7}
$$

The rational efficiency is a criterion of performance which can be formulated for a plant or a plant component and it is given by the ratio of the exergy transfer rate associated to the plant (or plant component) output exergy to the exergy transfer rate associated to the corresponding input exergy.

$$
E = E_{K} + E_{P} + E_{PH} + E_{CH}. \tag{1}
$$

The kinetic  $(E_K)$  and potential  $(E_P)$  exergy components, as ordered forms of exergy, are represented by ordinary kinetic and potential energy equations.

The physical exergy  $(E_{PH})$  component is defined as the maximum amount of work obtainable when a stream of matter is taken reversibly from its initial state, at  $P_{1}$  and  $T_{1}$  to the environment state at  $T_{0}$  and  $P_0$  (where thermal and mechanical equilibria exist) by physical processes. In other words,

The rational efficiency is a criterion of performance which can be formulated for a plant or a plant component and it is given by the ratio of the exergy transfer rate associated to the plant (or plant component) output exergy to the exergy transfer rate associated to the corresponding input exergy.

$$
W_{REV} = E_{PH} = (H_1 - T_0S_1) - (H_0 - T_0S_0), \tag{2}
$$

where  $H$  represents enthalpy and  $S$  entropy.

The overall chemical exergy  $(E_{CH})$  component is defined as the maximum amount of work obtainable when a stream of matter is taking reversibly from its environment state to the dead state (here defined as the state where all kinds of equilibria exist, including chemical equilibrium) at  $T_{0}$  and  $P_0$  by a reversible process involving solely mass, heat and expansion/compression work transfer with the dead state.  $E_{CH}$  is calculated according to a procedure proposed in Hinderink et al. [2] which basically splits  $E_{CH}$  into a specific chemical term and a mixture term. The specific chemical term is defined as

The third form involves transiting of exergy, meaning that, though crossing the system, this flow of exergy does not take part in the process. It is given by subtracting the transiting term from the incoming and outgoing exergy terms,

$$
\chi = \frac{E_{OUT} - E_{TR}}{E_{IN} - E_{TR}}. \tag{8}
$$

In Henley and Seader [4], an approach based on the fugacity of the components is proposed to evaluate the thermodynamic efficiency of distillation processes. Essentially, Ref. [4] define the efficiency of a separation process at standard conditions as the quotient of the minimum amount of work needed for this process and the total exergy input to achieve the process. The expression for the thermodynamic efficiency is given by

$$
\xi = \frac{RT_0\bigg[\sum_{OUT}n_k\bigg(\sum_i z_{i,k}\ln(f_{i,k})\bigg) - \sum_{in}n_j\bigg(\sum_i z_{i,j}\ln(f_{i,j})\bigg)\bigg]}{\sum_i\big(1 - \frac{T_0}{T_r}\big)Q_r + \sum - W_S},
$$

$$
E_0 = L_0\sum_{i = 1}^n x_{0,i}E_{0,i}^{0l} + V_0\sum_{i = 1}^n y_{0,i}E_{0,i}^{0v}, \tag{3}
$$

where  $L_{0}$  and  $V_{0}$  represent the liquid and vapour fraction;  $x_{0,i}$  and  $y_{0,i}$  are molar fractions in the liquid and vapour phases, respectively;  $E_{0,i}^{0x}$  is the standard exergy (  $x = l$  for liquid phase and  $x = v$  for vapour phase) and  $n$  refers to the number of components in the stream. The mixture term is given by

where  $k$  refers to one of the outgoing streams;  $j$  refers to one of the incoming streams;  $i$  refers to any component in the stream;  $r$  refers to any reservoirs  $r$  at temperatures  $T_{r};R$  is the universal gas constant,  $z$  represents the feed composition,  $Q$  refers to the heat duty, and  $W_{S}$  the shaft work.

$$
E_{MIX} = \Delta_{MIX}H - T_0\Delta_{MIX}S, \tag{4}
$$

where

$$
\Delta_{MIX}M = L\left(M^l -\sum_{i = 1}^{n}x_iM_i^l\right) + V\left(M^v -\sum_{i = 1}^{n}y_iM_i^v\right),
$$

where  $M$  is any thermodynamic property.

An advantage of the procedure proposed in Kotas [1] over the one proposed in Henley and Seader [4] is to allow the computation of irreversibility rates and efficiencies individually.

In fact, it is important to adopt a unique definition of thermodynamic performance evaluation when comparing a given process in its original configuration with its proposed improved configuration. The comparison of thermodynamic performance between the original configuration and the new proposed configurations is carried out using the rational efficiency  $\psi$  [1], since this form of analysis is easy to apply and gives a good insight into the process. Furthermore, procedures proposed by Kotas [1] and Henley and Seader [4] to perform thermodynamic analysis were applied to the new proposed configuration.

# 3. Industrial case

This work presents a case study involving the purification 1,2- ethylenedichloride (written EDC for short) in a distillation column currently operating in a vinyl chloride monomer (VCM) plant of the Braskem Company in Brazil.

EDC is an intermediate substance in the production of VCM which is subsequently used as raw material for the production of poly vinyl chloride (PVC). The column under consideration has four feed streams originated from different parts of the VCM plant where its distillate, high purity EDC, is sent to a cracking furnace in which a endothermic reaction takes places to produce VCM, while the bottom product is sent to the recuperation system. Fig. 1 depicts the actual (original) configuration.

The simulation of the original configuration was carried out using the commercial simulator Aspen PlusTM. Its internal routine RateFrac based on non- equilibrium stages was used to model the process. Although the column is operated under the condition of low pressure, the Redlich- Kwong Equation of State was used to describe the vapour phase. After several tests, the two- parameter version of the Wilson Eq. was chosen to describe the liquid phase behaviour. A comparison between the real and the simulated data (see Table 1) indicates that the selected modelling give a good agreement with the actual behaviour of the column.

The objective of this case study is to evaluate an alternative design for the distillation column used to purify EDC in the VCM plant such that the proposed modification is more energetically efficient than the actual configuration currently in operation. One attractive possibility is to use a heat pump scheme to replace steam, as the source of energy, for electrical energy.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/5719be611def8512f81d02d89648f5497379f99141c48c2aa5037d768690ed0d.jpg)  
Fig. 1. Actual configuration of the distillation system.

Table 1 Main results of the simulated column  

<table><tr><td rowspan="2">Available measurements for the column</td><td rowspan="2">Unit</td><td colspan="2">Actual</td><td colspan="2">Simulation</td></tr><tr><td>Distillate</td><td>Bottom</td><td>Distillate</td><td>Bottom</td></tr><tr><td>Temperature</td><td>℃</td><td>55.00</td><td>93.79</td><td>55.00</td><td>95.89</td></tr><tr><td>EDC</td><td>%</td><td>99.618</td><td>94.291</td><td>99.606</td><td>96.312</td></tr><tr><td>Tetrachloroethylene</td><td>ppm</td><td>140.566</td><td>7541.007</td><td>133.340</td><td>7528.010</td></tr><tr><td>1,1,2-Trichloroethane</td><td>ppm</td><td>14.799</td><td>21,394.996</td><td>12.668</td><td>23,502.150</td></tr></table>

The use of heat pump configurations to reduce the energy consumption in distillation columns is discussed in details in, e.g. King [5] and Henley and Seader [4]. In general, this is an alternative that should be considered at the first stages of design. But sometimes, it is economically viable to redesign a process in operation to include heat pumps, especially for intensively energetic processes.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/074601efc6fba02f8bbc6170ea6bd39520d08ed4ce744eb6f5a4fe978d5e1912.jpg)  
Fig. 2. Heat pump scheme used in this work.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/07afbbcf49e2bb6d9829af16032c43ac5c6293309424f92dc4b1c16a9b0498da.jpg)  
Fig. 3. Reboiler of the new configuration.

The heat pump scheme used in this work is depicted in Fig. 2. It consists of a relatively simple arrangement where the design task is to find a suitable temperature approach in the reboiler such that the thermodynamic efficiency of the system is increased with reduced irreversibility rates. The set- up for this model is described in the next paragraphs.

According to Smith et al. [6], well- designed compressors have efficiencies between 0.70 and 0.80; in this work an adiabatic compressor with an isentropic efficiency of 0.72 was considered. This choice leads to super- heating in its outgoing stream. As depicted in Fig. 2, the compressed gas heats up the bottom product in the reboiler producing the boil- up.

Fig. 3 shows a detailed scheme of the reboiler considered in this work. The vapour fraction of the stream to boil up is assumed equal to  $20\%$  w/w. According to Wallas [7], ideal vaporized fractions in reboilers are of  $10 - 35\%$  w/w. The heating medium is totally condensed at the reboiler outlet. The reboiler temperature difference is the temperature difference between streams to condenser and from the bottom.

The same condenser currently in operation was considered for the new configuration.

The procedure used to simulate the new configuration consisted on simulating five sub- configurations. Four of these sub- configurations are based on four levels of temperature differences in the reboiler, namely 1, 10, 20, and  $30^{\circ}\mathrm{C}$ , that is, for each one of these sub- configurations there was a related area in the reboiler and a defined power to be supplied to the compressor. The fifth configuration considers the original reboiler and in this case the temperature difference is found to be  $2.82^{\circ}\mathrm{C}$ .

The simulation results in Fig. 4 show that the reboiler exchanger area decreases with increase temperature difference and seems to level off at about  $300\mathrm{m}^2$  while the compressor power increases very sharply. This suggests

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/063e91275ece61bdcde71c2cd21c6b8196b593a6891646a8a1dd83241869dce3.jpg)  
Fig. 4. Reboiler area and compressor power profiles.

that the benefit of using large temperature differences through the reboiler in an attempt to reduce heat exchange area, and hence capital cost of this equipment, is overcome by the need of a large compressor, eventually soaring capital costs.

Because of its high temperature and flow rate, the still hot stream leaving the reboiler can be further used, for example, to exchange heat with other streams in the VCM plant. Another attractive option would be to feed the cracking furnace directly with this stream so fuel gas could be saved. Fig. 5 depicts the temperature behaviour of this stream.

# 4. Exergetic analysis

Irreversibility rates and efficiencies for the equipments involved in all configuration schemes are calculated based on the equations described in Araujo [8]: efficiencies are calculated according to the procedure proposed in Kotas [1] and stream exergy calculations are carried out based on the procedure proposed in Hinderink et al. [2]. All thermodynamic properties are obtained from the simula tions in Aspen PlusTM. The main results are discussed in what follows.

As the composition of the streams in the system are practically due to EDC (at least  $94\%$  w/w), there are some peculiar characteristics in this case study: almost all chemical exergy is due to EDC; exergy of mixture has a relatively very small value; exergy changes in the system are essentially related to physical exergy. Table 2 shows the calculated values of all forms of exergy involved in the original configuration (see Fig. 1).

In order to identify the main source of irreversibility, Table 3 presents the thermodynamic evaluation for each unit separately. The small irreversibility rate  $(242\mathrm{kW})$  and high efficiency  $(99.68\%)$  of the distillation column is because of the high concentration of EDC present in all streams in the system. Moreover, the physical exergy is the one that really makes the difference, particularly influenced by the boil up stream.

However, when the whole system is taken into account, i.e. when the reboiler and condenser are included, the thermodynamic efficiency turns out to be  $2.16\%$  the reason being the high exergy of the utilities as input to the computation of the efficiency (see Eq. (7)).

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/a25db5d6b2e4ecd7a10a92676ef58231aad0cf991701f97da0327a17398d38cd.jpg)  
Fig. 5. Reboiler warming stream outlet temperature.

Table 2 Calculated stream exergy of the original configuration  

<table><tr><td>Stream</td><td>Chemical exergy (kW)</td><td>Physical exergy (kW)</td><td>Exergy of mixture (kW)</td><td>Total exergy (kW)</td></tr><tr><td>Reflux</td><td>169,219.17</td><td>24.44</td><td>-9.41</td><td>169,234.20</td></tr><tr><td>Distillate</td><td>310,476.91</td><td>44.84</td><td>-17.27</td><td>310,504.47</td></tr><tr><td>Column bottom to reboiler</td><td>2,480,398.42</td><td>1968.61</td><td>-388.16</td><td>2,481,979.98</td></tr><tr><td>Top vapor</td><td>479,696.07</td><td>2172.59</td><td>-28.33</td><td>481,840.32</td></tr><tr><td>Boil up</td><td>2,480,398.42</td><td>4223.39</td><td>-388.16</td><td>2,484,233.65</td></tr><tr><td>T-1303T feed</td><td>86,406.16</td><td>5.77</td><td>-14.19</td><td>86,397.75</td></tr><tr><td>T-1301F feed</td><td>89,432.90</td><td>66.01</td><td>-11.59</td><td>89,487.32</td></tr><tr><td>T-1503F feed</td><td>129,487.02</td><td>105.67</td><td>-9.82</td><td>129,582.86</td></tr><tr><td>EDC IMP feed</td><td>70,100.84</td><td>27.41</td><td>-1.13</td><td>70,127.11</td></tr><tr><td>Bottom product</td><td>64,950.41</td><td>52.02</td><td>-17.25</td><td>64,985.18</td></tr></table>

There is much room to improve the heat exchange process in the condenser that has the largest exergetic loss (irreversibility rate) and the smallest thermodynamic efficiency. Figs. 6- 8 show the irreversibility rates and efficiencies of the five sub- configurations (marked along the plotted lines) for the compressor, reboiler, and condenser, respectively.

In Fig. 6, the continuous increase in the irreversibility rate of the compression process is due to the increase in the compressor outlet pressure. On the other hand, the thermodynamic efficiency increases only slightly. Therefore, the use of large compressors aiming to improve efficiency is not justified because of large values of irreversibility rates.

Table 3 Thermodynamic evaluation results of the original configuration  

<table><tr><td>Unit/process</td><td>Irreversibility rate (kW)</td><td>Rational efficiency (%) [1]</td></tr><tr><td>Reboiler</td><td>887.00</td><td>71.76</td></tr><tr><td>Condenser</td><td>1731.97</td><td>17.59</td></tr><tr><td>Column</td><td>242.45</td><td>99.68</td></tr><tr><td>Global</td><td>2861.42</td><td>2.16</td></tr></table>

It can be seen in Figs. 7 and 8 that the irreversibility rate in the reboiler is approximately three times larger than that in the condenser, while the efficiency is approximately five times larger because the reboiler is now the top condenser of the distillation process and the condenser is simply used for temperature reduction (the pressure being reduced by expansion through a valve) in order to deliver the reflux required by the distillation column as well as the distillate. Thus, all efforts should be concentrated in reducing the irreversibility rate in the reboiler.

Fig. 9 shows the overall irreversibility rate and efficiency of the five sub- configurations. The units that most influence this behaviour are the reboiler and the condenser. From an

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/0b9cc413468fed60e4447ed06e108ef59ed54d87188b19b1f2bc27fecc7d0965.jpg)  
Fig. 6. Irreversibility rate and efficiency of the compression process.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/92df1ca4f81ed8ae093902a5f6cfec3fb4c845d86b627d70dc495de479acd427.jpg)  
Fig. 7. Irreversibility rate and efficiency of the reboiler.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/a04bc1da508dcd456ba5837cb998845886759f89b85f5f1af1fef3d191968747.jpg)  
Fig. 8. Irreversibility rate and efficiency of the condenser.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/7585fccc7dc5b83f55c429b1e3b3fbd3ab826ebb25f1ed06ddcf25f69bb5ddb5.jpg)  
Fig. 9. Overall irreversibility rate and efficiency of the new sub-configuration.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/bfacf6712fe68cb1ef381aa5971c35fcefd2f09bba49f1b282397bfe88005b16.jpg)  
Fig. 10. Irreversibility rate distribution of the considered configurations.

![](https://cdn-mineru.openxlab.org.cn/extract/f01920ca-259b-4f31-899f-ae521c12b9ce/404b641833705dec9ad94a98c975a04d0268814718e6ff1d724510b6aafff22a.jpg)  
Fig. 11. New configuration overall efficiency.

exergetic standpoint, the best sub- configurations are those related to smaller temperature differences.

Fig. 10 shows a diagram in which is presented the irreversibility rate distribution for the original and the five sub- configurations. The substantial reduction in the condenser irreversibility rate is due to the reduction of the heat exchanged in this equipment because all latent heat is exchanged in the reboiler. For temperature differences of more than  $10^{\circ}\mathrm{C}$  the reboiler irreversibility rate becomes larger than that of the original configuration. For temperature differences less than  $10^{\circ}\mathrm{C}$  the total irreversibility of the sub- configurations is more than  $50\%$  smaller than the original configuration. For temperature differences larger than  $30^{\circ}\mathrm{C}$  the irreversibility rate of the new sub- configurations becomes larger than that of the original configuration mainly because of the reboiler influence.

In order to compare, results obtained by procedures proposed by Kotas [1] (see Eq. (7)) and Henley and Seader [4] (see Eq. (9)), Fig. 11 depicts the profile of efficiency against temperature difference in the reboiler. A very important observation from Fig. 11 is the perfect similarity between the profiles of the overall efficiency calculated by Kotas [1] in comparison with that proposed by Henley and Seader [4]. Although they have different numerical values, they provide the same response, so, one or another form to represent the global efficiency of the process is perfectly acceptable.

# 5. Conclusion

The exergetic method is a very important tool in process thermodynamic analysis, allowing the identification of local and global irreversibility rates (exergetic losses), and efficiencies. The calculation of both these variables and not only one or another separately is of vital importance in order to guarantee successfully a final accurate decision about process modifications.

Comparison between the real and simulated data for the original configuration presented an excellent agreement, which leads to conclude that the selection of the thermodynamic and column models was correct. From a thermodynamic approach, the high efficiency of the column is due to the high concentration of DOE present in all streams. However, for the whole system the thermodynamic efficiency is very low. The major option to improve the thermodynamic efficiency of the whole process is to reduce the exergy losses in the new reboiler.

In agreement with literature, a vapour compression heat pump improves the thermodynamic performance of a distillation column. The substantial reduction in the condenser irreversibility rate of the original configuration in relation to that of the new sub- configurations is the principal reason of the improvement in the thermodynamic efficiency.

The procedures defined by Kotas [1] and Henley and Seader [4] to perform thermodynamic analysis yield the same profiles and tendencies for calculation of global efficiencies of processes. The principal advantage of Kotas's procedure is to allow the computation of irreversibility rates and efficiencies of the various parts that comprise the whole process in a very explicit and objective way which represents a great difference in the investigation of possible exergetic improvement options of the process. It is important to note that the use of Kotas's procedure is more interesting when the three parts that form the exergy of a given stream are calculated separately as proposed by Hinderink et al. [2].

# Acknowledgments

The authors are grateful to Braskem Company for the permission to publish this work.

# References

[1] Kotas TJ. The exergy method of thermal plant analysis. FL: Krieger Publishing Company; 1995.  [2] Hinderink AP, Kerkhof FPYM, Lie ABK, De Swaan Arons J, Van Der Kooi HJ. Exergy analysis with a flowsheeting simulator—I. Theory: calculating exergies of material streams. Chem Eng Sci 1996;51:4693- 700.  [3] Cornelissen RL. Thermodynamics and sustainable development—the use of exergy analysis and the reduction of irreversibility. The Netherlands: University of Twente; 1997.

[4] Henley EJ, Seader JD. Equilibrium- stage separation operations in chemical engineering. New York: Wiley; 1981.  [5] King CJ. Separation process. New York: McGraw- Hill Book Company; 1971.  [6] Smith JM, Van Ness HC, Abbott MM. Introdução à Termodinâmica da Engenharia Química. Rio de Janeiro: LTC Editora; 2000.  [7] Walas SM. Chemical process equipment—selection and design. USA: Butterworths Publishers; 1988.  [8] Araújo ACB. Master thesis, Federal University of Campina Grande, Brazil; 2003.