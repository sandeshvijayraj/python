import math
import pylab as plt
import math
import numpy as np

n = 100
x = np.linspace(0, 2 * math.pi, n)[:,np.newaxis]
y =np.sin(x) + 0.3*np.random.randn(n)[:,np.newaxis]

print("len",x)
print("len2",len(y))
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
poly = PolynomialFeatures(degree = 5)
X_poly = poly.fit_transform(x) 
poly.fit(X_poly, y) 
lin2 = LinearRegression()
lin2.fit(X_poly, y)

plt.plot(x, y, color = 'blue' , label='y noisy') 
plt.plot(x, lin2.predict(poly.fit_transform(x)), color = 'red', label='y pred') 
plt.title('sandesh bafna')
plt.legend()
plt.show()