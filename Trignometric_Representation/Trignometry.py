import numpy as np
import matplotlib.pyplot as plt
# Function for Plotting Sine Functions
def perform():
    def f(x):
        return np.sin(x)
    x = np.linspace(-2*np.pi,2*np.pi, 1000)
    plt.plot(x,f(x), label='sin(x)', color='blue')
    plt.title('SIN(X)')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True)
    plt.show()
# Function for Plotting Cosine Functions
def performs():
    def f(x):
        return np.cos(x)
    x = np.linspace(-2*np.pi,2*np.pi, 1000)
    plt.plot(x,f(x), label='COSINE(x)', color='blue')
    plt.title('COSINE(X)')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True)
    plt.show()
# Function for Plotting Tangent Functions
def tangents():
    def f(x):
        return np.tan(x)
    x = np.linspace(-2*np.pi,2*np.pi, 1000)
    plt.plot(x,f(x), label='Tangent(x)', color='blue')
    plt.title('Tan(X)')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True)
    plt.show()
ins = input("Trigonometric symbol?: ").casefold()
if ins in ['sin','cosine','tangent']:
    if ins == 'sin':
        perform()
    if ins == 'cosine':
        performs()
    if ins == 'tangent':
        tangents()
else:
    print("Invalid Input! ")