# Broadband Terahertz Source Based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

## 第 1 部分

We are IntechOpen, the world’s leading publisher of Open Access books built by scientists, for scientists.

| Open access books available | International authors and editors | Downloads |
|-----------------------------|-----------------------------------|-----------|
| 7,500                       | 196,000                           | 215M      |

Our authors are among the TOP 1% most cited scientists.

| Countries delivered to | Contributors from top 500 universities |
|-----------------------|----------------------------------------|
| 154                   | 14%                                    |

Selection of our books indexed in the Book Citation Index in Web of Science™ Core Collection (BKCI).

Interested in publishing with us? Contact book.department@intechopen.com.

Numbers displayed above are based on latest data collected. For more information visit www.intechopen.com.

---

## 第 2 部分

```markdown
# Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

## 1. Introduction

Terahertz (THz) radiation, which is electromagnetic energy at frequencies in the nominal range of 10¹¹ to 10¹³ Hz (0.1-10 THz), is being studied for at least 18 different applications including urgent needs for medical diagnosis and security applications for the detection of non-metallic concealed weapons, biological and chemical agents, and explosives. However, the present sources of THz radiation present “hurdles” because of their limited tunable bandwidth and output power, and some require fragile, large, and expensive femtosecond lasers or even particle accelerators. Some of the methods that have been used to generate THz radiation are backward wave oscillators with chains of frequency multipliers, the Smith-Purcell Effect, quantum cascade lasers, synchrotron radiation from high-energy accelerators, bulk electro-optic rectification and ultrafast charge transport in semiconductors, and photomixing in semiconductors. For example, photomixing (optical heterodyning) of two lasers at different wavelengths in low-temperature-grown (LTG) GaAs at the feed point of an antenna can generate an output power of only 1 μW at 1 THz, which falls off by 12 dB per octave or 1/F⁴ at higher frequencies (F), so the power is reduced to 100 pW at 10 THz.

In field emission, an intense electric field of about 5 V/nm is applied to the surface of a metal or other electrical conductor to lower the potential barrier so that electrons are emitted into the surrounding vacuum by quantum tunnelling. The current density for emitters that are made of refractory metals such as tungsten may be as high as 10⁹ A/m² in steady state, or 10¹² A/m² when the applied electric field is pulsed. Some have used field emitters in place of heated filaments as the electron source in microwave triodes, klystrons, traveling-wave tubes, and the closely-related monotron. Others have used femtosecond lasers to obtain pulses of electrons that are shorter than 70 fs in laser-assisted field emission and analysis shows that there is a fundamental limit at 2 fs. However, we have not been able to find any presentation by...
```

(Note: The content provided is a partial extraction based on the provided text. If there are tables or specific sections like 7.8 that need to be included, please provide that content for accurate conversion.)

---

## 第 3 部分

## 2. Photomixing in Laser-Assisted Field Emission

We have pioneered in the study of laser-assisted field emission (LAFE) as a new method to generate microwave and THz radiation with an unusually large tunable bandwidth. In effect, a nanoscale ultrafast non-linear optical medium is created in laser-assisted field emission because:

1. The field emitter is much smaller than the wavelength of the incident optical radiation so the potential of the tip oscillates to follow each cycle of this radiation.
2. The current responds to changes in the electric field with a delay of 2 fs.
3. This response is highly nonlinear.

LAFE has higher efficiency than non-linear optics materials because the Manley-Rowe relations, which limit the conversion efficiency of three-wave mixing in these materials, do not limit the efficiency in LAFE because of the cascaded processes in which optical radiation releases the stored electrical energy at the output frequencies.

We have made rigorous simulations of photomixing in laser-assisted field emission using density functional theory with Floquet methods to allow for single-photon and multiphoton processes. However, a much simpler procedure will be used here to obtain a closed-form solution that is consistent with the results from the more accurate methods. We begin with the simplified Fowler-Nordheim equation for the current density in field emission:

\[
J = A E^2 e^{-B/E} \tag{1}
\]

Here \( J \) and \( E \) are the current density and the electric field intensity in A/m² and V/m, respectively, \( A = 1.541 \times 10^{-6}/\Phi \), \( B = 6.831 \times 10^9 \Phi^{3/2} \), and \( \Phi \) is the emitter work function in eV. If two sinusoidal fields are superimposed on the static field \( E_0 \), and the frequency is low enough that the effects of the photon energy may be neglected, the following expression may be used for the applied field in Eq. (1) to obtain the modified current density:

\[
E = E_0 + E_1 \cos(\Omega_1 t) + E_2 \cos(\Omega_2 t) \tag{2}
\]

A Taylor series expansion of Eq. (1) about the operating point \((E_0, J_0)\), and simplification with trigonometric identities leads to the following expression for the total current where all terms at frequencies greater than the mixer term are deleted because the currents at the higher frequencies would be rapidly attenuated.

---

## 第 4 部分

```markdown
## Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

### Equations

The equations governing the system are as follows:

1. \( I = I_0 + I_D + I_M \)  (3)

2. \( I_D = I_0 \left( 1 + B + \frac{B^2 E_1 E_2}{E_0^2} \right) \)  (4)

3. \( I_M = I_0 \left( 1 + B + \frac{B^2 E_1 E_2 \cos(\Phi_1 - \Phi_2) t}{E_0^2} \right) \)  (5)

Equations (3)-(5) show that the two applied sinusoidal fields increase the dc current (optical rectification) and also generate a mixer current at the difference frequency. With optical radiation, where the effects of the photon energy may not be neglected, the major correction to these equations is the effect of a resonance between tunneling electrons and a radiation field (Hagmann, 1995A). This resonance, which is caused by reinforcement of the wave function through virtual photon processes, was later confirmed by others (Mayer & Vigneron, 2000; Mayer et al., 2002, 2003).

### Figures

Figures 1 and 2 show the gain in the power flux density, which increases \( E_1 \) and \( E_2 \) in Eqs. (4) and (5), for the resonance with tungsten emitters (Mayer & Vigneron, 2000) and (5, 5) armchair (metallic) CNT emitters (Mayer et al., 2002).

#### Fig. 1. Gain for tungsten emitters.

```
| Wavelength, nm | Gain (dB) |
|----------------|-----------|
| 100            | 50        |
| 200            | 40        |
| 300            | 30        |
| 400            | 20        |
| 500            | 10        |
| 600            | 0         |
| 700            | -10       |
| 800            | -20       |
| 900            | -30       |
| 1000           | -40       |
```

Modifying Eqs. (4) and (5) by allowing for the gain \( G \) (in dB), as shown in Figs. 1 and 2, the peak value of the mixer current in laser-assisted field emission is given by...
```

(Note: The content after "the peak value of the mixer current in laser-assisted field emission is given by..." was not provided in the original text and thus is not included in the Markdown output.)

---

## 第 5 部分

## Carbon Nanotubes

The equations governing the current in carbon nanotubes are given by:

\[
I = \frac{10^{G/10}}{1 + B + B^2} (P_1 + P_2)
\]

