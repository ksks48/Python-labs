def check(a, N=5000):
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    rnd = np.random.RandomState(0)
    for _ in range(N):
        x = rnd.rand()*(6)-3 #*(b-a)+a
        y = rnd.rand()*(6)-3 
        if eval(a):
            plt.plot(x, y, "k.", markersize=1)
    plt.show();        

#This is an example how to call check() function
check('x**2+y**2<4 and (x**2+y**2>2)', 8000)
