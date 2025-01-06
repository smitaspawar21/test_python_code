import matplotlib.pyplot as plt
import numpy as np

x = ["jan","feb","march","Apr","MAy","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
y = [1,2,3,5,5,10,12,14,13,10,8,9]

plt.plot(x,y,marker="o",color="blue")
plt.xlabel("Months")
plt.ylabel("Sale")
plt.legend("polynimial")
plt.savefig("matplot.jpeg")