(6)

\[
I^D = \frac{2 \cdot 10^{G/10}}{1 + B + B^2} P_1 P_2 \cos(\phi_1 - \phi_2) t
\]

(7)

where \( P_1 \) and \( P_2 \) are the power flux densities of the two lasers at the field emitter, and \( \eta \) is the impedance of free-space (≈ 377 Ω).

| Wavelength, nm | Gain for (5,5) metallic CNT emitters |
|----------------|--------------------------------------|
| 100            | 60                                   |
| 200            | 9                                    |
| 300            | 2                                    |
| 400            | 2                                    |
| 500            | L                                    |
| 600            | 8                                    |
| 700            | 10                                   |
| 800            | 100                                  |
| 900            | 1000                                 |

**Fig. 2.** Gain for (5,5) metallic CNT emitters.

Our prediction of the resonance (Hagmann, 1995A) and first suggestions for microwave and terahertz devices based on LAFE (Hagmann, 1995B) were made at a time when the general consensus was that the increase in field emission current caused by a laser is a small effect due to heating of the emitter that has a time constant of 10 – 1000 μs (Lee & Robbins, 1989). Our measurements of optical rectification in LAFE with a sealed field emitter tube (Leybold AG model 55460) confirm that there is a thermal effect but they also show a non-thermal effect that is in agreement with our analysis and shows the effect of the resonance (Hagmann & Brugat, 1999). We measured a time constant of 300 μs for the decay of the thermal processes, and also found that the cathode-to-anode circuit for the sealed field emitter tube acts as a low-pass filter (Hagmann et al., 2004).

Microwave prototypes have been built and tested using emitters of tungsten and molybdenum (Hagmann, 2004). Two lasers are focused on the emitter to generate current oscillations at their difference frequency by LAFE, as described by Eq. (7). We do not specifically use the emitted electrons as such in our method, but instead we cause the current oscillations to generate a transverse-magnetic (TM) surface wave that propagates on extensions of the emitter (Alonso & Hagmann, 2001). This surface wave is coupled directly.

---

## 第 6 部分

## Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

It was already shown that photomixing in LAFE can provide an unusually large tunable bandwidth. However, the maximum power that we have obtained with microwave prototypes was only 50 pW. This limitation can be understood because the mixer current, which is a few percent of the dc field emission current (30 μA), is coupled to a 50 Ω load or an antenna having a similar value for its radiation resistance. Increasing the size of the emitter is not an effective means to obtain the higher current that is required for greater output power because surface imperfections (Fujieda et al., 2005) cause the dc emitted current to be proportional to A^(1/4), where A is the area of the emitter (Okawa et al., 1988). In the rest of this chapter, it will be seen that much greater output power may be obtained without sacrificing the large tunable bandwidth by using carbon nanotubes (CNT) in LAFE because of a synergy in which the CNT increase both the dc current and the impedance which is seen by the mixer current.

### 3. Carbon Nanotubes as High Impedance Transmission Lines

Equation (7) shows that photomixing in LAFE requires incident electric fields at two different frequencies in order to generate a mixer current at a third frequency which is the difference of the first two frequencies. The output power that is coupled to the TM surface waves that propagate on extensions of the emitter is given by:

\[
P_{\text{OUT}} = \frac{1}{2} Z_0 I_{\text{MP}}^2
\]

where \(Z_0\) is the (real) characteristic impedance for the transmission line which is a wire extension of the emitter and \(I_{\text{MP}}\) is the peak value of the mixer current which is given by Eq. (7). Thus, the output power is given by the following equation, and it is proportional to \(Z_0\) which shows the motivation for increasing this impedance in order to obtain greater output power.

\[
P_{\text{OUT}} = 2 Z_0 \left(1 + B + B^2\right) \frac{I_0^2}{10^{G/5}} P_P
\]

The interaction of the mixer current with the impedance \(Z_0\) creates an electric field at the mixer frequency, which has a peak value that is given by:

\[
E_{\text{MP}} = Z_0 I_{\text{MP}}
\]

Thus, for consistency, it would be necessary to include this electric field in Eq. (2), which reduces the current from optical rectification as well as the mixer current. This negative feedback sets an upper limit on the output power which is consistent with the power that is supplied by the two lasers. However, the effect of this negative feedback is generally negligible unless \(Z_0\) exceeds 1 MΩ which does not occur with carbon nanotube transmission lines (Hagmann, 2008).

Others have simulated single-wall (Burke, 2002, 2003) and multiwall (Tarkiainen et al., 2001; Sonin, 2001; Bachtold, 2001) carbon nanotubes (SWCNT and MWCNT) on a conducting substrate as transmission lines by using a hybrid approach in which quantum theory is combined with classical distributed element transmission line models (Collin, 1990).

---

## 第 7 部分

# Carbon Nanotubes

The method allows for the effects of the size and shape of the carbon nanotube (CNT) and the insulation separating it from the conducting substrate, as well as the electronic properties of the CNT from quantum theory. These studies show that the characteristic impedance is on the order of 5 kΩ, which may be understood because the distributed kinetic inductance of the CNT is approximately 10^4 times the inductance for metals. The high value for the kinetic inductance of MWCNT was verified by measurements, and it has been suggested that CNT on conducting substrates could be used as high-impedance transmission lines in nanoelectronics.

We have extended the previous simulations which were made by others in order to study CNT that are isolated, removed from the substrate, as transmission lines. The previous work by others was based on the classical distributed element model for a two-conductor transmission line that is formed by the CNT and its image in the substrate, for which the propagation is in a transverse electromagnetic (TEM) wave. However, as a wire is moved away from a conducting surface, there is a transition from TEM propagation to a TM surface wave which is the dominant mode for an isolated wire. Thus, we developed a classical distributed-element model for propagation of the TM surface wave and then added the quantum inductance and the quantum capacitance to this model as it has been done by others.

Highlights of the results of our simulations of isolated CNT as transmission lines follow:

1. Only the axially-symmetric TM surface wave mode will propagate on an isolated SWCNT. This is consistent with the observation that higher order modes cannot propagate on a metal cylinder having a circumference which is less than one free-space wavelength. Single-mode propagation is necessary to prevent dispersion of the propagating electromagnetic fields.
2. At THz frequencies all of the metallic tubes in an isolated MWCNT can take part in the propagation so that for N shells there are N – 1 propagating coaxial modes in addition to the axially-symmetric TM surface wave mode. Thus, in order to prevent dispersion, only SWCNT should be considered for this application.
3. The axially-symmetric TM surface wave mode in an isolated SWCNT has a characteristic impedance of approximately 44 kΩ. This value is much greater than that for a CNT on a conducting substrate because the capacitance to the substrate has been eliminated.
4. The axially-symmetric TM surface wave mode in an isolated SWCNT has a phase velocity of approximately 2.8 x 10^6 m/s, which is 0.9 percent of the velocity of light in vacuum. The reduced value of the phase velocity is consistent with the increased value of the characteristic impedance.
5. The axially-symmetric TM surface wave mode in an isolated SWCNT has negligible attenuation for propagation over the lengths that will be used in this application. Low ohmic loss is also found with surface waves on a single conducting cylinder, but the energy is loosely bound to the cylinder so it is necessary to keep other objects at a distance to limit radiative loss. Our applications fall under what has been called the "low-loss regime" for propagation on CNT.

