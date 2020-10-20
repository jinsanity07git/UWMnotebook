 Mathematics,linear algebra,diff equations

### Content

* references: Advanced Engineering Mathematics, E. Kreyszig, 7th Ed. Wiley. 

### Ordinary Differential Equations 

Topics:

- [ ]  First Order Differential Equations

- [ ] Linear Second Order Differential Equations
- [ ] Higher Order Differential Equations
- [ ] Laplace Transform
- [ ] Series Solutions of Differential Equations
- [ ] Sturm-Liouville Theory & Eigenfunction Expansions

### Partial Differential Equations[^1] 

Topics:
- [ ] Solution of Equations (Wave Equation, Heat Equation, Potential, Elastic Membrane, etc.) -  Separation of Variables, Use of Fourier Series
- [ ] Laplace Transform
- [ ] Error Functions
- [ ] Use of Sturm-Liouville Theory & Eigenfunction Expansions

### Linear Algebra 

Topics:
- [x] Matrices and Determinants
- [x] Solutions to Systems of Linear Equations - Gauss Elimination Method
- [x] Cayley Hamilton Theorem
- [ ] Definiteness of a Matrix
- [x] Ranks 秩
- [x] Euclidean Norm
- [x] Eigenvalues and Eigenvectors
- [ ] Jordan Forms   -- link 
- [ ] Repeated Eigenvalues  -- link



Solutions to Systems of Linear Equations - Gauss Elimination Method

