{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import matplotlib.pyplot as plt\
\
# Fixed sensitivity\
sensitivity = 0.99\
\
# Define ranges for prevalence and specificity\
prevalence = np.linspace(0.00001, 0.50, 500)  # 0.001% to 50%\
specificity_values = [0.99, 0.999, 0.9999, 0.99999]\
\
# Function to calculate probability of infection given a positive test\
def prob_infected(sensitivity, specificity, prevalence):\
    return (sensitivity * prevalence) / ((sensitivity * prevalence) + ((1 - specificity) * (1 - prevalence)))\
\
# Plot\
plt.figure(figsize=(10, 6))\
for specificity in specificity_values:\
    probabilities = prob_infected(sensitivity, specificity, prevalence)\
    plt.plot(prevalence * 100, probabilities * 100, label=f'Specificity = \{specificity * 100:.3f\}%')\
\
plt.xlabel('Prevalence (%)')\
plt.ylabel('Probability of Infection Given Positive Test (%)')\
plt.title('Probability of Infection Given Positive Test vs. Prevalence')\
plt.legend()\
plt.grid(True)\
plt.show()}