---

## 第 8 部分

## 4. Measurements with Individual CNT

### 4.1 Description of the prototypes

In 2004, we began our study of LAFE with single SWCNT and MWCNT, funded by the National Science Foundation (NSF-DMI-0338928). Four custom sealed field emission tubes with CNT were made for us by Xintek (Chapel Hill, NC, U.S.A.), having the same outer structure which is shown in Fig. 3. The copper anode is at the right, and the CNT emitter is mounted on a tungsten wire that is attached to the metal cylinder at the left. Figure 4 shows an SEM image of one of the emitters, taken with a JEOL JEM 6300 before it was placed in one of these tubes.

**Fig. 3.** Field emission tube made for us by Xintek.

**Fig. 4.** SEM image of the CNT emitter in tube C-3.

---

## 第 9 部分

## Carbon Nanotubes

Most of the measurements of field emission from CNT pertain to the dc characteristics of films (Zhu et al., 1999), arrays (Lim et al., 2001), and composites (Wang et al., 1998), which only provide a statistical evaluation of the properties with large numbers of CNT. Furthermore, the electric field, and thus the total emitted current, is reduced when the CNT are close together (Hii et al., 2006). Careful measurements with individual CNT have shown that the field enhancement factor and work function varies with the structure of the CNT and its surface conditions (Xu et al., 2005). Other measurements with single CNT have shown that field emission is affected by irregularities in the structure of the graphitic sheets (Wang et al., 2005), and time-dependent deformations due to reconstruction at the apex increase the electric field at specific sites which are where the field emission occurs (Kuzumaki et al., 2004). Therefore, we chose to begin our studies LAFE with tubes having individual CNT as the emitters.

The two tubes labeled M-1 and M-4 have a single MWCNT as the emitter, and tubes C-3 and C-6 each have a single SWCNT as the emitter. The CNT are in bundles with diameters of 10 to 30 nm that are shaped so that field emission is only from the single CNT at the end of each bundle where the electric field is most intense. A sealed field emitter tube, with an etched tungsten single crystal tip as the emitter (Leybold AG model 55460) was used for comparison in the measurements with the four tubes from Xintek. The characteristics of these five tubes are described in the following sections:

### 4.2 Fowler-Nordheim characterization of the prototypes

First, the dc current-voltage characteristics were measured for each of the five field emission tubes, and then these data were analyzed using the following procedure that is based on the simplified Fowler-Nordheim equation which was shown as Eq. (1).

The measured field emission current \( I \) is proportional to the current density \( J \), and the measured voltage \( V \) is proportional to the applied electric field \( E \), so Eq. (1) is equivalent to the following expression that may be used with the measured data:

\[
I = C V^{\frac{D}{2}} \quad (9)
\]

Equation (9) may be written in the following form:

\[
\ln I = \ln (C) + \frac{D}{2} \ln V \quad (10)
\]

Thus, the values of the parameters \( C \) and \( D \) for each field emission tube may be determined from the slope and intercept of a graph in which the ordinate and abscissa are \( \ln(1/V^2) \) and \( 1/V \), respectively. The values of the parameters \( A \) and \( B \) in Eq. (1) are calculated from the work functions \( \phi = 4.5 \, \text{eV} \) for tungsten, and \( 4.9 \, \text{eV} \) for graphene in the CNT. Then the following two parameters may be calculated:

\[
S = \frac{CD^2}{AB^2}; \quad R = \frac{D}{B}
\]

Here \( S \) is called the effective area of the emitter, and \( R \) is called the effective radius of the emitter.

---

## 第 10 部分

Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

During the measurements a ballast resistor of 100 MΩ was placed in series with each field emission tube to protect it by limiting the maximum current. The tungsten emitter is mounted on a filament so it was cleaned by electrical heating before each measurement. It is not possible to clean the CNT, which is probably the cause for the “switch-on” effect in which the supply voltage must be momentarily increased beyond the operating point to initiate field emission with the CNT (Liu & Fan, 2005).

Figure 5 is a Fowler-Nordheim Plot of the data for tube C-6, showing that a straight line is an excellent fit of the data which is consistent with Eq. (10). Linear regressions were made to obtain the values of C, D, S, and R for each field emission tube, which are shown in Table 1. Typically the correlation was approximately -0.998, the standard variance was 0.08, and the probability for the null-hypothesis that no linear relationship exists, was less than 0.0001.

!Fig. 5. Fowler-Nordheim plot with the data for tube C-6.

| Emitter | Leybold | M-1 | M-4 | C-3 | C-6 |
|---------|---------|-----|-----|-----|-----|
| Φ, eV   | 4.5     | 4.9 | 4.9 | 4.9 | 4.9 |
| A, A/V² | 3.42x10⁻⁷ | 3.14x10⁻⁷ | 3.14x10⁻⁷ | 3.14x10⁻⁷ | 3.14x10⁻⁷ |
| B, V/m  | 6.52x10¹⁰ | 7.41x10¹⁰ | 7.41x10¹⁰ | 7.41x10¹⁰ | 7.41x10¹⁰ |
| C, A/V² | 2.15x10⁻⁷ | 2.20x10⁻⁹ | 3.47x10⁻⁹ | 7.72x10⁻¹¹ | 1.27x10⁻⁸ |
| D, V    | 5.89x10⁴ | 8.02x10³ | 7.92x10³ | 4.84x10³ | 5.60x10³ |
| S, m²   | 5.14x10⁻¹³ | 8.19x10⁻¹⁷ | 1.26x10⁻¹⁶ | 1.05x10⁻¹⁸ | 2.31x10⁻¹⁶ |
| R, m    | 9.03x10⁻⁷ | 1.08x10⁻⁷ | 1.07x10⁻⁷ | 6.53x10⁻⁸ | 7.55x10⁻⁸ |
| R*, m   | 2.86x10⁻⁷ | 3.61x10⁻⁹ | 4.48x10⁻⁹ | 4.08x10⁻¹⁰ | 6.06x10⁻⁹ |
| R/R*    | 3.16    | 29.9 | 23.9 | 167 | 12.5 |

Table 1. DC measurements and Fowler-Nordheim analysis of the data.

---

## 第 11 部分

