Transportation Topic of Operation Research









### C_ 3   Introduction to Linear Programming

#### 3.1 What is a Linear Programming (LP) Problem?

LP: Linear Programming (verb), LP Model (noun)
LP is a tool for solving some optimization problems.
An LP has an objective function and constraints 
	e.g., profit objective and budget and time constraints.
All equations in LP are linear.
Some LP terminology 

##### Linearity

* Proportionality
* Additivity

##### The four LP assumptions

![image-20180829101618338](https://ws1.sinaimg.cn/large/006tNbRwly1fuqzb0z01vj30e808xt9n.jpg)  

LP Terminology







##### LP Terminology

(1) Feasible region
(2) Solution X=(X1,X2)=(0,0) or (100, 200) or (100, -1)
(3) Feasible solution/ infeasible solution
(4) Basic solution: (2D-2 lines meet, 3D-3 planes meet)
     (This definition is the same as the previous one of BS 
     from geometry point of view.) 
(5) Basic feasible solution (BFS)
(6) Optimal solution: best sol.

#### 3.2 Graphical solution

Any LP with only two variables can be solved graphically.  

![image-20180829101824889](https://ws4.sinaimg.cn/large/006tNbRwly1fuqzd69tfgj309i0bumxu.jpg)

* Isoprofit line 
* We can convert (≤, ≥) to (=) by adding a slack variable (s) or subtracting an excess variable (e)

##### Convex set

LP deals with only convex sets (feasible Region)
A set of points S is a convex set if ...

* If S is a polygon, the points at its corners are corner points.  (Text has more explanations.)

In LP, a feasible area is a convex set.
Compare the convex set and convex function.

#### 3.5 A Work-Scheduling Problem

* minimum-cost methods 
  * for satisfying workforce requirements in manufacturing industry (production schedule, maintenance schedule) and service industry (doctor schedule, nurse schedule, airplane schedule).
* types
  * static scheduling problem
  * dynamic scheduling problem
* eg.
  * xi: #people **beginning** work on day i (i=1,7)

#### 3.6 A Capital Budgeting Problem

* net present value (NPV) 
  * The total current value of cash flows for any investment 
* eg. ![image-20180829103213141](https://ws1.sinaimg.cn/large/0069RVTdly1fur05m2fktj30e408nmy0.jpg)

#### 3.8 Blending Problems (product mix)

![image-20180829103559774](https://ws1.sinaimg.cn/large/0069RVTdly1fur05h7f58j30i90ej41k.jpg) 



#### 3.9 Production Process Models

key step 

* determine how the input to a later stage of the process is related to the output from its earlier stages. (balance eq)
* ![image-20180829103858146](https://ws3.sinaimg.cn/large/0069RVTdly1fuqzy5hzj0j30b208smy0.jpg)

![image-20180829103922838](https://ws2.sinaimg.cn/large/0069RVTdly1fuqzyi50juj30hv06i3zq.jpg) 











graphical method

* 1slack variable

* surplus variable  

If an LP has ≥ or = constraints, however, a starting bfs may not be readily apparent.  

In such a case, the Big M method may be used to find an initial bfs.

* * (≤) constraint => add a slack variable
  * (=) constraint => add an artificial variable
  * (≥) constraint => subtract an excess variable and then add an artificial variable
  * Use Big-M in the obj ft row for the artificial variables.

    ​                    



### C4 _The Simplex Algorithm Goal
Programming 

#### 4.1 & 4.5 Simplex Method

![image-20180829095508756](https://ws3.sinaimg.cn/large/006tNbRwly1fuqyogt5uuj304e038jr9.jpg)

![image-20180829095447342](https://ws1.sinaimg.cn/large/006tNbRwly1fuqyo3z4c4j30er08qt9x.jpg)

##### 4.5 The Simplex Algorithm







#### Big M Method 

Description of the Big M Method

1. (b≥0) Modify the constraints so that the rhs of each constraint is nonnegative.  	

*  If rhs<0, multiply -1 on both sides.

* e.g.,  2x1-x2 ≤-5 Þ -2x1+x2 ≥+5

2.(Standard form) <br/>Convert inequality constraints to (=) constraints. <br/>(Use slack/ excess variables for ≤, ≥).

3.(Initial basis) <br/>Add artificial variables to the rows without slack variables.  (Also add sign restrictions si, ei, ai ≥ 0.)

4.(Adjustment of row-0) <br/>Add (for each artificial variable) $Ma_i$ to min problem objective functions <br/>(or - $Ma_i$  to max prob).

5.(Canonical form) <br/>Make the coefficients of artificial variables ==in the obj ft row== zero by ERO, and start SM. 

#### Miscellaneous issues 

#### Goal Programming - Software

#### Summary of Simplex algorithm

1. Convert the LP to standard form 
2. find m basic variables directly from standard form 
   1. or inventing engough atificial variables 
3. convert the LP's  objective function the row  0 format 
4. obtain canonical form1   
5. iteration & identify the current bfs
   1. determine if the current bfs is optimal
6. find a new bfs with a  better objective value
   1. pivot column (determine which nbv should become a bv)
   2. pivot row (determine which bv should become a nbv) 
      1. minimum ratio test
   3. pivot term (use elementary row operations to find a new bfs with better objective value)

### C5 _ Sensitivity Analysis: An Applied Approach



### C7_Transportation,Assignment & Transshipment Problems

A transportation problem (TP) tries to minimize transportation cost from suppliers to customers while meeting capacity and demand constraint.

General TP structure

![image-20180828091509453](https://ws2.sinaimg.cn/large/006tNbRwly1fupry1lsbjj30eo097js0.jpg)

![image-20180828091613273](https://ws1.sinaimg.cn/large/006tNbRwly1fupry5h0i1j30gz09zdh8.jpg)

* Transportation tableau
  * This tableau is used to solve a TP problem.
  * It shows the demand, supply and cost.
  * It also shows the solution (xij).
  * Only basic xij values are shown in the table.

![image-20180828091826012](https://ws4.sinaimg.cn/large/006tNbRwly1fuprzyv1x8j307w04zmx4.jpg)

Finding initial BFS for TP

Unlike other LP problems, a balanced transportation problem with m supply points and demand points is easy to solve although it has m + n equality constraints.(We do not need the big-M method.)

Initial BFS

* There are three basic methods to find the bfs for a balanced TP 
  * Northwest Corner Method
  * Minimum Cost Method
  * Vogel’s Method

#### 7.3 The Transportation Simplex Method (TSM)

* The iteration procedure is:
  * Step 1 Determine the **entering** variable. 
    * We assume we have this variable for now.
  * Step 2 Find the **loop** involving the entering variable.
  * Step 3 **Label** the cells in the loop as even or odd cells.
  * Step 4 **Update** the loop: decrease the value of each odd cell by θ and increase the value of each even cell by θ. (θ: min value in the odd cells) 
    * If θ=0, degeneracy happened.  We adjust the cells by zero amount. 
    * If multiple cells have the same θ value, we arbitrarily choose one of these odd cells for updating the loop.  Degeneracy will happen.



find an initial bfs (NW method) 

update the table (loop procedure)

Determining entering variable

* The procedure is ：
  * Make ui for each row and vj for each column.
  * Let u1=0.
  * Determine other ui and vj using cij= ui + vj for all BVs.
  * We find __𝑐__𝑖𝑗_ of NBVs by using these ui and vj values.
  * Check optimality and choose an entering variable.



Example

377-380



#### 7.5.Assignment Problems

Assignment problems (APs) assign one supply point to one                      demand point.  (For this problem, m should be the same as n.)  

The xij values can be either 0 or 1.

* If xij =1, supply point i is assigned to demand point j.
* only m basic variables are 1, <br/> and m-1 basic variables are 0

In general an assignment problem is a balanced transportation problem, in which all supplies and demands are equal to 1.



##### Hungarian Method

* Step1 (Cost matrix reduction) 
  * For each row, subtract the minimum value of the row.
  * And then, for each column, subtract the minimum value of the column.
* Step2:  Draw the minimum number of lines (horizontal and/or vertical) to cover all zeros in the matrix. If m lines are required, we got an opt sol. W/o, proceed to step 3.
* Step3: Find the smallest nonzero element (call its value k) uncovered by the lines drawn in step 2. Now subtract k from each uncovered element and add k to each element that is covered by two lines. Return to step2.

![image-20180828101509529](https://ws1.sinaimg.cn/large/006tNbRwly1fuptnqkrzrj30gt0aaace.jpg)



#### 7.6 transshipment problem 

transshipment problem 

* A  transportation problem allows only shipments that go **directly from supply points to demand points**

transshipment points

* In many situations, there are also points that can receive and send goods, called **transshipment points**, in the transportation network or supply chain. 

main tasks 

*  determining shipping cost, and demand quantities and supply quantities

* eg. p390-393











summary 

395-397







### C8_ Network Models

A network can represent material flow or a sequence of activities. Many practical problems can be optimized by network analysis. 

- Shortest path problem,
- Maximum flow problem, 
- Minimum spanning tree problem, and
- PERT/CPM.

#### 8.2 Shortest Path Problems

* In a small problem, the solution is easy, by “inspection.”

  * enumeration

*  Dijkstra’s algorithm

  * all arc lengths are non-negative
  * In each iteration, we determine the minimum distance from the source to only one city. 
  * The formula is 

  Temp label of node j  = 

  min {its current temp label, 
      node i’s permanent label +length of arc (i,j) ∀ i preceding j}

##### Eg 2: Equipment  Replacement

**Modeling Shortest Path Problem by Transshipment formulation**  

page ...

#### 8.3 Maximum Flow Problems

Sometimes, we want to know the max. amount of traffic or commodity from one place **(source)** to another **(sink)** subject to arc capacity. 

* This can be solved by LP or a special algorithm, 
  **Ford-Fulkerson Method.** 
  (A simple and efficient method.)



Example 3 : 

* LP formulation: maximizing number of barrels of oil per hour that can be sent from so to $s_i$ .
* Add an artificial arc, $a_0$ , from sink to source for flow balance at nodes. 
* LP formulation idea: maximum circulation quantity
  Decision variable
  xij = Millions of barrels of oil per hour that will pass through arc(i,j) of pipeline.
* Two types of constraints
  * **(Arc capacity)** 0 ≤ flow through each arc ≤ arc capacity 
  * **(Flow balance)** (Flow into node i)=(Flow out from node i)
* Objective: maximize circulation quantity

##### Ford-Fulkerson Method

book 



#### 8.4 CPM and PERT

Network models can be used as an aid in the **scheduling** of large complex projects that consist of many activities.

**methods**

* critical path method (CPM).
* program evaluation and review technique (PERT) 
  * If the duration of activities is not known with certainty, 
  * can be used to estimate the probability that the project will be completed by a given deadline.
* PERT and CPM are closely related and often treated together as PERT/CPM

Project Network





Project Network

##### Project Network

* A network for **precedence relationships** between activities is called a project network. 
* An activity may have predecessors.
* We use an **activity on arc (AOA)** network.
* Sometimes, it uses a **dummy activity** that takes zero time just to show precedence relationship. 

![image-20180828214806185](https://ws4.sinaimg.cn/large/006tNbRwly1fuqdo0qudrj308n03f3yl.jpg)



##### CPM/PERT construction

- Node 1 represents the start of the project. An arc should lead from node 1 to represent each activity that has no predecessors.
- A node (called the finish node) representing the completion of the project should be included in the network.
- Number the nodes such that the node of the completion time of an activity has a larger number than the node of the beginning of the activity.
- An activity should not be represented by more than one arc in the network
- Two nodes can be connected by at most one arc.



Earliest/Latest start time

##### Earliest/Latest start time

![image-20180828215343051](https://ws4.sinaimg.cn/large/006tNbRwly1fuqdu3ii3cj30f109rmyf.jpg)







#### 8.5 Minimum Cost Network Flow Problems

all special cases of minimum cost network flow problems (MCNFP)

* The transportation, assignment, transshipment, shortest path, maximum flow, and CPM problems 
* emphasis on flow balance  
  * node
  * arc

![image-20180828215922651](https://ws2.sinaimg.cn/large/006tNbRwly1fuqdzq8u2nj30au03ldfs.jpg)

![image-20180828215936944](https://ws1.sinaimg.cn/large/006tNbRwly1fuqdzyxiwfj306y05f0sx.jpg)



#### 8.6 Minimum Spanning Tree Problems

to ‘connect’ all nodes with minimum distance (cost, time) in a graph

##### **minimum spanning tree** 

* A tree is a set of arcs without a loop
* A spanning tree is a tree that connects **all of the nodes**.

##### method 

* MST Algorithm 
  * Select any node. 
  * Select the node whose distance to any of the already selected nodes is the smallest.  
  * Repeat this step until all nodes are connected.  Tie can be broken arbitrarily.
* nE.g., start from node 1.

![image-20180828220759139](https://ws2.sinaimg.cn/large/006tNbRwly1fuqe8q4r6fj30jc02vgma.jpg)



### C_ 9  Integer Programming (IP)

#### 9.1 Introduction to IP

- Pure integer programming (IP) 
  All variables are required to be integers.
- Mixed integer programming (MIP)
  Only a part of the variables are required to be integers. 
- 0-1 IP
  All variables are binary (0 or 1).
- LP relaxation of an IP
  The LP obtained by removing integer requirements of an IP.

#### 9.2 Formulation

* Knapsack problem
  * An IP with one constraint (such as what is given above.)
  * volume (or weight) and capacity.
  * pleasure or reward.
* Additional constraint
  * logical
* Fixed-Charge Problems (Set up cost)
  * rent machines 
* Lockbox (Location-allocation problem)  
* Facility Location (Set-Covering Problems)



##### Either-Or Constraint

![image-20180829085552838](https://ws1.sinaimg.cn/large/006tNbRwly1fuqwytpa8nj30fh02w74b.jpg)

* Here, by using M, we nullify one of the two constraints

eg:

* Constraint: xi: either  xi≤0  
                            or        xi ≥1000  (1000-xi≤0)
    Formulation: xi≤Myi
                           1000-xi≤M(1-yi)  

##### If-then Constraint

![image-20180829090532388](https://ws4.sinaimg.cn/large/006tNbRwly1fuqx8voaw2j30d6032glo.jpg)



If f>0, then y should be zero (from the first line).  
And then, if y is zero, g should be non-negative (from the second line).



Piecewise linear function





##### Piecewise linear function

- A piecewise linear function consists of several straight line segments.
- ![image-20180829090944057](https://ws4.sinaimg.cn/large/006tNbRwly1fuqxd81qhvj305o02rgle.jpg)
- At break points, the slopes of the piecewise linear functions change.
- A piecewise linear function is not a linear function, and LP cannot be used to solve the optimization problem. However, by using 0-1 variables, a piecewise linear function can be represented in a linear form.



#### 9.3 BB Method

The Branch-and-Bound Method for Solving Pure Integer Programming Problems

**methods:**

* Branch and Bound method 
*  cutting plane method

##### Concept

Let us consider the following IP problem with the feasible area                  shown here.
            Max z=3x1+2x2
            st.        2x1+x2 ≤ 6
            x1, x2: non-negative integer
IP is difficult to solve.  (I.e., it takes a long time.  There is no good procedure known for this.)

* Complexity Theory
  In practice, most IPs are solved by some versions of the branch-and-bound procedure.  Branch-and-bound (BB) methods **implicitly enumerate** all possible solutions to an IP.

how does it work?

* The BB procedure cuts the feasible area and solves the subproblems.  
* relax (remove) the integer constraints, and solve LP relaxation of the IP, and use its result.
* We make many subproblems, and so, solving an IP takes a long time.  



Factors that affect the solution time of LP and IP.

* n<m<#integer variables<special problem structure

eg.

* ![image-20180829092055675](https://ws4.sinaimg.cn/large/006tNbRwly1fuqxozpuhij30i30begms.jpg)
* notation: For a max problem, we have,
  * **Candidate solution**: solution that meets all constraints including the integer requirements.
  * **Lower Bound** (of the opt z value): The best (maximum) z value of candidate solutions found so far.  
    If an LP relaxation gives z-value (UB) that is smaller than the current LB, we do not need to consider the LP relaxation any more. We want to find a large LB (or tight LB).
  * **Fathom**: not considering its subproblem anymore. This can be because 
    (1) the problem is infeasible, 
    (2) a candidate (or integer) solution is found, or 
    (3) its LB is lower than the current LB.
         If we cannot fathom, we continue branching.

##### General approaches

Two general approaches are used to determine which subproblem should be solved next.

* The most widely used is LIFO (or **backtracking**).
  	LIFO solves the subproblem made last first.  This leads us <u>down one side</u> of the branch-and-bound tree quickly and finds a candidate solution quickly. 
* The second commonly used approach is **jumptracking**.
  	When branching on a node, the jumptracking method solves all the problems created by branching together.  After solving all these, BB selects the best one (largest z value), solves it, and branches it.
    	Needs **more subproblems and more memory** than backtracking. Jumptrcking generally approaches the opt z-value **quicker** than backtracking.



Unimodular matrix and IP 









##### Unimodular matrix and IP 

* unimodular matrix :  any square sub-matrix of a matrix has a determinant of 1, 0, or -1
* **theorem**: When we solve Ax=b, if A is unimodular and b has only integer values, the solution, x, has only integer values.  
  * So, if the conditions for A and b are met for an IP, then we do not need to put the integer constraints on x.
* A unimodular A matrix of an IP makes the IP solution much faster.
* tolerance setting (eg. 20%)
  * causes the solver to stop when a feasible solution is found that has an objective function value within 20% of the original LP relaxation.
  * 5% of tolerance is often used.

9.4 covers MIP problems

9.5 covers the important Knapsack Problem

9.6 covers more examples such as scheduling and Traveling Sales Person (TSP)  

* heuristic approach







[^1]: 标准型