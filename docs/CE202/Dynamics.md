

### Resources for Dynamics

[Dynamics and Dynamical Systems](https://def.fe.up.pt/dynamics/preface.html) 

[Dynamics and Vibrations: Notes: Equations of Motion for Particles](http://www.brown.edu/Departments/Engineering/Courses/En4/Notes/particles_eom/particles_eom.htm)  

[This is an online textbook for dynamics.](http://dynref.engr.illinois.edu/index.html)

* ARC LENGTH CALCULATOR FOR CURVE
* [Arc Length of a Curve](http://www.mathwords.com/a/arc_length_of_a_curve.htm) 

[HyperPhysics mind map](http://hyperphysics.phy-astr.gsu.edu/hbase/) 



 <div style="page-break-after: always;"></div>   

### Chapter 12, Sections 1-3

• Introduction [Week2: Exercise 1](CE202/lab/lab2_equations_presentation.md)

 Rectilinear Motion of Particles

* Average Velocity: $\vec { v } _ { \text {ave} } = \frac { \Delta \vec { x } } { \Delta t }$                 Velocity: $\vec { v } = \lim _ { \Delta t \rightarrow 0 } \frac { \Delta \vec { x } } { \Delta t } = \frac { d \vec { x } } { d t } = \dot { \overline { x } }$ 
* Average Acceleration:  $\vec { a } _ { a v e } = \frac { \Delta \vec { v } } { \Delta t }$        AccelerationL: $\vec { a } = \lim _ { \Delta t \rightarrow 0 } \frac { \Delta \vec { v } } { \Delta t } = \frac { d \vec { v } } { d t } = \dot { \vec { v } } = \frac { d ^ { 2 } \vec { x } } { d t ^ { 2 } } = \ddot { \vec { x } }$ 
* Other formulations: $a = \frac { d v } { d t } = v \frac { d v } { d x } \Rightarrow a d x = v d v$ 

* Choose which expression 
  * if $a = f ( t )$ then use $d v = a d t = f ( t ) d t$
    if $a = f ( x )$ then use $v d v = a d x = f ( x ) d x$ 
  * $\begin{aligned} \text { if } a = f ( v ) \text { then use } d t = a ^ { - 1 } d v & = [ f ( v ) ] ^ { - 1 } d v \\  & \text { or use } d x = a ^ { - 1 } v d v = [ f ( v ) ] ^ { - 1 } v d v \end{aligned}$   
* Constant or non-constant?
  * constant
     $v = a _ { c } t + v _ { 0 }$
    $x = \frac { 1 } { 2 } a _ { c } t ^ { 2 } + v _ { 0 } t + x _ { 0 }$
    $v = \sqrt { 2 a _ { c } \left( x - x _ { 0 } \right) + v _ { 0 } ^ { 2 } }$ 
  *  non-constant: 
    * definite integral or indefinite integral 
      $\int v ( t ) d t$<br/>$\int v ( x ) d x$
      $\int x ( t ) d t$ 
    * $\int a ( x ) d x$  
      $\int a ( v ) d v$   
      $\int a ( t ) d t$    



 <div style="page-break-after: always;"></div>   

### Chapter 12, Sections 4-6 

**General curvilinear motion** 

* Rectangular Components
  * position: $\vec { \mathbf { r } } = x \hat { \mathbf { i } } + y \hat { \mathbf { j } } + z \hat { \mathbf { k } }$ 
  * Velocity: $\vec { \mathbf { v } } = \frac { d \vec { \mathbf { r } } } { d t } = v _ { x } \hat { \mathbf { i } } + v _ { y } \hat { \mathbf { j } } + v _ { z } \hat { \mathbf { k } }$ 
    * $v _ { x } = \frac { d x } { d t } = \dot { x }$ ,etc
  * Acceleration: $\vec { \mathbf { a } } = \frac { d \vec { \mathbf { v } } } { d t } = a _ { x } \hat { \mathbf { i } } + a _ { y } \hat { \mathbf { j } } + a _ { z } \hat { \mathbf { k } }$ 
    * $a _ { x } = \frac { d v _ { x } } { d t } = \dot { v } _ { x } = \frac { d ^ { 2 } x } { d t ^ { 2 } } = \ddot { x } ,$ etc 

**Special case: Projectile motion  ** [Week3: Exercise 2](http://129.89.35.118/udata/project/1532522260233_user/dynamic%20animation/trim_Functions.html) 

Horizontal acceleration = 0

* Vertical acceleration = g In this class, that is $32.2 ft/s^2$ or $9.81 m/s$
* steps
  1. establish coordinate system
  2. identify knowns and unknowns
  3. identify equations that will produce desired unknowns from knowns.





 <div style="page-break-after: always;"></div>   

### Chapter 12, Sections 7-8

**Curvilinear** Motion

* Normal and tangential coordinates	
   * steps
     1. establish coordinate system
     2. identify knowns and unknowns
     3. identify equations that will produce desired unknowns from knowns.

   * equations

    *  $ \begin{aligned}
      ​       \vec{v} &= \dot{s} \, \hat{e}_t \\
      ​        \vec{a} &= \ddot{s} \, \hat{e}_t + \frac{\dot{s}^2}{\rho} \hat{e}_n  \\
      ​        \kappa = \frac{|x''y' - y''x'|}{(x'^2 + y'^2)^{3/2}} 
      ​  \end{aligned}$
      
    - ​	 $\begin{aligned}
      ​	       \vec{v} &= v \hat{u}_t \\
      ​	       \vec{a} &= \dot{v} \, \hat{u}_t + \frac{v^2}{\rho} \hat{u}_n 
      ​		\end{aligned}$ 
   
     * $\rho = \frac{(x'^2 + y'^2)^{3/2}} {|d^2y/dx^2|} $ 
   
*  Polar and cylindrical coordinates.   [Week4: Exercise 3](CE202/lab/lab4_equations_presentation.md) 

  * components	
    * Transverse coordinate[^1] , θ, measured **counter clockwise** from a fixed reference: the positive x-axis, for example.
    * Radial coordinate, r, measured from a **fixed origin.** 



* equations

   - ​    $\begin{aligned}
     ​              \vec{v} &= \dot{r} \, \hat{u}_r + r\dot{\theta}  \hat{u}_{\theta} + \dot{z} \hat{u}_z       \\
     ​              \vec{a} &= (\ddot{r} - r\dot{\theta}^2) \, \hat{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta}  )\hat{u}_{\theta} + \ddot{z} \hat{u}_z  
     ​              \end{aligned}$          
   - $tan(\psi) = \frac{r}{dr/d\theta}$  

    $\begin{aligned}
   ​              \vec{v} &= \dot{s} \, \hat{e}_t 
   ​              \\
   ​              \vec{a} &= \ddot{s} \, \hat{e}_t + \frac{\dot{s}^2}{\rho} \hat{e}_n
   ​              \end{aligned}$    or   $\begin{aligned}
   ​              \vec{v} &= v\ \hat{u}_t \\
   ​              \vec{a} &= \dot{v} \, \hat{u}_t + \frac{v^2}{\rho} \hat{u}_n
   ​\end{aligned}$    

###  Chapter 12, Sections 9-10  

* Absolute dependent motion analysis of two particles [Week5: Exercise 4](CE202/lab/lab5_equations_presentation.md)

  * steps

    1. **define variables** to keep track of parts of the system.
    2. express the **fixed length** of the rope in terms of the parts known and unknown:
    3. **differentiate** to find velocities (differentiate with time)
  * [Types of Pulleys and How do They Work? - Pulleys](https://8ypulleys.weebly.com/types-of-pulleys-and-how-do-they-work.html) 
    * fixed Pulley
    * movable pulley


* Relative motion analysis of two particles
  * steps
    1. Start with relative position
       * tip-to-tail technique:  $v_B = v_A + v_{B/A}  $  
    2. differentiate with respect to time ?
       *  to find relative velocity and relative acceleration:

* <img src="../CE202/Dynamics_img/image-20201019121114549.png"  style="zoom:50%;" />

[^1]: [Polar (Radial/Transverse) Coordinates](http://web.mst.edu/~reflori/be150/lessons/lesson_05/polar_coordinates.html) 



 <div style="page-break-after: always;"></div>   

### Chapter 13,Sections 1-6

* Newton’s Laws of
  * • Equations of motion for a system of particles
    *  in rectangular coordinates
    *  with normal and tangential coordinates
    *  with **polar coordinates** 
  * • Friction

* Equations of motion for a system of particles
  * steps
    1. Draw a Free Body Diagram
    2. Kinetics
    3. Kinematics 
    4. Combine and solve
  * equations
    * Newton’s 2nd Law of Motion  [Week7: Exercise 5](CE202/lab/lab7_equations_presentation.md) 
      * $\sum \vec{F} =  m\vec{a}  $   
    * Friction
      * $F_f = \mu N$    
      * Static fiction $\mu_s$ **$F_s ≤ μ_s N$** 
      * Kinetic friction $\mu_k$   
    * Rectilinear motion 
      *  Constant linear acceleration
          $\begin{aligned}               a &= a_0 = \text{constant} \\               v &= v_0 + a_0 t \\               x &= x_0 + v_0 t + \frac{1}{2} a_0 t^2               \end{aligned}$     
    * Circular motion
      * Circular motion (constant r ) 
        $\begin{aligned}               r &= \text{constant} \\               \vec{v} &= r \omega \,\hat{e}_\theta \\               \vec{a} &= - r \omega^2 \,\hat{e}_r + r \alpha \,\hat{e}_\theta               \end{aligned} $
      * Constant angular acceleration
        $\begin{aligned}               r &= r_0 = \text{constant} \\               \alpha &= \alpha_0 = \text{constant} \\               \omega &= \omega_0 + \alpha_0 t \\               \theta &= \theta_0 + \omega_0 t + \frac{1}{2} \alpha_0 t^2               \end{aligned}$
    * Curvilinear Motion 
  * simple pendulum            
    * FBD
    * Used path coordinates.
    * Could have just as well used polar. 

![simple pendulum](Dynamics_img/image-20201024191222973.png)



* Polar Coordinates
  * $tan\psi = \frac{r d\theta} {dr} =\frac{r} {dr/d\theta}  $ 
  
  *  ![TN in polar](Dynamics_img/image-20201019114524207.png)
  
     

 <div style="page-break-after: always;"></div>   



### Chapter 14 Sections 1-6

Work, Energy, Power, and Efficiency  

* Work of a force  [Week9: Exercise 6](CE202/lab/lab9_equations_presentation.md)
  * $U_{1-2} = \int_{\vec{r}_1}^{\vec{r}_2} \vec{F} \cdot d\vec{r} $ 
    * constant force : $U_{1-2} = F_c cos\theta(s_2 -s_1) $  
    * gravitational force (weight) : path independence : $-mgh $
    * work of a spring  :  $U_{1-2} = \int_{\vec{r}_1}^{\vec{r}_2} \vec{F_s} \cdot d\vec{r} = \int_{s_1}^{s_2} ks ds =  \frac{1}{2} k(s_2^2-s_1^2) $    

* Kinetic energy
  *  a point mass:
      $ T = \frac{1}{2} m v^2 $ 

* Relate work and energy
  * steps
    1. Start with $\sum \vec{F_t} =  m\vec{a_t}  $ 
    2. Recall that  $a_t = vdv/ds$  => $\sum \vec{F_t} =  mv dv/ds  $  
    3. Separate variables and integrate  $\int \vec{F_t} ds = 1/2m(v_2^2 -v_1^2) $ 
    4. Recognize the definition of work on the left: $U_{1-2} = 1/2m(v_2^2 -v_1^2) $   
    5. Rewrite as $\sum U_{1-2} = T_2 -T_1$  ;
    6. Principle of Work and Energy :  $T_1 +\sum U_{1-2} = T_2 $  

* Power and mechanical efficiency

  * $e = output \ power / input \ power$   

* Conservative Force

  * path independent

    * Gravity; Spring; Electric; Magnetic

  * non-conservative forces 

    * Friction and drag

      Non-elastic material stress (deformation)

* Potential Energy
  *  relative to a datum,
    * ground level : $V_g = mgh$
    * rest / unstretched length : $V_e = mgh$  

* Conservation of Energy
  * Valid only when all forces conservative
  * For a system of particles
    * $\sum T_1 + \sum V_2 = \sum T_2 + \sum V_2 $  
  * $\begin{aligned}               E &= T + V \\               \text{total energy} &= \text{kinetic energy} + \text{potential energy}               \end{aligned} $   



<div style="page-break-after: always;"></div> 

### Chapter 15 Sections 1-4

Topics

• Linear Impulse and Momentum

• Conservation of Linear Momentum

• Central and Oblique impact



*  **Principle of Linear Impulse and Momentum:**    [Week11: Exercise 7](CE202/lab/lab10_equations_presentation.md)

  * $m\vec{v_1} + \int_{\vec{t}_1}^{\vec{t}_2} \vec{F} \cdot dt  = m\vec{v_2} $ 
  * If it is inconvenient to integrate vectors, you can dot with unit vectors to produce scalar equations:
  * **Linear Momentum**
    * $\vec{L} =m\vec{v}$ 
    * Units of mass-velocity: kg·m/s and slug·ft/s. 
  * **Linear Impulse**
    * $\vec{I} = \int \vec{F} dt$
    * Units of force-time: N·s and lb·s.
  * **On a system of particles:** 
    * $m(\vec{v_G})_1 + \sum \int_{\vec{t}_1}^{\vec{t}_2} \vec{F_i} \cdot dt  = m(\vec{v_G})_2 $    
    *   Only external forces
    * G: center of mass

* **Conservation of Linear Momentum**

  *  “If the time period over which the **motion** is studied is very short, some of the **external impulses** may be **neglected** or considered approximately equal to zero.”
    * The **forces** causing negligible impulses are called **nonimpulsive forces**.
    *  The **forces** which act for a very short period of time and are large enough to produce a significant change in momentum are called **impulsive forces.**  
  * $m\vec{v_1}  = m\vec{v_2} $ 

* **Impacts:**

  *  Direction of motion of each particle  with **line of impact**: 	 

    * **Central Impact**  : noncollinear

      * Deformation impulse  $\int \vec{P} dt$ 

      * Restitution impulse: $\int \vec{R} dt$  

      * coefficient of restitution
        $ e = \int \vec{R} dt/ \int \vec{P} dt $
        $ e= =\frac{ [(v_B)_2 - (v_A)_2]}{[(v_A)_1 - (v_B)_1]}$  

        * Elastic impact: e = 1
        * Plastic impact:  e = 0

        ​	

    * **Oblique Impact**: nonnoncollinear

      * linear momentum of the entire system  is conserved along the line of impact:
      *  **Line of impact** ( X-axis)
      * ${\sum m(v_x)_1 = \sum m(v_x)_2  }$  
      * $ e= =\frac{ [(v_{Bx})_2 - (v_{Ax})_2]}{[(v_{Ax})_1 - (v_{Bx})_1]}$    
      * plane of impact (y axis)
        * $m_A(v_{Ay})_1 = m_A(v_{Ay})_2$ 
        *  $ m_B(v_{By})_1 = m_B(v_{By})_2 $  





 <div style="page-break-after: always;"></div> 

 <div style="page-break-after: always;"></div>  

### Chapter 15 Sections 5-7 

* Angular Momentum
  * $\mathbf { H } _ { Q } = \mathbf { r } _ { O P }  \times  m \mathbf { v }$  
  * Direction: right-hand rule
  * Cross product
    * $\mathbf { H } _ { o } = \mathbf { r } _ { o P } \times m \mathbf { v } = m \operatorname { det } \left| \begin{array} { c c c } { \hat { \mathbf { i } } } & { \hat { \mathbf { j } } } & { \hat { \mathbf { k } } } \\ { r _ { x } } & { r _ { y } } & { r _ { z } } \\ { v _ { x } } & { v _ { y } } & { v _ { z } } \end{array} \right|$  

      $= m \left[ \left( r _ { y } v _ { z } - r _ { z } v _ { y } \right) \hat { \mathbf { i } } 
      -\left( r _ { x } v _ { z } - r _ { z } v _ { x } \right) \hat { \mathbf { j } } + \left( r _ { x } v _ { y } - r _ { y } v _ { x } \right) \hat { \mathbf { k } } \right]$  a 
  * Units: (distance·mass·speed)
  * $kg·m^2 /s $ or $slug·ft^2 /s$ 

* Relations between Moment of a Force and Angular Momentum

  > the resultant moment about point O of all the forces acting on the particle is equal to the time rate of change of the particle’s angular momentum about point O.

  * $\sum \mathbf { M } _ { o } = \mathbf { r } \times \sum \mathbf { F } = \mathbf { r } \times m \dot { \mathbf { v } }$
    $\sum \mathbf { M } _ { o } = \dot { \mathbf { H } } _ { 0 }$  (can be rewritten in the form $\Sigma \mathbf { M } _ { O } d t = d \mathbf { H } _ { O }$)

* Principle of Angular Impulse and Momentum
  * **angular impulse** 

    *  $\int _ { t _ { 1 } } ^ { t _ { 2 } } \mathbf { M } _ { O } d t = \int _ { t _ { 1 } } ^ { t _ { 2 } } ( \mathbf { r } \times \mathbf { F } ) d t$ 

  * principle of angular impulse and momentum for a system of particles

    * $\Sigma \left( \mathbf { H } _ { O } \right) _ { 1 } + \Sigma \int _ { t _ { 1 } } ^ { t _ { 2 } } \mathbf { M } _ { O } d t = \Sigma \left( \mathbf { H } _ { O } \right) _ { 2 }$ 

  * Conservation of Angular momentum 

    > When the angular impulses acting on a particle are all zero(eg. central force) 

    *  moment review:

      * Vector formulation: $\mathbf { M } _ { o } = \mathbf { r } \times \mathbf { F }$ 
      * Direction:   right-hand rule 

      <img src="https://ws3.sinaimg.cn/large/006tNbRwly1fwrt2tfkcfj3070058wew.jpg" style="zoom:70%" />

    * particle 
      $\left( \mathbf { H } _ { O } \right) _ { 1 } = \left( \mathbf { H } _ { o } \right) _ { 2 }$ 
    * system of particles 
      $\Sigma \left( \mathbf { H } _ { O } \right) _ { 1 } = \Sigma \left( \mathbf { H } _ { O } \right) _ { 2 }$ 


 <div style="page-break-after: always;"></div>   



### Chapter 16 Sections 1-5

Planar Kinematics of a Rigid Body

* Planar Kinematics of a Rigid Body

  *  **Translation** -within a reference plane.
    *  $\mathbf { r } _ { B } = \mathbf { r } _ { A } + \mathbf { r } _ { B / A }$ 
       $\mathbf { v } _ { B } = \mathbf { v } _ { A }$
       $\mathbf { a } _ { B } = \mathbf { a } _ { A }$  
  *  **Rotation**- about axis perpendicular to that reference plane 

    * $\omega = \frac { d } { d t } \theta = \dot {\theta}$
      $\alpha = \frac { d } { d t } \omega = \dot { \omega }$
      $\alpha d \theta = \omega d \omega$ 
    * $\omega = \omega _ { 0 } + \alpha _ { c } t$
      $\theta = \theta _ { 0 } + \omega _ { 0 } t + 1 / 2 \alpha _ { c } t ^ { 2 }$
      $\omega ^ { 2 } = \omega _ { 0 } ^ { 2 } + 2 \alpha _ { c } \left( \theta - \theta _ { 0 } \right)$  
  *  [Cross product ](https://en.wikipedia.org/wiki/Cross_product): 
     *  formula: $\mathbf { a } \times \mathbf { b } = \| \mathbf { a } \| \| \mathbf { b } \| \sin ( \theta ) \mathbf { n }$   
     *  The cross product **a** × **b**  changes as the angle between the vectors **a**and **b**  changes.


* Absolute Motion Analysis

  * Steps:  
    1. locate point of interest in terms of physical parameters:
       * lengths and angles
    2. just differentiate to get speed and acceleration  

* Relative Motion Analysis

  * $\mathbf { r } _ { B } = \mathbf { r } _ { A } + \mathbf { r } _ { B / A }$ 

  * Velocity 

    * $\mathbf { v } _ { B } = \mathbf { v } _ { A } + \mathbf { v } _ { B / A }$  
      $\mathbf { v } _ { P } = \mathbf { \omega } \times \mathbf { r } _ { P }$ 
      $\mathbf { V } _ { B / A } = \mathbf { \omega } _ { A B } \times \mathbf { r } _ { B / A }$ 

  * Acceleration
    $\mathbf { a } _ { P } = \mathbf { a } \times \mathbf { \mathbf { r } } _ { P } + \mathbf { \omega } \times \left( \mathbf { \omega } \times \mathbf { r } _ { P } \right)$  

    $\mathbf { a } _ { B } = \mathbf { a } _ { A } + \mathbf { a } _ { A B } \times  \mathbf { r } _ { B / A } - \omega _ { A B } ^ { 2 } \mathbf { r } _ { B / A }$  

 <div style="page-break-after: always;"></div>   

 <div style="page-break-after: always;"></div> 

###  Chapter 16 Sections 6-7



Planar Kinematics of a Rigid Body

*  Instantaneous Center of Zero Velocity
  *  Defination
        * Location that just for an instant has zero velocity
        * May have non-zero acceleration 
        * Not necessarily on the body
  *  Three ways to find:
        * With velocity of point on body $v_A$and ω.
            * At distance of $v_A /ω$  ($r_{A/IC}$)  
            * With line of action of two nonparallel velocities $v_A $and $v_B$ 
            * With magnitude and direction of two parallel velocities
            * via proportional triangle
*  Acceleration via Absolute Motion Analysis
   *  complictate 
*  Acceleration via Relative Motion Analysis
     *  $\mathbf { a } _ { B / A } = \left( \mathbf { a } _ { B / A } \right) _ { t } + \left( \mathbf { a } _ { B / A } \right) _ { n }$ 
     *  $\mathbf { a } _ { B } = \mathbf { a } _ { A } + \boldsymbol { \alpha } \times \mathbf { r } _ { g / A } - \omega ^ { 2 } \mathbf { r } _ { B / A }$ 
          *  $\begin{aligned} \mathbf { a } _ { B } & = \text { acceleration of point } B \\ \mathbf { a } _ { A } & = \text { acceleration of the base point } A \\ \boldsymbol { \alpha } & = \text { angular acceleration of the body } \\ \omega & = \text { angular velocity of the body } \\ \mathbf { r } _ { B / A } & = \text { position vector directed from } A \text { to } B \end{aligned}$ 

* Procedure for Analysis
  * Vector Analysis
    * Kinematic Diagram.
      * establish the directions of the fixed x, y coordinates
      * indicate $\mathbf { a } _ { A } , \mathbf { a } _ { B } , \boldsymbol { \omega } , \boldsymbol { \alpha } , \mathbf { a n d } \mathbf { r } _ { B / A }$ 
    * Acceleration Equation. 
      * express the vectors in Cartesian vector form and apply 
        $\mathbf { a } _ { B } = \mathbf { a } _ { A } + \boldsymbol { \alpha } \times \mathbf { r } _ { g / A } - \omega ^ { 2 } \mathbf { r } _ { B / A }$  
      * check direction on sign



 <div style="page-break-after: always;"></div>   

### Chapter 17 Sections 1-3

* Angular Momentum Balance:

  * $\sum \mathbf { M } _ { / O } = \dot { \mathbf { H } } _ { / O } = \mathbf { r } _ { P / O } \times m \mathbf { a } _ { p }$ 
  * Angular Momentum about the **Center of Mass** 
    * $\sum \mathbf { M } _ { / G } = \dot { \mathbf { H } } _ { G } = \mathbf { r } _ { G / G } \times m \mathbf { a } _ { G } = 0$ 

* Planar Kinetics of a Rigid Body

  * rotating about a fixed axis.

    * $I _ { 1 O } ^ { z } = \int _ { m } r _ { O P } ^ { 2 } d m = \int _ { V } r _ { O P } ^ { 2 } \rho d V = \rho \int _ { V } r _ { O P } ^ { 2 } d V$  
    * shell element : $I _ { z } = \frac { 1 } { 2 } m R ^ { 2 }$
    * Disk element:  $d I _ { y } = \frac { 1 } { 2 } ( d m ) x ^ { 2 } = \frac { 1 } { 2 } \left[ \rho \left( \pi x ^ { 2 } \right) d y \right] x ^ { 2 }$  

  * “Parallel Axis” theorem 

    * $I _ { / O } ^ { z } = I _ { / G } ^ { z } + m d ^ { 2 }$ 

  * Radius of Gyration

    > Just another way to express Moment of Inertia

    * $I = m k ^ { 2 }$
      $k = ( I / m ) ^ { 1 / 2 } \\ k: \text{radius of gyration} \  m: mass $  
    * The sum of moments on an object about a fixed point equals the rate of change of the angular momentum about that fixed point: 
      * $\sum \mathbf { M } _ { O } = \dot { \mathbf { H } } _ { O }$  
      * For a **particle**, an object with no dimensions:
        * $\sum \mathbf { M } _ { / O } = \mathbf { r } _ { P / O } \times m \mathbf { a } _ { P }$
          $\sum \mathbf { M } _ { / P } = \mathbf { r } _ { P / P } \times m \mathbf { a } _ { P } = 0$ 
      * For a rigid body that is <u>constrained from rotating</u>:
        * $\sum \mathbf { M } _ { / O } = \mathbf { r } _ { P / O } \times m \mathbf { a } _ { P }$
          $\sum \mathbf { M } _ { / G } = \mathbf { r } _ { G / G } \times m \mathbf { a } _ { G } = 0$  
      * For a rigid body <u>rotating about a fixed axis</u>:
        * $\sum \vec { \mathbf { M } } _ { o } = \vec { \mathbf { a } } _ { / O } ^ { z } =  { \alpha} \left( I _ { / G } ^ { z } + m d ^ { 2 } \right)$
          $\sum \vec { \mathbf { M } } _ { / G } = { \alpha} \  I _ { / G } ^ { z }$   

  * Equations of Motion: Translation

    * Rectilinear Translation
      * $\begin{aligned} \Sigma F _ { x } & = m \left( a _ { G } \right) _ { x } \\ \Sigma F _ { y } & = m \left( a _ { G } \right) _ { y } \\ \Sigma M _ { G } & = 0 \end{aligned}$ 
    * Curvilinear Translation
      * $\begin{aligned} \Sigma F _ { n } & = m \left( a _ { G } \right) _ { n } \\ \Sigma F _ { t } & = m \left( a _ { G } \right) _ { t } \\ \Sigma M _ { G } & = 0 \end{aligned}$  

 <div style="page-break-after: always;"></div>   

### Chapter 17 Sections 4-5

* friction
* a cylinder rolls without slipping
  * $ a_G = \alpha r$
  *  340 Chapter 16 Planar Kinematics of a Rigid Body

* Planar Kinetics of a Rigid Body

  * Just particles or rigid bodies **only translating**:

    * $\Sigma \underline { \mathbf { M } } _ { O } = \mathbf { r } _ { G / O }  \times m \mathbf { a } _ { G }$ 
      $\Sigma \underline { \mathbf { M } } _ { G } = 0$ 

  * **Rotation** only about fixed axis, no translation:

    * $\Sigma \underline { \mathbf { M } } _ { / O } = \underline { \alpha } I _ { O } = \underline { \alpha } \left( I _ { G } + m d ^ { 2 } \right)$ 

      $\Sigma \mathbf { M } _ { / G } =  { \alpha } I _ { G }$   

  * Rigid bodies translating and rotating:

    * $\Sigma \underline { \mathbf { M } } _ { O } = \underline { \mathbf { r } } _ { G / O } \times m \mathbf { \alpha } _ { G } + \underline { a } I _ { G }$ 
      $ \Sigma \mathbf { M } _ { / G } = \underline { \alpha } I _ { G }$  

* At what angle does disk slide instead of roll? 

* <img src="https://ws2.sinaimg.cn/large/006tNbRwly1fxoeqn7kdej30hw0l2q65.jpg" style="zoom:70%" /> 

 <div style="page-break-after: always;"></div>   

### Chapter 17 Sections 3-5

summary

| **Translation**                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Rectilinear Translation<br />$\begin{aligned} \Sigma F _ { x } & = m \left( a _ { G } \right) _ { x } \\ \Sigma F _ { y } & = m \left( a _ { G } \right) _ { y } \\ \Sigma M _ { G } & = 0 \end{aligned}$ | Curvilinear Translation<br />$\begin{aligned} \Sigma F _ { n } & = m \left( a _ { G } \right) _ { n } \\ \Sigma F _ { t } & = m \left( a _ { G } \right) _ { t } \\ \Sigma M _ { G } & = 0 \end{aligned}$ |
| acceleration<br />$a _ { G } = d v _ { G } / d t \quad a _ { G } d s _ { G } = v _ { G } d v _ { G }$ | $\left( a _ { G } \right) _ { n } = v _ { G } ^ { 2 } / \rho$ <br />$\left( a _ { G } \right) _ { t } = d v _ { G } / d t \quad \left( a _ { G } \right) _ { t } d s _ { G } = v _ { G } d v _ { G }$ |
| **Rotation about a Fixed Axis**                              |                                                              |
| $\begin{array} { r l } { \sum F _ { n } } & { = m \left( a _ { G } \right) _ { n } = m \omega ^ { 2 } r _ { G } } \\ { \Sigma F _ { t } } & { = m \left( a _ { G } \right) _ { t } = m \alpha r _ { G } } \\ { } & { \Sigma M _ { G } = I _ { G } \alpha } \end{array}$ | If the angular acceleration is variable, use<br />$\alpha = \frac { d \omega } { d t } \quad \alpha d \theta = \omega d \omega \quad \omega = \frac { d \theta } { d t }$ <br />If the angular acceleration is constant, use<br />$\begin{aligned} \omega & = \omega _ { 0 } + \alpha _ { c } t \\ \theta & = \theta _ { 0 } + \omega _ { 0 } t + \frac { 1 } { 2 } \alpha _ { c } t ^ { 2 } \\ \omega ^ { 2 } & = \omega _ { 0 } ^ { 2 } + 2 \alpha _ { c } \left( \theta - \theta _ { 0 } \right) \end{aligned}$ |
| **Gerneral plane motion**                                    |                                                              |
| $\begin{aligned} \Sigma F _ { x } & = m \left( a _ { G } \right) _ { x } \\ \Sigma F _ { y } & = m \left( a _ { G } \right) _ { y } \\ \Sigma M _ { G } & = I _ { G }  { \alpha  }  \end{aligned}$ | $\Sigma M _ { Ic } = I _ { G } \alpha + \left( m a _ { G } \right) d = I _ { IC } \alpha$ |
|                                                              |                                                              |

*  ![image-20181205105003967](Dynamics_img/image-20181205105003967.png)

<div style="page-break-after: always;"></div>   

 <div style="page-break-after: always;"></div>   