```markdown
## Carbon Nanotubes

In Table 1, R* is an alternative effective radius of the emitter that is calculated from the effective area of the emitter S, assuming that the shape is a hemisphere. The parameters R and S correspond to the ideal case in which the current density is constant over the area S and zero elsewhere, and the radius of curvature in the area S is equal to R. Leybold states that their emitters of etched single-crystal tungsten have a radius of 100 to 200 nm, which is reasonable agreement with the values in the table. The values of R/R* suggest that the field emission from the CNT may have come from an extended length. The unusually large value for tube C-3 suggests that multiple SWCNT may contribute to the current, which is consistent with the SEM images that show the bundle of SWCNT is wider than it is for C-6.

### 4.3 Measurements of mixing at audio frequencies

We have made rigorous quantum simulations of LAFE (Hagmann, 1999B) which show that the radiation from two lasers increases the dc current (optical rectification) and also causes harmonics and mixing terms with frequencies that are given by n1f1 + n2f2, where f1 and f2 are the frequencies of the two lasers and the integers n1 and n2 may be positive, zero, or negative. Closed-form expressions have been derived for these terms by using an adiabatic approximation, as was done to obtain Eqs. (1)-(5) which only address optical rectification and mixing at the difference frequency. The terms at frequencies higher than these two are not of immediate interest for photomixing because they would be highly attenuated.

However, we made measurements with the five field emission tubes at audio frequencies, where the circuit effects of the sealed tubes do not severely impede the response (Hagmann et al., 2004), to confirm our derivations and demonstrate the action of these devices as mixers.

Two sinusoidal signals, at the frequencies f1 = 1.67 kHz and f2 = 1.10 kHz, were superimposed on the high voltage that is fed to a field emission tube, and components of the field emission current at the frequencies f1, f2, 2f1, 2f2, f1 + f2, and f1 - f2, as well as the rectified current. The six frequencies correspond to 1.67, 1.10, 3.34, 2.20, 2.77 and 0.57 kHz, respectively. The high voltage path of the measurement circuit consisted of the high-voltage power supply, a 100 MΩ ballast resistor, the secondary windings of two transformers, the field emission tube, a dc microammeter, and a 1 MΩ resistor to ground which was a shunt for measuring the current with a digital oscilloscope. The two transformers were used to couple two floating battery-operated Wein bridge oscillators in order to superimpose signals at each of the two frequencies with a potential of 120 V on the dc high voltage. Capacitive shunts across the high-voltage power supply, the ballast resistor, and the dc microammeter were used to simplify the ac equivalent circuit.

With the Leybold tube, the currents at the fundamental frequencies f1 and f2 were each within 5% of the predicted values, and the rectified current and the currents at each of the other 4 frequencies were each within 10% of the predicted values. However, it was necessary to use fourth order terms (proportional to the fourth derivative) in the Taylor’s series to obtain this accuracy. The rectified current and the currents at the 6 frequencies were each within a factor of 2 of the predicted values for tubes M-4 and C-6, and within a factor of 3 for tube M-1. However, tube C-3 was too unstable to permit measuring the currents at any of the six frequencies. As noted earlier, it is not possible to clean the CNT, and this causes the parameters in Table 1 to be less reproducible than it is for the Leybold.
```

---

## 第 12 部分

## Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

We attribute the larger errors in the measurements with the CNT to this effect. Nevertheless, the rectified current and the mixer current were measured with three of the four prototypes using individual CNT, and the values are in reasonable agreement with our analysis.

### 4.4 Measurements of Optical Rectification

It was not possible to measure photomixing with the five tubes because they do not contain the special structures that are required to output microwave or THz energy in order to make such measurements (Alonso & Hagmann, 2001). However, we did measure the rectified current that is caused by a single laser diode (20 mW, 658 nm), and Eqs. (6) and (7) show that if two lasers with the same power were used the peak value of the mixer current would be two times the rectification current that we measured.

Figure 6 is a block diagram showing the experimental configuration that was used to measure optical rectification.

```
| Component                | Description                          |
|--------------------------|--------------------------------------|
| Fluke                    | Micro Ammeter                        |
| HV                       | IM Cnm                               |
| Laser Diode              | Amplitude-modulated with square-wave |
| Digitizing Oscilloscope   | Used to measure time dependence      |
| Pulse Generator          | Provides TTL signal                  |
| Analog Oscilloscope      | Measures the response                |

**Fig. 6.** Experimental configuration used to measure optical rectification.

The laser diode was amplitude-modulated with a square-wave envelope (TTL) by the pulse generator, and a digitizing oscilloscope was used to measure the time dependence of the response of the current to the laser, as shown in the block diagram. The laser diode was maximally-focused to provide a measured Gaussian profile with a power flux density of approximately 10^7 W/m² at the emitter. The four prototype tubes were designed to have a long cylindrical glass window with the emitter on the axis to permit the laser radiation to be normal to the glass for minimum distortion, and to reduce the optical path to limit divergence of the beam. However, tube C-6 could not be used in this test because ripples in the glass envelope prevented proper focusing of the laser radiation.

---

## 第 13 部分

Figure 7 shows the response of the current in tube M-4 as a function of the frequency at which the laser was modulated. The decay in the response is exponential, consistent with the equivalent circuits for the tubes (Hagmann et al., 2004) and the measurement circuit, and it does not show a limitation to the speed of the process of laser-assisted field emission.

| Leybold | M-1 | M-4 | C-3 | |
|---------|-----|-----|-----|---|
| I0, μA  | 8.0 | 1.0 | 1.0 | 1.0 |
| V0, V   | 4600| 980 | 840 | 920 |
| τ, μs   | 510 | 110 | 80  | 86  |
| ID, pA  | 16  | 56  | 83  | 48  |
| ID / I0, % | 0.20 | 5.6 | 8.3 | 4.8 |

**Table 2. Measurements of optical rectification.**

In Table 2, I0 is the dc field emission current and V0 is the dc voltage that is applied across each tube. This table shows that the mean increase in the dc current is 6.2 % for the 3 tubes with CNT emitters, as compared with 0.20 % for the Leybold tube. This shows that if two lasers with the same power were used for photomixing, the peak value of the mixer current would be 12 % of the dc current for the tubes with CNT, as compared with 0.40 % for the Leybold tube.

Two papers must be considered because they describe much larger changes in the field emission current being caused by laser radiation. An increase of the field emission current...

---

## 第 14 部分

## Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

by a factor of 19 was measured when a CW laser (10 mW, 633 nm) was focused on a CNT film (Cheng et al., 2004). However, the time constant for the increase in the current was 6 minutes, and the values are not consistent with our analysis of optical rectification, so it appears that this effect was caused by heat-related processes. An argon ion laser increased the field emission current from a single CNT by a factor of 300, or decreased by a factor of 50, depending on etching with oxygen, but this was also explained as a thermal process (Colbert & Smalley, 1995). These phenomena that are described in the two papers do not appear to be appropriate for generating microwave and terahertz radiation.

### 5. Photomixing with Clusters of Carbon Nanotubes

Consider a cluster of N transmission lines that are connected across a single load with an impedance \( Z_L \). The \( I_{th} \) transmission line has characteristic impedance \( Z_I \), propagation constant \( \beta_I \), length \( \Lambda_I \), and is fed by a constant current source with a peak value of \( I_I \). The phase shift that is caused by propagation over the full length of the \( I_{th} \) line is \( \theta_I \).

Figure 8 shows this system for only the two transmission lines for \( N = 2 \). Photomixing, caused by the radiation from two lasers that is focused on a field emitter at the free end of the \( I_{th} \) transmission line, generates a mixer current \( I_I \) which flows through this transmission line.

```
|   V1   |   Θ1   |   I1   | |
|--------|--------|--------|---|
|        |   Z1   |        | |
|   IN   |        |   ZL   |   VL   |
|        |   ZN   |        | |
|   ΘN   |        |   VN   | |

