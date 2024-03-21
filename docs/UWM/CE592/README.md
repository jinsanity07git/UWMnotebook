---

typora-copy-images-to: ipic
---





* multiple choices

* concepts 

  * keywords

* computations

  * 4 or 5 problem
    * mode choice
    * assignment 
      * All or nothong
      * equilibrium 
      * dynamic assignment 
    * TIA
      * Trip breaks
      * trip distribution
    * data management 
      * Sampling 
    * 

* Questions for guraduate students (bonus)




production and attraction

* defined by land use
* predicting numbers of  trip based on land characteristic (vs OD)





# Data management

[L5_pdf](../../CIV%20590%20UTP/content/Lecture%20Notes/L5-Data%20Management.pdf) 

SAMPLE SIZE 

CENTRAL LIMITTHEOREM

* $\overline { X } \sim N \left( \mu , \frac { \sigma ^ { 2 } } { n } \right)   
  where \ \overline { X } = \frac { \sum x _ { i } } { n } \\( Z = \frac { \overline { X } - \mu } { \frac { \sigma } { \sqrt { n } } } \rightarrow N ( 0,1 )$  
*  
* $p \left( \overline { X } - Z _ { 1 - \alpha / 2 } \sigma / \sqrt { n } \leq \mu \leq \overline { X } + Z _ { 1 - \alpha / 2 } \sigma / \sqrt { n } \right) = 1 - \alpha$ 

# Trip generation

* scope
  * how long
  * how large
* decision
  * 1. Time (temporal) decisions (departure time and duration) 2. Destination decisions 3. Modal decisions 4. Route (spatial) decisions 

### TRAVEL FORECASTING MODELS 

BASIC ASSUMPTIONS FOR MODELING 

*  observable variables.
* explicit functional relationship 
* “explain” only in a statistical, correlative sense. [^1]
* identical for all individuals and constant over time.   

MODEL DEVELOPMENT PROCESS 

1. Specification   y=f(X) 

2. Estimation   y=aX+b; a=1, b=2 3

3. Implementation   If Z > W, then y=aX+b 

4. Validation   ypredicted2015+k=yobserved2015 

5. Forecasting  y2020= ypredicted2020+k 


THE URBAN TRANSPORTATION MODELING SYSTEM (**<u>UTMS</u>**)- FOUR-STEP 

![1537911287854](C:\Users\zihao\AppData\Roaming\Typora\typora-user-images\1537911287854.png)

* pros: pragmatic; analytically; simple techniques; reasonable amount of data. 
* cons: aggregate; not necessarily represent individual trip making behavior.





home_based 

* household 
* vehicle ownership
* social economic 

work_based

* employee number/policy
* parking space
* roofed space

Shop-based: Ts = f (number of retail workers, type of retail, square foot, location, competition) 





TRIP GENERATION METHODS 

1. Growth-factor Models 

2.  Regression Models 

3.  Category Analysis 


 Regression Models 

* HOUSEHOLD-BASED REGRESSION 
* ZONE-BASED REGRESSION 





### Regression Models 

file > add-in > analysis tool pack > data analysis 

* [Excel Regression Analysis Output Explained - Statistics How To](http://www.statisticshowto.com/excel-regression-analysis-output-explained/)  
* [How to Interpret Regression Analysis Results: P-values and Coefficients](http://blog.minitab.com/blog/adventures-in-statistics-2/how-to-interpret-regression-analysis-results-p-values-and-coefficients) 
* [Multiple Regression Analysis Excel | Real Statistics Using Excel](http://www.real-statistics.com/multiple-regression/multiple-regression-analysis/multiple-regression-analysis-excel/) 
* [Basic Statistics in Python: Probability](https://www.dataquest.io/blog/basic-statistics-in-python-probability/) 



(WEEK 5) 

[Detailed New National Maps Show How Neighborhoods Shape Children for Life](https://www.nytimes.com/2018/10/01/upshot/maps-neighborhoods-shape-child-poverty.html) 

* CAUTIONS OF REGRESSION MODELS
  * Correlation among explanatory variables (particularly income and auto ownership) may create estimation problem. 
  * The assumption that the explanatory variables have linear, and additive impacts on trip generation may be wrong. 
  *  “Best fit” equations may yield counterintuitive results 
  *  A high R2 (Coefficient of determination) by itself means little <u>if the t-test is marginal or poor,</u>  
  *  Choose only the independent variable that have highest correlation with the **dependent variable** and low correlation among the **independent variables**. 
  *  Check the coefficients are **logical** or not. Trip generation is never “negative” in reality no matter what value the independent variable has.

ZONE-BASED REGRESSION Zonal Total or Zonal Average? 

* Zonal Total
*  Zonal Average 
* CONCLUSIONS 
  *  The difference between zone totals and zonal average lies in the **error-term distribution** in each case.  It is obvious that the constant variance condition of the model CANNOT hold in both cases, unless $H_i$ was constant for all zones i. So, which one is better?  
  *  **Zonal average may be better** because normalizing zones by size reduces **heteroscedasticity**(the variance of the error term is not a constant); also, variables are independent of size, reducing the risk of **multicollinearity**(multiple independent variables are correlated with each other). 
  *  But, by using zonal average, important socioeconomic variations within the zone may be obscured or may yield **spurious results**. (internal variation in zone VS household) 



###  Category Analysis



(CROSS-CLASSIFICATION ANALYSIS)

It is exclusively used as **disaggregate** models. 

* Advantages: 
  * 1 – grouping are **independent of the zone systems** 
  * 2 –**no prior assumptions** about the relationship are required 
  * 3 – relationships can be different for each group (effect of x1 can be different for group a or b)
  *  4 –group the HH by their characteristics and **minimize standard deviation within the class**. 
*  Disadvantages: 
  * 1 – we can’t really infer relationships outside of the range 
  * 2 –no goodness-of-fit   (no comparison )
  * 3 – need lots of data (enough to produce a reliable sample size in each group) 
  * 4 –grouping is done by **trial and error**, more than a structured method.



FHWA----SIMPLIFIEDTRIPPRODUCTION PROCEDURE[^2]  



### Growth-factor Models

least useful ; least accurate 

![1538516471917](C:\Users\zihao\AppData\Roaming\Typora\typora-user-images\1538516471917.png) 



growth factor methods are only used in practice to predict the future number of external trips to an area; 

* because they are not too many in the first place
*  and also because there are no simple ways to predict them



TRIP ATTRACTION

* Trip attraction rates can be made by analyzing the urban activities that attract trips. 
* Trips are attracted to various locations, depending on the character of, location, and amount of activities taking place in a zone. 
* Three trip generation methods are used for this end too, but obviously types of independent variables used are different.

CONTROL TOTAL 



![1538517424698](C:\Users\zihao\AppData\Roaming\Typora\typora-user-images\1538517424698.png)



# Trip distribution

BASICASSUMPTIONSOFTRIP DISTRIBUTION

1. Number of trips decrease with “travel costs” between zones 
2.  Number of trips increase with zone “attractiveness” 
3.  Number of trips increase with zone “productivity”

METHODS OFTRIP DISTRIBUTION

### I. **Growth Factor Models** 

* Uniform 

  * single factor

* Singly-Constrained 

  * row factor	

* Doubly-Constrained 

  * “Balancing factors Ai and Bj” (Furness 1965)
  * A- row factor ; B - column factor
  * stop criterion/rule -- error percentage <= ...
  * **converge** is not guaranteed  

* Average Factor 

  * trip table 
  * growth factor table ---averaging growth factors
  * stop criterion/rule -- growth factor  ~= 1.

* Fratar Method  

  * $ T_{ij} (k+1) = \frac{T_{ij}(k)\tau_j}{\sum T_{ij}(k)\tau_j}P_i (T) $   

    * $\tau_j$ growth factor

  * averaging number of trips ---  force $T_{ij} = T_{ji}$  


GROWTH FACTOR LIMITATIONS

* Assuming that trips grow at a standard uniform rate is a **fundamentally flawed concept** 
* The method is heavily dependent on **the accuracy of the base-yea**r trip matrix. 
* Cannot handle **new zone(s)** which is available in the base year. 
* It does not account for changes in **transportation costs** due to improvements.

### II. Gravity Model

CONSTRUCTINGAGRAVITY MODEL

$T_{ij} = P_i A_j f(C_{ij})a_i b _j$ 

* coefficient: a b
* friction: $f()$ 
* $\sum_{i}  T_{ij} = A_j$   

SIMPLE GRAVITY MODEL

* The simple gravity model set $b_j $to be 1.0
* `relative attractiveness`  instead of `# of attraction ` 

DOUBLY CONSTRAINTGRAVITY MODEL 

* iteratively for ai (row total) and bj (column total) 




calibration of the gravity model

* determination of cost c
* Keep in mind that the socioeconomic factor, K, 
  can be a matrix of values rather than just one  

Limitation of GM

* Too much of a reliance on K-Factors in calibration 
* The skim table impedance factors are often too simplistic to be realistic 
  *  Typically based solely upon vehicle travel times 
  *  At most, this might include tolls and parking costs
  *  Almost always fails to take into account how things such as good transit and walkable neighborhoods affect trip distribution 
  *  No obvious connection to behavioral decision-making



# Mode Choice

[L9Mode splitt.pdf ](../../CIV 590 UTP/content/Lecture Notes/L8-Mode%20Split.pdf)   

AVAILABLE MODES

FACTORS AFFECTING MODECHOICE 

* TRAVELER SPECIFIC
  * • Car availability and /or ownership 
  * • Possession of a driving license 
  * • Household structure (single, married, married with kids, retired, etc) 
  * • Income 
  * • Residential density
* MODE-SPECIFIC 
  * Firstly, quantitative factors are: 
    * • Travel time: in-vehicle travel time (IVTT), OVTT including connection/transfer, walking and waiting time, 
    * • Minimum cost: out of pocket total expense (OPTC) 
    * • Availability and cost of parking • Availability of public transit (route, schedule, frequency, park-and-ride, etc.) 
  * Secondly, qualitative factors are: 
    * • Comfort and convenience 
    * • Reliability and regularity 
    * • Protection and security
* TRIP SPECIFIC
  Characteristics of the journey 
  * • **Trip purpose** 
  * • Time of day 
  * • **Departure time** 



MODEL CHOICE/MODE SPLIT MODEL 

UTILITY AND UTILITY FUNCTIONS 

* MAKINGCHOICE (DETERMINISTIC)

## BINARY PROBIT MODELS 

> “Probit” name comes from Probability Unit 

* better to use when choices are corelated 

* MAKINGCHOICES (PROBABILISTIC)
  * RANDOMUTILITY FUNCTION 
    * Random un-specificable error 

    * BINARY PROBIT MODELS

      ![1539293960111](C:\Users\zihao\AppData\Roaming\Typora\typora-user-images\1539293960111.png)



$ \begin{array} { l } { P _ { i } ( 1 ) = P \left( U _ { 1 } > U _ { 2 } \right) } \\ { = P \left( \beta _ { 1 } \mathbf { X } _ { i 1 } + \varepsilon _ { i 1 } \geq \beta _ { 2 } \mathbf { X } _ { i 2 } + \varepsilon _ { i 2 } \right) } \end{array}$ 

$\begin{array} { l } { = P \left( \beta _ { 1 } \mathbf { X } _ { i 1 } - \beta _ { 2 } \mathbf { X } _ { i 2 } \geq \varepsilon _ { i 2 } - \varepsilon _ { i 1 } \right) } \\ { = P \left( \varepsilon _ { i 2 } - \varepsilon _ { i 1 } \leq \beta _ { 1 } \mathbf { X } _ { i 1 } - \beta _ { 2 } \mathbf { X } _ { i 2 } \right) } \end{array} $      

$\begin{array} { l } { \varepsilon _ { i 1 } \sim N \left( 0 , \sigma _ { 1 } ^ { 2 } \right) } \\
 { \varepsilon _ { i 2 } \sim N \left( 0 , \sigma _ { 2 } ^ { 2 } \right) } 
\\ { \varepsilon _ { i } \sim N \left( 0 , \sigma ^ { 2 } \right) \quad \text      
 { where } : \sigma = \sqrt { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } - 2 \sigma _ { 12 } } } 
\\ { f \left( \varepsilon _ { i } \right) = \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } \left( \frac { \varepsilon _ { i } } { \sigma } \right) ^ { 2 } } } \end{array} $   

The probability for observation i to choose 1 is $P_i (1)$ :

$ P _ { i } ( 1 ) = \Phi \left( \frac { \beta _ { 1 } \mathbf { X } _ { \mathrm { il } } - \beta _ { 2 } \mathbf { X } _ { \mathrm { i2 } } } { \sqrt { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } - 2 \sigma _ { 12 } } } \right) = \Phi ( z ) $  

* Where $\Phi (.) $ is the standardized cumulative normal distribution 




## MULTINOMIAL LOGIT (MNL) MODEL

* error distributional **assumption** of **Gumbel Distribution** (type I extreme value) [^3]  

![1539294429473](C:\Users\zihao\AppData\Roaming\Typora\typora-user-images\1539294429473.png)  

$ P _ { i m } = p r o b \left( V _ { i n } + \varepsilon _ { i m } \geq 
\text{ max utility among the rest outcomes  } \right ) $ 

$\begin{aligned} P _ { i n } & = \operatorname { prob } \left( V _ { i m } + \varepsilon _ { i n } \geq M _ { i s } + \varepsilon _ { i s } \right) \\ & \text { where } M _ { i s } + \varepsilon _ { i s } = \operatorname { Max } \left( B _ { i s } + \varepsilon _ { i s } , \forall S \neq m \right) \end{aligned}$  

$P _ { i m } = \frac { e ^ { V _ { i n } } } { \sum _ { s } e ^ { V _ { i s } } } = \frac { e ^ { \beta _ { m } \mathbf { X } _ { i m } } } { \sum _ { s } e ^ { \beta _ { s } X _ { i s } } }$ 

* case:

  * BINOMIAL LOGIT MODEL 
    (Auto and Transit)

  $P ( A ) = \frac { e ^ { V _ { A } } } { e ^ { V _ { A } } + e ^ { V _ { T } } } = \frac { 1 } { 1 + e ^ { \left( V _ { T } - V _ { A } \right) } }$ 

* Limitation

  * INDEPENDENCE OF IRRELEVANTALTERNATIVES (IIA) 

* INDEPENDENCE OF IRRELEVANTALTERNATIVES (IIA)



## NESTED LOGIT MODEL

When the MNL assumption is violated, switch to a nested model.



MODEL

* Primary Level 
* Nested Level 
* WHAT ISTHETA Θ
  *  A value between 0 and 1 
    * Θ=1 implies that there exists an equivalent MNL model 



# Traffic Assignment

[TSP problem](../01develop/TSP.md) [^4] 

[L10-Traffic Assignment.pdf ](../../CIV 590 UTP/content/Lecture Notes/L10-Traffic%20Assignment.pdf)   



To assign a trip to a specific route, you need: 

1. Number of trips between pairs of zones 
2. Available highway or transit routes 
3. Travel costs (time, monetary cost)
4. A decision rule (algorithm) for selecting a route



Three classes

1. Shortest path (All or nothing)

2. Equilibrium assignment\

   a. (Deterministic) User Equilibrium (DUE)

   b. System Optimal or Social Equilibrium 

3. Dynamic traffic assignment



CAPACITY RESTRAINT 

*  BPR models
   ( Highway (link) performance function,
    volume-delay function)
  * The relationship between **route travel time** and **traffic flow** 
  *  Features 
        * Travel time is no longer static, it is affected by the traffic on route. 
        *  The dynamic travel time leads to a dynamic traffic assignment



## Shortest path

ALL-OR-NOTHING (AON)

• Assume NO CONGESTION effects. 

• Assume all drivers consider the same attributes for route choices and they perceive and weigh them in the same way. 

• Implications: 

​	• Link costs are fixed 

​	• Every driver from i to j choose the same route. 

• Application: in **sparse** and **uncongested** network where they are few alternative routes and they are very different in cost.

[ Dijkstar](../../CIV 590 UTP/content/Lecture Notes/Dijkstar.pdf)   doc

* [Dijkstra Visualzation](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html) (table)
* [VisuAlgo - Single-Source Shortest Paths](https://visualgo.net/en/sssp) 





## Equilibrium assignment

### User Equilibrium 





* The rule of choice underlying user equilibrium is that travelers will select a route so as to minimize their PERSONAL travel time between the OD. 
* Assumptions 
  *  Travelers will select routes between OD on the basis of **route travel times** only. 
  * Travelers **know the travel times** that would be encountered on all available routes between their ODs.\]

>  **Wardrop first principle:** “the travel time between a specified OD on all used routes is the same and is less than or equal to the travel time that would be experienced by a traveler on any unused route”. (Wardrop 1952)  

* Application: 
  * congested assignment

![1540503452399](..\image\1540503452399.png) 



UE MATHEMATICAL PROGRAMMING APPROACH

* Sheffi 1985$

| $\begin{array} { c } { \min S ( x ) = \sum _ { n } \int _ { 0 } ^ { x _ { n } } t _ { n } ( w ) d w } \\ { \quad \left\{ \begin{array} { l } { x _ { n } \geq 0 } \\ { q = \sum _ { n } x _ { n } } \end{array} \right. } \end{array}$ | $\begin{array} { c } { \min S ( x ) = \sum _ { n } \int _ { 0 } ^ { v _ { i } } t _ { n } ( v_i ) d v } \\ { \quad \left\{ \begin{array} { l } { v _ { i } \geq 0 } \\ { q = \sum _ { n } v _ { i } } \end{array} \right. } \end{array} $ |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Notation: 

* n: a specific route, and 
* $t_n(w)$: performance function corresponding to route n 
* $w$ denotes flow  =  $x_n$  =  $v_i$ :  in n_th route 



### SYSTEM OPTIMIZATION (SO) 

OR SOCIAL EQUILIBRIUM (SE)

* Definition:
  *  a solution that minimize the number of total vehicle hours of travel for some specified OD traffic flow (from the entire system perspective)

> ^| **Wardrop second principle:** “Under social equilibrium conditions traffic should be arranged in congested networks in such a way that the average (or total) travel cost is minimised”, (Wardrop 1952)
>

* SE MATHEMATICAL PROGRAMMING APPROACH 

$\begin{array} { l } { \min S ( x ) = \sum _ { n } x _ { n } t _ { n } \left( x _ { n } \right) } \\ { \left\{ \begin{array} { l } { x _ { n } \geq 0 } \\ { q = \sum _ { n } x _ { n } } \end{array} \right. } \end{array}$ 




* principle of **anarchy** 



* BRAESS’S PARADOX 



### Solving UE:

 HEURISTIC EQUILIBRATIONTECHNIQUES

* Network Loading 

  * The process of assigning O-D entries to the network for specific link travel times. 
  * The process follows the route-choice criterion, which underlies any traffic assignment model. 

* Three Loading Methods 

  *  **Capacity restraint** 

    * Repeated use of all-or-nothing assignment in which the travel times from the previous assignment are used in the current iteration.   
    * Comment: Bad algorithm; only works for a congested network

  * **Incremental** 

    * The modeler divides the total trip matrix T into a number of fractional matrices by applying a set of proportional factors $p_{n}$ 
    * Comment: converge  depends on choice of  proportional factors $p_{n}$ 

  *  **Method of successive average (MSA)**

    *  an improved Capacity Restraint UE Loading 
    * $V _ { a } ^ { n } = ( 1 - \phi ) V _ { a } ^ { n - 1 } + \phi F _ { a }$ 
      * Weighted sum of  `volume of last iteration ` Va and  `auxiliary flow` Fa
        *  Load the whole of the matrix T **all-or-nothing** to these trees obtaining a set of **auxiliary flow Fa.**  
      * A better way is to make weight 𝜙=1/n where n is the nth iteration
    * Comment:   small route sets; 

  * **Frank Wolfe Algorithm** 

    [Frank–Wolfe algorithm - Wikipedia](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm) 

    * similar to MSA

      $V _ { a } ^ { n } = ( 1 - \phi ) V _ { a } ^ { n - 1 } + \phi F _ { a }$ 

    * determine $\phi$ 

      * choose $\phi$ such that the value of obj. function is minimized 
      * partial differential equation / gradient

    *  



## Dynamic Traffic Assignment  (time-dependent)











# Urban activity system analysis

[L11.pdf ](../../CIV 590 UTP/content/Lecture Notes/L11-Urban%20Activity%20Analysis.pdf)   

* urban planning theories
* personal accessibility
* land-use models 

## urban planning theories 

*  “urban activity system” or “urban land use”
* A major factor linking the demand and supply of the real estate market is the `price` 
* Urban form
  * Conventional grid
  * Curvilinear loop pattern 
  * Cul-de-Sac Pattern[^5]  
* Urban interaction
* Urban spatial structure : build environment 

> Figure 1   P7



## Accessibility

* ATTRACTIVENESS AND ACCESSIBILITY 
* model

## Land-use models 

1. Scenarios  (whtat-if )

   * pros
   * cons

2. Heuristic Models: Lowry-Type Model (1960) 

   > [RAND Corporation - Wikipedia](https://en.wikipedia.org/wiki/RAND_Corporation) 

   - pros
   - cons

3.  Operational Models or integrated urban models: ITLUP (Integrated Transportation and Land-Use Package) (1983) 

   * aggregated model 

4.  Simulation Models: UrbanSim (1998) 

   * household based (agent)
   * types
     * accounting model
     * probabilistic models
     * regression model

5. Activity-based Model (1990) 













#  Site impact study

/TIA Introduction of TIA.pdf







\TIA Trip Distribution Modes Assignment.pdf 





* TIA Scales
   According to the size of the development, any development that generates ≥100 peak hour trips should be required to prepare a TIA. 
  * Why 100+ peak hour trips? 
* ACCESS LOCATION AND DESIGN REVIEW
  * 



# Site Trip Generation



[STG.pdf](../../CIV 590 UTP/content/Lecture Notes/   TIA%20Site%20Trip%20Generation.pdf)  



* TRIP DEFINITIONS
  * Primary 
  * Pass-by
  * Diverted
  * Internal

TRIP GENERATION RATES

* 



[STDis & assign.pdf](../../CIV 590 UTP/content/Lecture Notes/TIA%20Trip%20Distribution%20Modes%20Assignment.pdf)   

 

# Taffic impact analysis 








# Expression 

precondition; given condition ; run into an error 

often times; afterwards

as you can tell ; relatively straightforward 

collective wisdom 



[^1]: http://www.tylervigen.com/spurious-correlations 

[^2]: [Trip Generation - Civil IITB](http://www.civil.iitb.ac.in/~gpatil/utsp_vlab/tripgeneration.php) 
[^3]: [Gumbel distribution - Wikipedia](https://en.wikipedia.org/wiki/Gumbel_distribution)

<iframe id="google_ads_iframe_/10518929/tmnp.howtogeek/article_details/a1-p1-s1_0" title="3rd party ad content" name="google_ads_iframe_/10518929/tmnp.howtogeek/article_details/a1-p1-s1_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" data-load-complete="true" data-integralas-id-de48ed7a-c147-cf35-b632-836b5f56d871="" style="box-sizing: inherit; max-width: 100%; border: 0px; vertical-align: bottom;"></iframe>



[^4]: [Use Links in Typora/Markdown](https://support.typora.io/Links/) 
[^5]: https://www.citylab.com/design/2011/09/street-grids/124/
[^6]: Cunard and Mahmassani - Traffic Flow Theory.pdf