* [System of linear equations - Wikipedia](https://en.wikipedia.org/wiki/System_of_linear_equations)

  * Row reduction

    Main article: [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)

  To perform row reduction on a matrix, one uses a sequence of [elementary row operations](https://en.wikipedia.org/wiki/Elementary_row_operations) to modify the matrix until the lower left-hand corner of the matrix is filled with zeros, as much as possible. There are three types of elementary row operations:

  - Swapping two rows,

  - Multiplying a row by a nonzero number,

  - Adding a multiple of one row to another row.

  - Matrix solution[[edit](https://en.wikipedia.org/w/index.php?title=System_of_linear_equations&action=edit&section=17)]

    If the equation system is expressed in the matrix form ![A{\mathbf {x}}={\mathbf {b}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/afd4dd2b20811c02f1881f90b8215743566cd95d), 

    the entire solution set can also be expressed in matrix form. If the matrix *A* is square (has *m* rows and *n*=*m* columns) and has full rank (all *m* rows are independent), then the system has a unique solution given by


#### 3.3 Skew-symmetric matrix [wiki](https://en.wikipedia.org/wiki/Skew-symmetric_matrix)

#### 3.7 inverse matrix 

[Invertible matrix](https://en.wikipedia.org/wiki/Invertible_matrix#Methods_of_matrix_inversion)

The determinant of **A** can be computed by applying the [rule of Sarrus](https://en.wikipedia.org/wiki/Rule_of_Sarrus) as follows:

![\det(\mathbf {A} )=aA+bB+cC.](https://wikimedia.org/api/rest_v1/media/math/render/svg/8d36697eaa2961b54cfc06e44c102f6dce854e97) 

[Linear Algebra with Python](https://www.google.com/search?q=python+linear+algebra+library&oq=python+&aqs=chrome.0.69i59j69i61j69i60l2j69i59l2.1629j0j7&sourceid=chrome&ie=UTF-8) 

[Matrix Inverse -- from Wolfram MathWorld](http://mathworld.wolfram.com/MatrixInverse.html)

For a ![3×3](http://mathworld.wolfram.com/images/equations/MatrixInverse/Inline15.gif) [matrix](http://mathworld.wolfram.com/Matrix.html)

![ A=[a_(11) a_(12) a_(13); a_(21) a_(22) a_(23); a_(31) a_(32) a_(33)], ](http://mathworld.wolfram.com/images/equations/MatrixInverse/NumberedEquation3.gif) 

the matrix inverse is  (note the negative sign on (i != j) )

![ A^(-1)=1/(|A|)[|a_(22) a_(23); a_(32) a_(33)| |a_(13) a_(12); a_(33) a_(32)| |a_(12) a_(13); a_(22) a_(23)|;   ; |a_(23) a_(21); a_(33) a_(31)| |a_(11) a_(13); a_(31) a_(33)| |a_(13) a_(11); a_(23) a_(21)|;   ; |a_(21) a_(22); a_(31) a_(32)| |a_(12) a_(11); a_(32) a_(31)| |a_(11) a_(12); a_(21) a_(22)|]. ](http://mathworld.wolfram.com/images/equations/MatrixInverse/NumberedEquation4.gif) 



#### 3.10 the determinant

* classical adjoint ([Adjugate matrix - Wikipedia](https://en.wikipedia.org/wiki/Adjugate_matrix))

  * The adjugate of **A** is the *transpose* of **C**, that is, the *n*×*n* matrix whose (*i*,*j*) entry is the (*j*,*i*) cofactor of **A**,

  ![{\displaystyle \operatorname {adj} (\mathbf {A} )_{ij}=\mathbf {C} _{ji}=(-1)^{i+j}\mathbf {M} _{ji}\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5ffdf1e439812c129537fb2f53d72dccb10f6f91). 

  * ![{\displaystyle \operatorname {adj} (\mathbf {A} )=\det(\mathbf {A} )\mathbf {A} ^{-1}~,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bf80fab79d92470316f819bd40d94f161672316a)  

  * ![{\displaystyle \mathbf {A} \operatorname {adj} (\mathbf {A} )=\det(\mathbf {A} )\,\mathbf {I} ~.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/796464af46244ce68d4dacd11748095d1efd15f6) 

  For a ![3×3](http://mathworld.wolfram.com/images/equations/MatrixInverse/Inline15.gif) [matrix]

* ![{\displaystyle \operatorname {adj} (\mathbf {A} )=\mathbf {C} ^{\mathsf {T}}={\begin{pmatrix}+{\begin{vmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{vmatrix}}&-{\begin{vmatrix}a_{12}&a_{13}\\a_{32}&a_{33}\end{vmatrix}}&+{\begin{vmatrix}a_{12}&a_{13}\\a_{22}&a_{23}\end{vmatrix}}\\&&\\-{\begin{vmatrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{vmatrix}}&+{\begin{vmatrix}a_{11}&a_{13}\\a_{31}&a_{33}\end{vmatrix}}&-{\begin{vmatrix}a_{11}&a_{13}\\a_{21}&a_{23}\end{vmatrix}}\\&&\\+{\begin{vmatrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{vmatrix}}&-{\begin{vmatrix}a_{11}&a_{12}\\a_{31}&a_{32}\end{vmatrix}}&+{\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}}\end{pmatrix}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ba4611744163871c90f73f47d564dc026f78b9e)   

* 



#### 3.12 eigenvalues and eigenvectors

[Eigenvalue -- from Wolfram MathWorld](http://mathworld.wolfram.com/Eigenvalue.html)

[Eigenvector -- from Wolfram MathWorld](http://mathworld.wolfram.com/Eigenvector.html)

example:

* [Eigenvalues and eigenvectors of 3 by 3 matrices](http://wwwf.imperial.ac.uk/metric/metric_public/matrices/eigenvalues_and_eigenvectors/eigenvalues2.html)

  * [characteristic equation](http://mathworld.wolfram.com/CharacteristicEquation.html)

    ![ ](http://mathworld.wolfram.com/images/equations/Eigenvalue/NumberedEquation6.gif)

  * [ "Eigenvalues Calculator 3x3" ](http://www.wolframalpha.com/widgets/view.jsp?id=9aa01caf50c9307e9dabe159c9068c41) 

  * [Cubic Formula -- from Wolfram MathWorld](http://mathworld.wolfram.com/CubicFormula.html)

  * [Wolfram|Alpha Widgets: "Solve cubic equation](http://www.wolframalpha.com/widgets/view.jsp?id=3f4366aeb9c157cf9a30c90693eafc55)

  * [3 Ways to Solve a Cubic Equation - wikiHow](https://www.wikihow.com/Solve-a-Cubic-Equation)

    * [ Algebraic solution](https://en.wikipedia.org/wiki/Cubic_function#Algebraic_solution) 

    * [Exact Solution of Cubic Equations - math for college](http://mathforcollege.com/nm/mws/gen/03nle/mws_gen_nle_bck_exactcubic.pdf)


#### references:

- [ ] [Linear Algebra Cheat Sheet for numerical computing environments, ](https://github.com/scalanlp/breeze/wiki/Linear-Algebra-Cheat-Sheet)

- [x] [Linear Algebra Review and Reference](http://www.cs.cmu.edu/~zkolter/course/15-884/linalg-review.pdf)

- [ ] [guide to linear algebra Preview](https://minireference.com/static/excerpts/noBSguide2LA_preview.pdf) (160 pages, PDF)

  - [ ] https://minireference.com/
  - [ ] Click to see large concept map
  - [ ] [Free tutorial](https://minireference.com/static/tutorials/linear_algebra_in_4_pages.pdf) (4 pages, PDF)

- [ ] [mind map](https://www.mindomo.com/zh/mindmap/linear-algebra-381bdd65d6c649a6925c5c11be0616f0)

- [Cheat Sheet - Berkeley Math](https://math.berkeley.edu/~peyam/Math54Fa11/Cheat%20Sheets/Cheat%20Sheet%20(tiny%20font,%20no%20margins).pdf)

- [Handout A: Linear Algebra Cheat Sheet 1 Basic Notations](http://www.se.cuhk.edu.hk/~manchoso/1415/xidian/A-linalg.pdf)

- [Quora cheat sheet](https://www.quora.com/What-is-the-best-linear-algebra-cheat-sheet-for-machine-learning#)

  * [**Cheat Sheets for AI, Neural Networks, Machine Learning, Deep Learning & Big Data**](https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463)





### Calculus 

Topics:

- [ ] Derivatives, Differentiation and Partial Derivatives - Taylor's Series
- [ ] Curvature of a Curve
- [ ] Definite and Indefinite Integrals
- [ ] Functions of Several Variables
- [ ] Line and Surface Integrals
- [ ] Green's Theorem





[Mind maps of Advanced Mathematics and various branches thereof](https://math.stackexchange.com/questions/124709/mind-maps-of-advanced-mathematics-and-various-branches-thereof)

[Paul's Online Math Notes](http://tutorial.math.lamar.edu/)

* [ Is Paul's Online Math Notes a good enough source for self-teaching calculus 3 and ODE?](https://www.quora.com/Is-Pauls-Online-Math-Notes-a-good-enough-source-for-self-teaching-calculus-3-and-ODE)

Derivatives 

* newton's method [link](http://tutorial.math.lamar.edu/Classes/CalcI/NewtonsMethod.aspx)
* 









## CHEAT SHEETS & TABLES

- [x] Algebra Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,30,N) - 139 KB]  
- [ ] Algebra Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,31,N) - 135 KB]   
- [x] Trig Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,32,N) - 109 KB]  
- [ ] Trig Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,33,N) - 107 KB]   
- [x] Common Derivatives and Integrals ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,34,N) - 56 KB] 
- [ ] Common Derivatives and Integrals (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,35,N) - 137 KB]   
- [x] Complete Calculus Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,40,N) - 240 KB]  
- [ ]  Complete Calculus Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,41,N) - 232 KB]   
- [x] Limits Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,42,N) - 114 KB]   
- [ ] Limits Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,43,N) - 112 KB]  
- [x]  Derivatives Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,44,N) - 61 KB]   
- [ ] Derivatives Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,45,N) - 194 KB]   
- [x] Integrals Cheat Sheet ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,46,N) - 178 KB]   
- [ ] Integrals Cheat Sheet (Reduced) ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,47,N) - 174 KB]   
- [x] Table of Laplace Transforms ![img](http://tutorial.math.lamar.edu/images/DoubleArrowRight.gif) PDF Link : [[Link](http://tutorial.math.lamar.edu/getfile.aspx?file=B,36,N) - 96 KB]x

## Footnote 

[^1]: PART C . CHAPTER 12. Partial Differential Equations (PDEs) ; page 556 / 1283
[^]: 