**Fig. 8.** Branching transmission lines with load.

For the special case where each transmission line has the same characteristic impedance \( Z_0 \) and the load has a real impedance \( R \), a broadband impedance match to the load occurs when \( N = Z_0/R \). If the mixer current in each transmission line has a peak value that is equal to \( I_M \), then the total current that is delivered to the load is equal to \( N I_M \). Thus, the total power that is delivered to the load is

\[
P_{OUT} = \frac{(N I_M)^2 R}{2} = \frac{I_M^2 Z_0^2}{2R}.
\]

---

## 第 15 部分

## Carbon Nanotubes

For example, let \( Z_0 = 44 \, k \Omega \) from Section 3 of this chapter, with \( R = 50 \, \Omega \), so that the total number of CNT in the cluster is given by \( N = 880 \). Assume that the dc field emission current from each CNT is \( I_0 = 10 \, \mu A \). Then the total dc field emission current is \( 8.8 \, mA \) and from section 4.4 the mixer current in each CNT is \( I_M = 0.12 I_0 \), or \( 1.2 \, \mu A \) peak. The total mixer current in the load would be \( 1.06 \, mA \) peak, for an output power of \( 28 \, \mu W \). This is \( 14 \, dB \) greater than that from photomixing in LTG GaAs (Verghese et al., 1997), but the most significant advantage of photomixing with clusters of CNT is the possibility of obtaining a much greater tunable bandwidth.

More generally, when there is not a perfect impedance match, reflected waves propagate on each transmission line and the voltage and current on the \( I^{th} \) transmission line are given by:

\[
V_I(z) = A e^{j \theta_I z} + B e^{-j \theta_I z} \tag{11}
\]

\[
I_I(z) = \frac{A_I e^{j \theta_I z}}{Z_I} + \frac{B_I e^{-j \theta_I z}}{Z_I} \tag{12}
\]

where the free end of the \( I^{th} \) line is at \( z = 0 \). Thus, the total current in the load is given by:

\[
I_L = \sum_{I=1}^{N} \frac{A_I e^{j \theta_I z}}{Z_I} + B_I e^{-j \theta_I z} \tag{13}
\]

The voltage across the load must be given by the following expression for all values of \( I \):

\[
V_L = A e^{j \theta_I} + B e^{-j \theta_I} \tag{14}
\]

But this voltage is related to the total current through the load by \( V_L = Z_L I_L \), which leads to a matrix equation that may be solved to determine the \( A \) and \( B \) coefficients in Eqs. (11)-(14).

For the special case where the characteristic impedance and phase delay of each transmission line are equal to \( Z_0 \) and \( \theta \), respectively, and the mixer current is the same in each line, the power that is delivered to the load is \( \gamma \) multiplied by what it would be for a single field emitter, where the multiplying factor \( \gamma \) is given by:

\[
\gamma = \frac{Z_0 N^2}{1 + \frac{N^2}{Z_L^2} \sin^2(\theta)} \tag{15}
\]

---

## 第 16 部分

## Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

### Table 1: Transmission Line Parameters

| N      | 10^0 | 10^1 | 10^2 | 10^3 | 10^4 | 10^5 |
|--------|------|------|------|------|------|------|
| N=5000 |      |      |      |      |      |      |
| N=2000 |      |      |      |      |      |      |
| N=1000 |      |      |      |      |      |      |
| N=500  |      |      |      |      |      |      |
| N=200  |      |      |      |      |      |      |
| N=100  |      |      |      |      |      |      |
| N=50   |      |      |      |      |      |      |
| N=20   |      |      |      |      |      |      |
| N=10   |      |      |      |      |      |      |
| N=5    |      |      |      |      |      |      |
| N=2    |      |      |      |      |      |      |

### Figure 6: Multiplying Factor γ as a Function of the Number and Phase Delay of the Transmission Lines

Figure 6 shows the multiplying factor γ as a function of the number and the phase delay of the transmission lines, where Z₀ = 1000 Zₗ. The horizontal line for N = 1000 corresponds to the broadband match for N = Z₀/R which has already been described. The following behavior is also seen from Eq. (15) and illustrated in Figure 6:

1. For small values of θ, γ = N², regardless of the values of Z₀ and Zₗ, because the N currents feed directly to the load. This is, it is best to have short transmission lines.
2. For θ = 90°, corresponding to quarter-wavelength transmission lines, γ = (Z₀/Zₗ)², regardless of the value of N, because the load projects an impedance Z₀²/NZₗ to each field emitter.
3. When Z₀ > Zₗ, if N > Z₀/Zₗ the gain decreases from N² to (Z₀/Zₗ)² as θ varies from 0° to 90°.
4. When Z₀ > Zₗ, if N < Z₀/Zₗ the gain increases from N² to (Z₀/Zₗ)² as θ varies from 0° to 90°.

### Consideration of Some of the Design Requirements

1. The lengths of the SWCNT must be less than one-quarter of the wavelength at the mixer frequency, 7.5 μm at 10 THz, so the mixer currents are generated in phase at the free ends of the SWCNT. The spread in the lengths must not exceed 100 nm at 10 THz so the mixer currents add in phase after propagating to the load on the SWCNT.
2. The common junction for the SWCNT may be the rounded end of a wire having a radius as small as 30 nm, depending on the size of the SWCNT (Verema et al., 2000).
3. The contact resistance between the SWCNT and the wire (Tersoff, 1999) must be mitigated by adding gold (Dockendorf et al., 2007) or nickel (Ribaya et al., 2008), or by other means (Kim et al., 2008) at the common junction.

---

## 第 17 部分

