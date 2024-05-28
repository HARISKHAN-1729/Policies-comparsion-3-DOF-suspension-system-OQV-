# Comparsion of the performance of active suspension system for a OQV, when subjected to different road conditions

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [System dynamics](#dynamics)
- [Results](#results)
- [Installation and Usage](#installation-and-usage)
- [Project Structure](#project-structure)
- [Bibliography](#bibliography)

---

## **Overview**
This repository hosts a detailed simulation of an active suspension system designed for a quarter-car model. This work was developed as part of the Advanced Control Methods course at Skoltech in 2024, focusing on improving vehicle dynamics under varying road conditions through advanced control techniques such as PID and LQR controllers.

- **Course:** Advanced Control Methods, Skoltech, 2024.
- **Team Members:** Haris Khan, Luis moreno, Amir Habel.
- **Final Presentation:** [[Link to Presentation]](https://docs.google.com/presentation/d/1QHCL57dTlITRUsoKisLSNBh8ljAMnTm1lT-WeIaO3NM/edit#slide=id.g2e06ae9955a_1_902).ttat


## **Problem Statement**
- Introduction:
  
  The performance of a vehicle's suspension system is pivotal in defining both the ride quality for passengers and the handling characteristics for drivers. Traditional passive suspension systems, consisting of        fixed-setting springs and dampers, often struggle to maintain an optimal balance between these two critical aspects, particularly across varying and unpredictable road conditions. The rigidity in passive systems 
  means they cannot adapt to changes in road surface, speed, or vehicle load dynamically, which can lead to compromised comfort and safety.

- Challenges with Passive Suspension Systems:
  
  Passive suspensions are inherently limited by their inability to adjust to real-time road dynamics. This limitation manifests in several ways:

  - Ride Comfort:

    Inadequate absorption of road irregularities leads to significant vehicle body vibrations, adversely affecting passenger comfort.
    
  - Handling Performance:
  
    Insufficient dynamic adjustment capabilities during maneuvers such as cornering, braking, or avoiding obstacles can result in suboptimal handling and stability.
    
  - Safety and Wear:
  
    The constant transmission of road shocks through a vehicle not only increases the wear and tear on its structural components but also elevates the risk of loss of contact between the tire and road surface, 
    potentially leading to dangerous driving situations.

   The Promise of Active Suspension Systems:
    
    Active suspension systems represent a technological advancement aimed at addressing these shortcomings. By utilizing adjustable components that can change their stiffness and damping characteristics in real- 
    time, active suspensions provide a more adaptable solution. They react to road inputs by actively controlling the suspension setup, thus maintaining vehicle stability and passenger comfort across a broader range 
    of conditions.

  # **Objectives of This Project:**
    
    The primary goal of this project is to demonstrate the superiority of different policies for active suspension systems using a quarter-car model, when subjected to different road conditions. Through the simulation, we aim to:

    - Optimize Ride Quality:
    
      By minimizing the vertical acceleration of the sprung mass, thereby reducing the sensation of road bumps and enhancing overall passenger comfort.
      
    - Enhancing Body Motion Control:
      
      Minimize bounce, pitch, and roll during cornering and braking to stabilize the sprung mass and maintain its nominal position.
      
    - Improving Vehicle Handling:
      
      Enhance the vehicle's ability to respond correctly to driver commands, particularly under critical conditions, by minimizing the displacement between the sprung and unsprung mass. 


      
    - Evaluate Control Strategies:
      Specifically, the project compares two types of control methods:
      
      - Proportional-Integral-Derivative (PID) Control:
        
        A widely used control strategy that adjusts the control inputs based on error, its integral over time, and its derivative.
        
      -  Linear Quadratic Regulator (LQR) Control:
        
        An optimal control strategy that aims to minimize a quadratic cost function, balancing the state and control efforts.
      
  **Significance and Impact:**
  
    The outcomes of this project have implications for automotive design and safety standards, particularly in how vehicles are engineered to cope with increasing demands for passenger comfort and vehicle agility. 
    By scientifically validating the performance benefits of active suspension systems, this research could influence future regulatory standards for automotive safety and environmental impact, considering that 
    improved handling can contribute to more efficient driving patterns and lower emissions.

# **System Dynamics:**

  <p align="center">
  <img src="images/system.png" alt="Active Suspension System" width="600"/>
  </p>

  **System Description:**
  
  **The quarter-car model includes:**
  
  - **Sprung mass (ms):** Represents the weight of the vehicle body.
  
  - **Unsprung mass (mus):** Represents the weight of the wheels and other components not supported by the springs.
  
  - **Suspension stiffness (ks):**  The stiffness of the springs supporting the sprung mass.
  
  - **Tire stiffness (kus):** The stiffness of the tires, which act as additional springs.
  
  - **Suspension damping (bs):** Damping component that controls the energy dissipation in the suspension system.
  
  - **Tire damping (bus):** Damping component associated with the tires.
  
  - **Road input (Zr):** Represents the vertical displacement due to road irregularities.

# **Differential Equations:**

 The dynamic behavior of this system is described by two differential equations that model the forces acting on both the sprung and unsprung masses. These equations 
 account for the spring and damping forces, as well as the control force exerted by the active suspension system (Fa).

### Dynamics Equations

1. **Equation for the Sprung Mass (\(m_s\))**:

   <p align="center">
   <img src="images/equation1.png" " width="600"/>
   </p>
   
2. **Equation for the Unsprung Mass (\(m_{us}\))**:

    <p align="center">
    <img src="images/equation2.png"" width="600"/>
    </p>


 ### States

   The state variables used for modeling and controlling the active suspension system based on a quarter-car model. These state variables, essential for the implementation of both PID and LQR controllers, are 
   outlined as follows:

   - x1 = Zs − Zus: This represents the suspension travel, which is the relative displacement between the sprung mass and the unsprung mass. It is a critical parameter for assessing and controlling the overall 
     suspension behavior, especially in terms of how well the suspension can absorb road irregularities and maintain vehicle stability.

   - x2 = Żs: This is the velocity of the sprung mass. Controlling this state variable is important for minimizing the oscillations of the vehicle's body, thereby improving ride comfort by reducing the impact of 
     bumps and other road surface imperfections.

   - x3 = Zus − Zr: Known as the wheel’s deflection, it measures the relative displacement between the unsprung mass and the road profile. This state is crucial for maintaining proper wheel-road contact, which is 
     fundamental for vehicle safety and handling.

   - x4 = ˙Zus: The vertical velocity of the unsprung mass, which affects how quickly the unsprung mass responds to road surface changes. Controlling this velocity helps in optimizing the interaction between the 
     tire and road, crucial for effective shock absorption and minimizing transmission of road noise and vibrations.

# **Results**
   <p align="center">
    <img src="images/simulation_plots.png"" width="600"/>
    </p>

1. Sprung Mass Velocity
   
  Description: This plot shows the velocity of the sprung mass over time. The sprung mass typically represents the vehicle body supported by the suspension.
  
  Red Line (PID): Shows fluctuations that suggest more frequent adjustments or corrections by the PID controller in response to road irregularities, leading to a somewhat less smooth velocity profile.
  
  Blue Line (LQR): Demonstrates a smoother response compared to PID, indicative of the LQR controller's ability to optimize control actions based on a predefined cost function that likely balances performance and 
  control effort.
  
2. Wheel Vertical Velocity
     
  Description: This graph displays the vertical velocity of the wheel, which directly impacts ride comfort and handling by affecting how the wheel interacts with the road surface.
  
  Red Line (PID): Exhibits sharp spikes, reflecting rapid changes in wheel velocity which could correspond to sudden impacts or bumps in the road.
  
  Blue Line (LQR): Similar to the PID, but potentially with slight damping effects that smoothen the response, indicating effective control over the unsprung mass dynamics.
  
3. Acceleration
     
  Description: Shows the acceleration experienced by the vehicle's sprung mass, a critical factor for assessing ride comfort.
  
  Red Line (PID): Displays significant peaks, especially at around 1 second and 2.5 seconds, suggesting strong responses to road bumps or other disturbances.
  
  Blue Line (LQR): While also showing peaks, the LQR line appears to smooth out more quickly than PID, potentially offering a more comfortable ride by minimizing high magnitude accelerations.
  
4. Wheel’s Deflection
   
  Description: This plot measures the deflection of the wheel relative to the vehicle body, which is important for maintaining good tire-road contact.

  Red Line (PID) and Blue Line (LQR): Both lines track closely together, showing similar patterns of deflection. This indicates that both controllers are maintaining comparable wheel positioning, which is crucial 
  for effective shock absorption and overall stability.
  
-5. Spring Travel

  Description: Represents the travel of the suspension spring, which is directly related to how well the suspension can absorb road shocks and maintain vehicle stability.
  
  Red Line (PID): The PID controller shows more variability in spring travel, which can be interpreted as a more reactive or less consistent damping strategy.
  
  Blue Line (LQR): Exhibits smoother transitions and less extreme changes in spring travel, suggesting better overall control of suspension movement and potentially enhanced ride quality.
  
**Analysis Summary:**
  These graphs collectively demonstrate the dynamic behavior of the vehicle's suspension system as controlled by PID and LQR strategies under simulated conditions. The LQR controller generally shows smoother   responses and potentially better performance in terms of ride comfort and handling stability compared to the PID controller. This could be attributed to the LQR's approach to minimizing a cost function that likely includes terms for control effort and deviation from desired states, thus achieving a more balanced and optimized response.
  
  Both controllers are effective, but the choice between them may depend on specific performance criteria, such as the priority between ride comfort (where LQR may excel) and responsiveness (where PID may provide sharper control).

# **Installation and Usage:**

**Prerequisites**

Ensure you have Python installed on your system. It's recommended to use Python 3.6 or newer. Download Python from python.org.

**Cloning the Repository**

 First, clone the repository to your local machine by running:
 ``` bash
     git clone https://github.com/your-username/your-repository-name.git
     cd your-repository-name
```

Replace https://github.com/your-username/your-repository-name.git with the actual URL of your repository.