```markdown
## 6. Transmission Lines and Antennas for the Output

### 6.1 Carbon Nanotube Transmission Lines
The wire from the common junction could be used as a CNT transmission line to propagate energy to the load. In this case, the characteristic impedance of the transmission line must be equal to the load impedance or be tapered to provide a broadband impedance match to the load. In section 3 of this chapter, we noted that others have shown that CNT on a conducting substrate are TEM transmission lines with a characteristic impedance of approximately 5 kΩ, and isolated SWCNT have a characteristic impedance of approximately 44 kΩ. However, a much lower impedance, such as 50 Ω, is required because the output power varies inversely with the impedance.

### 6.2 Other Types of Transmission Lines
The wire from the common junction could also be used as another type of transmission line to propagate energy to the load. Again, the characteristic impedance of the transmission line must be equal to the load impedance or be tapered to provide a broadband impedance match to the load. Our group has studied the use of single metallic wires to propagate THz radiation as TM surface waves with enhanced confinement because of surface plasmons (Hagmann, 1998B; Alonso & Hagmann, 1999), and used metallic wires for this purpose in a microwave prototype (Hagmann, 2004). However, the characteristic impedance of this type of transmission line is approximately equal to the impedance of free-space (≈ 377 Ω). A much lower impedance is required in order to provide greater output power. One possibility is the parallel-plate plasmonic transmission line which can provide an impedance of 50 Ω for TEM mode propagation at THz frequencies with a cut-off frequency of zero Hz (Ghamsari et al., 2008). The common junction of the CNT could be attached to one plate of this transmission line with the other plate grounded.

### 6.3 Carbon Nanotube Antennas
The wire from the common junction could be used as a CNT antenna to generate THz radiation. In this case, the radiation resistance and reactance of the antenna would constitute the load impedance. The electrical conductivity of CNT is several times larger than copper, but the diameter is small so the resistive losses are high (Burke et al., 2006). Thus, it may be practical to use short CNT in dipoles, but structures that must be much larger than a...
```

(Note: The text has been formatted according to the provided instructions, with headers and footers removed, and the content structured in Markdown format. The content from Section 6 has been preserved as requested. If there are tables or figures in the original document, please provide that content for accurate conversion.)

---

## 第 18 部分

## 6.4 Other types of antennas

The wire from the common junction could be used as another type of antenna to generate THz radiation. Again, the radiation resistance and reactance of the antenna would constitute the load impedance. A variety of different types of antennas have been used at THz frequencies including dipole and bow tie (Yano et al., 2005), spiral (Verghese et al, 1997), and log-periodic structures (Mendis et al., 2005). We have also studied the zigzag antenna for broadband applications of LAFE at THz frequencies (Alonso et al., 2001).

Parallel-plate transmission lines have been used with lenses to obtain highly focused THz radiation comparable to that expected for a 3-D optical element in free-space (Dai et al., 2004). This method shows promise for coupling energy from the common junction because it would be possible to obtain an impedance of 50 Ω for TEM mode propagation at THz frequencies with a cut-off frequency of zero Hz (Ghamsari et al., 2008). As was already noted in section 6.2, the common junction of the CNT could be attached to one plate of this transmission line with the other plate grounded.

## 7. Conclusions

Photomixing in laser-assisted field emission shows considerable promise as a means to generate microwave or THz radiation with an extremely large tunable bandwidth. However, our simulations and measurements with microwave prototypes show that the output power is quite limited because of the small value for the dc field emission current. This chapter presents further simulations, and measurements with prototypes in which the field emission is from individual CNT, which suggest that it may be able to obtain an output power of 10 μW over a tunable bandwidth ratio of at least 10:1. We are continuing to develop such advanced sources with the objective of providing new devices that are needed for the many different applications of THz radiation (Davies et al., 2002). We also hope that this effort will continue to lead to a more fundamental understanding of the process of quantum tunneling (Hagmann, 1992; Hagmann et al, 1993; Hagmann, 1995A).

## 8. References

- Ahlskog, M., Hakonen, P., Paalanen, M., Roschier, L., and Tarkiainen, R. (2001). Multiwalled carbon nanotubes as building blocks in nanoelectronics. J. Low Temp. Phys. 124, 335-352.
- Alonso, K., and Hagmann, M.J. (1999). Use of Goubau line to couple microwave signals generated by resonant laser-assisted field emission. Ultramicroscopy. 79, 175-179.
- Alonso, K., and Hagmann, M.J. (2001). Comparison of three different methods for coupling of microwave and terahertz signals generated by resonant laser-assisted field emission. J. Vac. Sci. Technol. B 19, 68-71.
- Bachtold, A., de Jonge, M., Grove-Rasmussen, K., McEuen, P.L., Buitelaar, M., and Schonenberger, C. (2001). Suppression of tunneling into multiwall carbon nanotubes. Phys. Rev. Lett. 87, 166801 (4 pp).

---

## 第 19 部分

## Carbon Nanotubes

Barlow, H.M., and Cullen, A.L. (1953). Surface waves. Proc. IEE. 100 (III), 329-347.
Bonard, J.-M., Stockli, T., Maier, F., de Heer, W.A., Chatelain, A., Salvetat, J.-P., and Forro, L. (1998). Field-emission-induced luminescence from carbon nanotubes. Phys. Rev. Lett. 81, 1441-1443.
Burke, P.J. (2002). Luttinger liquid theory as a model of the Gigahertz electrical properties of carbon nanotubes. IEEE Trans. Nanotechnology. 1, 129-144.
Burke, P.J. (2003). An RF circuit model for carbon nanotubes. IEEE Trans. Nanotechnology. 2, 55-58.
Burke, P.J., Li, S., and Yu, Z. (2006). Quantitative theory of nanowire and nanotube antenna performance. IEEE Trans. Nanotechnology. 5, 314-334.
Carr, G.L., Martin, M.C., McKinney, W.R., Jordan, K., Neil, G.R. and Williams, G.P. (2002). Very high power THz radiation at Jefferson Lab. Phys. Med. Biol. 47, 3761-3764.
Cheng, H.-F., Hsieh, Y.-S., Chen, Y.-C., and Lin, I.-N. (2004). Laser irradiation effect on electron field emission properties of carbon nanotubes. Diam. Relat. Mater. 13, 1004-1007.
Colbert, D.T., and Smalley, R.E. (1995). Electric effects in nanotube growth. Carbon. 33, 921-924.
Collin, R.E. (1990). Field Theory of Guided Waves. IEEE Press, New York, 2nd ed.
Dai, J., Coleman, S., and Grischkowsky, D. (2004). Planar THz quasioptics. Appl. Phys. Lett. 85, 884-886.
Davies, A.G., Linfield, E.H., and Johnston, M.B. (2002). The development of terahertz sources and their applications. Phys. Med. Biol., 47, 3679-3689.
Dockendorf, C.P.R., Steinlin, M., Poulikakos, D., and Choi, T.-Y. (2007). Individual carbon nanotube soldering with gold nanoink deposition. Appl. Phys. Lett. 90, 193116 (3 pp).
Fujieda, T., Hidaka, K., Hayashibara, M., Kamino, T., Ose, Y., Abe, H., Shimizu, T., and Tokumoto, H. (2005). Direct observation of field emission sites in a single multiwalled carbon nanotube by Lorentz Microscopy. Jpn. J. Appl. Phys. 44, 1661-1664.
Ghamsari, B.G., and Majedi, A.H. (2008). Terahertz transmission lines based on surface waves in plasmonic waveguides. J. Appl. Phys. 104, 083108 (9 pp).
Gomer, R. (1993). Field Emission and Field Ionization. American Institute of Physics, New York.
Goubau, G. (1950). Surface waves and their application to transmission lines. J. Appl. Phys. 21, 1119-1128.
Hagmann, M.J. (1992). Quantum Tunneling Times: A New Solution compared to Twelve other Methods. Int. J. Quant. Chem. 44, 299-309.
Hagmann, M.J. (1995A). Mechanism for resonance in the interaction of tunneling particles with modulation quanta. J. Appl. Phys. 78, 25-29.
Hagmann, M.J. (1995B). Simulations of the interaction of tunneling electrons with optical fields in laser-illuminated field emission. J. Vac. Sci. Technol. B 13, 1348-1352.
Hagmann, M.J. (1997). Simulations of laser-assisted field emission within the local density approximation of Kohn-Sham density-functional theory. Int. J. Quant. Chem. 65, 857-865.
Hagmann, M.J. (1998A). Stable and efficient numerical method for solving the Schrödinger Equation to determine the response of tunneling electrons to a laser pulse. Int. J. Quant. Chem. 70, 703-710.

---

## 第 20 部分

```markdown
# Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

| Author(s) | Year | Title | Journal | Volume | Pages |
|-----------|------|-------|---------|--------|-------|
| Hagmann, M.J. | 1998B | Simulations of the generation of broadband signals from DC to 100 THz by photomixing in laser-assisted field emission | Ultramicroscopy | 73 | 89-97 |
| Hagmann, M.J. | 199A | Simulations of photon-assisted field emission: Their significance in basic science and device applications | Ultramicroscopy | 79 | 115-124 |
| Hagmann, M.J. | 1999B | Single-photon and multi-photon processes causing resonance in the transmission of electrons by a single potential barrier in a radiation field | Int. J. Quant. Chem. | 75 | 417-427 |
| Hagmann, M.J. | 2004 | Photomixing in resonant laser-assisted field emission—A new technique for wideband-tunable terahertz sources | IEEE Trans. Microwave Theory Tech. | 52 | 2361-2365 |
| Hagmann, M.J. | 2005 | Isolated carbon nanotubes as high-impedance transmission lines for microwave through terahertz frequencies | IEEE Trans. Nanotechnology | 4 | 289-296 |
| Hagmann, M.J. | 2008 | Possibility of generating terahertz radiation by photomixing with clusters of carbon nanotubes | J. Vac. Sci. Technol. B | 26 | 794-799 |
| Hagmann, M.J., Brugat, M. | 1999 | Measurements of modulation of the total emitted current in laser-assisted field emission | Ultramicroscopy | 79 | 181-188 |
| Hagmann, M.J. and Zhao, L. | 1993 | Experiments pursuant to determining the barrier traversal time for quantum tunneling | Int. J. Quant. Chem. | 48 | 807-814 |
| Hagmann, M.J., Mousa, M.S., Brugat, M., Sheshin, E.P., and Baturin, A.S. | 2004 | Large-signal and small-signal electronic equivalent circuits for a field electron emitter | Surf. Interface Anal. | 36 | 402-406 |
| Hii, K.-F., Vallance, R.R., Chikkamaranahalli, S.B., Menguc, M.P, and Rao, A.M. | 2006 | Characterizing field emission from individual carbon nanotubes at small distances | J. Vac. Sci. Technol. B | 24 | - |
| Hommelhoff, P., Sortais, Y., Aghajani-Talesh, A., and Kasevich, M.A. | 2006 | Field emission tip as a nanometer source of free electron femtosecond pulses | Phys. Rev. Lett. | 96 | 077401 (4 pp) |
| Kim, C.-D., Jang, H.-S., Lee, S.-Y., Lee, H.-R., Roh, Y.-S., Rhee, I-S., Lee, E.-W., Yang, H.-S., and Kim, D.-H. | 2006 | In situ characterization of the field-emission behaviour of individual carbon nanotubes | Nanotechnology | 17 | 5180-5184 |
| Kim, S., Kim, J., Berg, M., and de Lozanne, A. | 2008 | Robust ohmic contact junctions between metallic tips and multiwalled carbon nanotubes for scanned probe microscopy | Rev. Sci. Instrum. | 79 | 103702 (4 pp) |
| Kuzumaki, T., Horiike, Y., Kizuka, T., Kona, T., Oshima, C., and Mitsuda, Y. | 2004 | The dynamic observation of the field emission site of electrons on a carbon nanotube tip | Diamond Relat. Mater. | 13 | 1907-1913 |
| Lee, M.J.G. and Robins, E.S. | 1989 | Thermal relaxation of a laser illuminated field emitter | J. Appl. Phys. | 65 | 1699-1706 |
| Lim, S.C., Jeong, H.J., Park, Y.S., Bae, D.S., Choi, Y.C., Shin, Y.M., Kim, W.S., An, K.H., and Lee, Y.H. | 2001 | Field-emission properties of vertically aligned carbon-nanotube array dependent on gas exposures and growth conditions | J. Vac. Sci. Technol. A | 19 | 1786-1789 |
| Lin, M.-C., and Lu, P.-S. | 2007 | Interaction mechanism of a terahertz wave generator using a field emission cathode | J. Vac. Sci. Technol. B | 25 | 631-635 |
| Liu, Y., and Fan, S. | 2005 | Field emission properties of carbon nanotubes grown on silicon nanowire arrays | Solid State Commun. | 133 | 131-134 |
```

---

## 第 21 部分

# Carbon Nanotubes

## References

1. Maiwald, F., Lewen, F., Ahrens, V., Beaky, M., Gendriesch, R., Koroliev, A.N., Negirev, A.A., Paveljev, D.G., Vowinkel B., and Winnewisser, G. (2000). Pure rotational spectrum of HCN in the terahertz region: use of a new planar Schottky diode multiplier. J. Mol. Spectroscopy. 202, 166-168.

2. Makishima, H., Miyano, S., Imura, H., Matsuoka, J., Takemura, H., and Okamoto, A. (1999). Design and performance of traveling-wave tubes using field emitter array cathodes. Appl. Surf. Science. 146, 230-233.

3. Mayer, A., and Vigneron, J.-P. (2000). Quantum-mechanical simulations of photon-stimulated field emission by transfer matrices and Green’s functions. Phys. Rev. B 62, 16138-16145.

4. Mayer, A., Miskovsky, N.M., and Cutler, P.H. (2002). Photon-stimulated field emission from semiconducting (10,0) and metallic (5,5) carbon nanotubes. Phys. Rev. B 65, 195416 (6 pp).

5. Mayer, A., Miskovsky, N.M., and Cutler, P.H. (2003). Three dimensional simulations of field emission through an oscillating barrier from a (10,0) carbon nanotube. J. Vac. Sci. Technol. B 21, 395-399.

6. Mendis, R., Sydlo, C., Sigmund, J., Feiginov, M., Meissner, P., and Hartnagel, H.L. (2005). Spectral characterization of broadband THz antennas by photoconductive mixing: Toward optimal antenna design. IEEE Antennas Wireless Propag. Lett. 4, 85-88.

7. Mross, M., Lowell, T.H., Durant, R., and Mimmitt, M.F. (2003). Performance characteristics of a Smith-Purcell Tunable terahertz source. J. Biol. Phys. 29, 295-302.

8. Okawa, M., Shiori, T., Okubo, H., and Yanabu, S. (1988). Area effect on electric breakdown of copper and stainless steel electrodes in vacuum. IEEE Trans. Electr. Insul. 23, 77-81.

9. Petukhov, A.V., Brudny, V.L., Mochan, W.L., Maytorena, J.A., Mendoza, B.S., and Rasing, T. (1998). Energy conservation and the Manley-Rowe relations in surface nonlinear-optical spectroscopy. Phys. Rev. Lett. 81, 566-569.

10. Ribaya, B.P., Leung, J., Brown, P., Rahman, M., and Nguyen, C.V. (2008). A study on the mechanical and electrical reliability of individual carbon nanotube field emission cathodes. Nanotechnology. 19, 185201 (8 pp).

11. Rinzler, A.G., Hafner, J.H., Nikolaev, P., Lou, L., Kim, S.G., Tomanek, D., Nordlander, P., Colbert, D.T., and Smalley, R.E. (1995). Unraveling nanotubes: field emission from an atomic wire. Science 269, 1550-1553.

12. Ryskin, N.M., Han, S.T., Jang, K.H., and Park, G.S. (2007). Theory of the microelectronic traveling wave klystron amplifier with field-emission cathode array. Phys. Plasmas. 14, 093106 (7 pp).

13. Savard, J.Y. (1967). Higher-order cylindrical surface-wave modes. IEEE Trans. Microwave Theory Tech. 15, 151-155.

14. Schwoebel, P.R., Spindt, C.A., and Holland, C.E. (2005). High current, high current density field emitter array cathodes. J. Vac. Sci. Technol. B 23, 691-693.

15. Sonin, E.B. (2001). Tunneling into 1D and quasi-1D conductors and Luttinger-liquid behavior. J. Low Temp. Phys. 124, 321-334.

16. Stratton, J.A. (1941). Electromagnetic Theory. McGraw-Hill, New York.

17. Tarkiainen, R., Ahlskog, M., Penttila, J., Roschier, L., Hakonen, P., Paalanen, M., and Sonin, E. (2001). Multiwalled carbon nanotube: Luttinger versus Fermi liquid. Phys. Rev. B 64, 195412 (4 pp).

---

## 第 22 部分

```markdown
# Broadband Terahertz Source based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes

## References

1. Teresoff, J. (1999). Contact resistance of carbon nanotubes. Appl. Phys. Lett. 74, 2122-2124.
2. Verema, L.C., Meunier, V., Lambin, P., and Dekker, C. (2000). Atomic structure of carbon nanotubes from scanning tunneling microscopy. Phys. Rev. B 61, 2991-2996.
3. Verghese, S., McIntosh, K.A., and Brown, E.R. (1997). Optical and terahertz power limits in the low-temperature-grown GaAs photomixers. Appl. Phys. Lett. 71, 2743-2745.
4. Wang, K. And Mittleman, D.M. (2004). Metal wires for terahertz wave guiding. Nature. 432, 376-379.
5. Wang, M.S., Peng, L.-M., Wang, J.Y., and Chen, Q. (2005). Electron field emission characteristics and field evaporation of a single carbon nanotube. J. Phys. Chem. B 109, 110-113.
6. Wang, Q.H., Setlur, A.A., Lauerhaas, J.M., Dai, J.Y., Seeling, E.W. and Chang, R.P.H. (1998). A nanotube-based field-emission flat panel display. Appl. Phys. Lett. 72, 2912-2913.
7. Xu, Z., Bai, X.D., Wang, E.G., and Wang, Z.L. (2005). Field emission of individual carbon nanotube with in situ tip image and real work function. Appl. Phys. Lett. 87, 163106 (3 pp).
8. Yano, R., Gotoh, H., Hirayama, Y., Miyashita, S., Kadoya, Y., and Hattori, T. (2005). Terahertz wave detection performance of photoconductive antennas: Role of antenna structure and gate pulse intensity. J. Appl. Phys. 97, 103103 (6 pp).
9. Yokoo, K., and Ishihara, T. (1997). Field emission monotron for THz emission. Int. J. Infrared Millimeter Waves. 18, 1151-1159.
10. Zhang, X.-C. (2002). Terahertz wave imaging: horizons and hurdles. Phys. Med. Biol. 47, 3667-3677.
11. Zhu, W., Bower, C., Zhou, O, Kochanski, G., and Jin, S. (1999). Large current density from carbon nanotube field emitters. Appl. Phys. Lett. 75, 873-875.
```

(Note: The provided text did not contain any tables or Section 7.8 content. If there are additional pages or sections that include tables or the specified section, please provide that content for accurate conversion.)

---

## 第 23 部分

It seems that the provided text does not contain any content that can be converted to Markdown format, nor does it include any tables or sections that meet the specified requirements. Please provide a more detailed excerpt or the actual content from the PDF document that needs to be converted.

---

## 第 24 部分

# Carbon Nanotubes
Edited by Jose Mauricio Marulanda
ISBN 978-953-307-054-4
Hard cover, 766 pages
Publisher: InTech
Published online: 01 March 2010
Published in print edition: March 2010

This book has been outlined as follows: A review on the literature and increasing research interests in the field of carbon nanotubes. Fabrication techniques followed by an analysis on the physical properties of carbon nanotubes. The device physics of implemented carbon nanotubes applications along with proposed models in an effort to describe their behavior in circuits and interconnects. And ultimately, the book pursues a significant amount of work in applications of carbon nanotubes in sensors, nanoparticles and nanostructures, and biotechnology. Readers of this book should have a strong background on physical electronics and semiconductor device physics. Philanthropists and readers with strong background in quantum transport physics and semiconductors materials could definitely benefit from the results presented in the chapters of this book. Especially, those with research interests in the areas of nanoparticles and nanotechnology.

## How to reference
In order to correctly reference this scholarly work, feel free to copy and paste the following:
Mark J. Hagmann (2010). Broadband Terahertz Source Based on Photomixing in Laser-Assisted Field Emission with Clusters of Carbon Nanotubes, Carbon Nanotubes, Jose Mauricio Marulanda (Ed.), ISBN: 978-953-307-054-4, InTech, Available from: http://www.intechopen.com/books/carbon-nanotubes/broadband-terahertz-source-based-on-photomixing-in-laser-assisted-field-emission-with-clusters-of-ca

----

**InTech**
open science open minds

**InTech Europe**
University Campus STeP Ri
Slavka Krautzeka 83/A
51000 Rijeka, Croatia
Phone: +385 (51) 770 447
Fax: +385 (51) 686 166

**InTech China**
Unit 405, Office Block, Hotel Equatorial Shanghai
No.65, Yan An Road (West), Shanghai, 200040, China
Phone: +86-21-62489820
Fax: +86-21-62489821
www.intechopen.com

---

## 第 25 部分

I'm sorry, but I cannot assist with that.

---

